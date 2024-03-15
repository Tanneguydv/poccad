##Author github user @Tanneguydv, 2021

import os
import os.path
import sys
import webbrowser
import numpy
from io import StringIO
import contextlib
import traceback
import time
import PyQt5
from qtpy import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QInputDialog, QFileDialog, QTreeWidgetItem, QTreeWidgetItemIterator

from OCC.Display.backend import load_backend
load_backend('qt-pyqt5')
import OCC.Display.qtDisplay as qtDisplay

import lib.Scripts as sc
from lib.Scripts import Shape, Construction, Boolean
from poccad import Ui_poccad
from lib.Shapemaker import MakeShape
from lib.Shapemaker import *
import lib.OCC_functions as occ

class Application(PyQt5.QtWidgets.QMainWindow):

    def __init__(self,app, parent=None):

        super(Application, self).__init__(parent)

        self.ui = Ui_poccad()
        self.ui.setupUi(self)

        self.canvas = qtDisplay.qtViewer3d(self)
        self.ui.OCClayout.addWidget(self.canvas)
        self.canvas.resize(829,739)
        self.canvas.InitDriver()
        self.display = self.canvas._display
        self.shape_converter = ShapeConverter()

        #ASSOCIATE Functions to display
        self.ui.render_button.clicked.connect(self.render_file)
        self.ui.isoview_button.clicked.connect(lambda : self.setview('Iso'))
        self.ui.topview_button.clicked.connect(lambda : self.setview('Top'))
        self.ui.leftview_button.clicked.connect(lambda: self.setview('Left'))
        self.ui.frontview_button.clicked.connect(lambda: self.setview('Front'))
        self.ui.rightview_button.clicked.connect(lambda: self.setview('Right'))
        self.ui.bottomview_button.clicked.connect(lambda: self.setview('Bottom'))
        self.ui.rearview_button.clicked.connect(lambda: self.setview('Rear'))

        self.ui.set_active_layer_button.clicked.connect(self.set_active_layer)
        self.ui.create_layer_button.clicked.connect(self.create_layer)

        self.ui.actionNew.triggered.connect(self.new_file)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave_as.triggered.connect(self.save_file_as)
        self.ui.actionExport.triggered.connect(self.export_file)
        self.ui.actionQuit.triggered.connect(self.quit)
        self.ui.actionAbout.triggered.connect(self.dialog_about)
        self.ui.actionUser_Guide.triggered.connect(self.user_guide_html)

        self.ui.actionBox.triggered.connect(self.makebox)
        self.ui.actionCylinder.triggered.connect(self.makecylinder)
        self.ui.actionSphere.triggered.connect(self.makesphere)
        self.ui.actionPoint.triggered.connect(self.drawpoint)
        self.ui.actionAxis.triggered.connect(self.drawaxis)
        self.ui.actionCut.triggered.connect(self.boolcut)
        self.ui.actionTranslate.triggered.connect(self.translate)
        self.ui.actionExportstep.triggered.connect(self.exportstep)

        self.changeviewval = 0
        self.render = False

        self.initialize()
        self.ui.OCCedit.textChanged.connect(self.changetext)

        self.cwd = os.getcwd()

        self.ui.treelayers.itemDoubleClicked.connect(self.change_layer_state)
        self.ui.treelayers.itemSelectionChanged.connect(self.on_item_selection_changed)



        self.lauching()

    def lauching(self):
        lauchingfile = 'files/3axis.pocc'
        with open (lauchingfile, 'r') as lf :
            for line in lf.readlines():
                if line == "\n":
                    self.ui.OCCedit.appendPlainText((line.strip('\n')))
                else :
                    self.ui.OCCedit.appendPlainText((line.strip('\n')))
        self.render_file()

    def user_guide_html(self):
        try :
            webbrowser.open(self.cwd + '\docs\_build\html\index.html')
        except:
            self.ui.Consult.appendPlainText('no html file found')

    def on_contextmenu_tree(self, point):
        self.popTreeMenu.exec_(self.ui.treeWidget.mapToGlobal(point))

    def changetext(self):
        if self.ui.OCCedit.toPlainText().endswith(':\n'):
            self.ui.OCCedit.insertPlainText('\t')
        if self.ui.OCCedit.toPlainText().endswith('='):
            print ('variable')

    def initialize(self):
        self.box = False
        self.cylinder = False
        self.sphere = False
        self.point = False
        self.axis = False
        self.booleancut = False
        self.translate = False
        self.expstep = False
        self.file_issaved = False
        self.selected_item = "base_layer"
        self.set_active_layer()
        # self.active_layer = ["base_layer" , False]

    def setview(self, view):
        self.ui.activeview.setPixmap(QPixmap('ui_files/icons/'+ (view) + '_on.png'))
        dispview = 'self.display.View_' + (view)+'()'
        exec (dispview)
        self.display.FitAll()

    def new_file(self):
        self.ui.OCCedit.clear()
        self.ui.output.clear()
        self.display.EraseAll()
        self.initialize()
        self.ui.output.appendPlainText('new codesheet')
        # clear the tree layer
        iterator = QTreeWidgetItemIterator(self.ui.treelayers, QTreeWidgetItemIterator.All)
        while iterator.value():
            iterator.value().takeChildren()
            iterator += 1
        i = self.ui.treelayers.topLevelItemCount()
        while i > -1:
            self.ui.treelayers.takeTopLevelItem(i)
            i -= 1

    def open_file(self):
        self.initialize()
        self.ui.output.clear()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.occ_file_path, _ = QFileDialog.getOpenFileName(parent=self, caption='Select File to open',dir='',filter="pocc Files (*.pocc);;All Files (*)", options=options)
        if self.occ_file_path:
            self.ui.output.appendPlainText('open ' + str(self.occ_file_path))
            self.file_issaved = True
            self.saved_file = (str(self.occ_file_path))
            self.ui.OCCedit.clear()
            with open (self.occ_file_path, "r") as opened_file:
                for line in opened_file:
                    self.ui.OCCedit.appendPlainText(line.strip('\n'))
        else :
            pass

    def save_file(self):
        if self.file_issaved == False :
            self.save_file_as()
        else :
            cad_edit = self.ui.OCCedit.toPlainText()
            self.ui.output.appendPlainText('saving ' + str(self.saved_file))
            with open (self.saved_file, "w") as cfe :
                for line in cad_edit:
                    if line.startswith("display = self.display"):
                        pass
                    if line.startswith('display.FitAll()'):
                        pass
                    else:
                        cfe.writelines(line)

    def save_file_as(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getSaveFileName(self,"Save file as","","All Files (*);;pocc Files (*.pocc)", options=options)
        if self.fileName:
            self.file_issaved = True
            self.saved_file = (str(self.fileName)+'.pocc')
            self.ui.output.appendPlainText('saving ' + str(self.saved_file))
            cad_edit = self.ui.OCCedit.toPlainText()
            with open (self.saved_file, "w") as cfe :
                for line in cad_edit:
                    if line.startswith("display = self.display"):
                        pass
                    if line.startswith('display.FitAll()'):
                        pass
                    else:
                        cfe.writelines(line)
        else :
            pass

    def export_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getSaveFileName(self,"Export file as","","All Files (*);;pocc Files (*.pocc);; Python Files (*.py)", options=options)
        if self.fileName:
            self.exported_file = (str(self.fileName)+'.py')
            self.ui.output.appendPlainText('exporting as' + str(self.exported_file))
            cad_edit = self.ui.OCCedit.toPlainText()
            with open (self.exported_file, "w") as cfe :
                cfe.write("#file generated with poccad under GPL-3.0 License\n#please visit https://github.com/Tanneguydv/poccad\nfrom OCC.Display.SimpleGui import init_display\ndisplay,start_display, add_menu,add_functionto_menu = init_display()\n")
                for line in cad_edit:
                    if line.startswith("display = self.display"):
                        pass
                    elif line.startswith('display.FitAll()'):
                        pass
                    else:
                        cfe.writelines(line)
                cfe.write("\ndisplay.FitAll()\nstart_display()\n")

        else :
            pass
        
    def render_file(self):
        print('render')
        #clear the tree layer
        iterator = QTreeWidgetItemIterator(self.ui.treelayers, QTreeWidgetItemIterator.All)
        while iterator.value():
            iterator.value().takeChildren()
            iterator += 1
        i = self.ui.treelayers.topLevelItemCount()
        while i > -1:
            self.ui.treelayers.takeTopLevelItem(i)
            i -= 1

        if os.path.isfile("cad_file_edit.pocc"):
            os.remove("cad_file_edit.pocc")
        self.display.EraseAll()
        cad_edit_text = self.ui.OCCedit.toPlainText()
        cad_edit = cad_edit_text.splitlines()
        with open ("cad_file_edit.pocc", "a") as cfe :
            final_layers_show = []
            cfe.write("display = self.display\n")
            for line in cad_edit:
                if line.startswith("display = self.") :
                    pass
                elif line.startswith('display.FitAll()'):
                    pass
                elif 'layer' in line and ".show" in line:
                    print("cad edit ", line)
                    final_layers_show.append(line)
                elif 'layer' in line and ".hide" in line:
                    final_layers_show.append(line)
                else :
                    print(line)
                    cfe.writelines(line + '\n')
            for line in final_layers_show:
                print("final_layers_show  ", line)
                cfe.writelines(line + '\n')
            cfe.write('\ndisplay.FitAll()')
        cfe.close()

        with open ("cad_file_edit.pocc", "r") as cfe :
            layers = []
            lines = cfe.readlines()
            for line in lines:
                if 'display.Display' in line :
                    layer = line.split('=', 1)
                    layername = layer[0]
                    if line.startswith('#'):
                        layername = layername.strip('#')
                        self.load_tree_layers(layername, 'off')
                    else :
                        self.load_tree_layers(layername, 'on')
                    print(layername)
                elif 'layer' in line and '=' in line: #TODO ne sert à rien pour le moment
                    layer = line.split(' =', 1)
                    layername = layer[0]
                    layers.append([layername, 'on'])
                    # self.load_tree_layers(layername, 'on')
                # elif 'layer' in line and ".show" in line:
                #     layer = line.split('.', 1)
                #     layername = layer[0]
                #     self.load_tree_layers(layername, 'on')
                #     print(layername)
                elif 'layer' in line and ".hide" in line:
                    layer = line.split('.', 1)
                    layername = layer[0]
                    for layer in layers:
                        if layer[0] == layername:
                            layer[1] = 'off' 
                    # layers.append([layername, 'off'])
                    # self.load_tree_layers(layername, 'off')
                    # print(layername)
            for layername in layers:
                self.load_tree_layers(layername[0], layername[1])
        cfe.close()

        # refresh occedit
        with open ("cad_file_edit.pocc", "r") as cfe :
            self.ui.OCCedit.clear()
            lines = cfe.readlines()
            for line in lines:
                if "display = self." in line :
                    pass
                elif line.startswith('display.FitAll()'):
                    pass
                elif line == '\n':
                    pass
                else:
                    self.ui.OCCedit.appendPlainText(line.strip('\n'))
        cfe.close()

        #get the print output in an exec statement
        try :
            @contextlib.contextmanager
            def stdoutIO(stdout=None):
                old = sys.stdout
                if stdout is None:
                    stdout = StringIO()
                sys.stdout = stdout
                yield stdout
                sys.stdout = old

            with stdoutIO() as s:
                exec(open("cad_file_edit.pocc").read())
            self.ui.output.appendPlainText(str(s.getvalue()))
            self.render = True
        except Exception :
            self.ui.output.appendPlainText(str(traceback.format_exc()))

    def dialog_about(self):
        infobox = QtWidgets.QDialog()
        infobox.setObjectName("infobox")
        infobox.resize(721, 379)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_files/icons/poccad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        infobox.setWindowIcon(icon)
        self.logo = QtWidgets.QLabel(infobox)
        self.logo.setGeometry(QtCore.QRect(10, 10, 701, 311))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("readme_files/poccad_github.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.infotext = QtWidgets.QLabel(infobox)
        self.infotext.setGeometry(QtCore.QRect(190, 340, 291, 16))
        self.infotext.setAutoFillBackground(True)
        self.infotext.setScaledContents(False)
        self.infotext.setOpenExternalLinks(True)
        self.infotext.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextSelectableByMouse)
        self.infotext.setObjectName("infotext")
        QtCore.QMetaObject.connectSlotsByName(infobox)
        _translate = QtCore.QCoreApplication.translate
        infobox.setWindowTitle(_translate("infobox", "poccad_info"))
        self.infotext.setText(_translate("infobox", "please visit https://github.com/Tanneguydv/poccad"))
        infobox.exec_()

    def quit(self):
        if os.path.isfile("cad_file_edit.pocc"):
            os.remove("cad_file_edit.pocc")
        sys.exit()

    #LAYERS

    def load_tree_layers(self, layername, state):
        displaylayer = QTreeWidgetItem(self.ui.treelayers, [layername])
        if state == 'on':
            if 'layer' in layername :
                displaylayer.setIcon(0, QIcon('ui_files/icons/shape_layer_on.png'))
            elif 'Point' in layername:
                displaylayer.setIcon(0, QIcon('ui_files/icons/construction_layer_on.png'))
            elif 'Axis' in layername:
                displaylayer.setIcon(0, QIcon('ui_files/icons/construction_layer_on.png'))
            elif 'Plane' in layername:
                displaylayer.setIcon(0, QIcon('ui_files/icons/construction_layer_on.png'))
            elif 'Curve' in layername:
                displaylayer.setIcon(0, QIcon('ui_files/icons/construction_layer_on.png'))
        if state == 'off':
            if 'layer' in layername :
                displaylayer.setIcon(0, QIcon('ui_files/icons/shape_layer_off.png'))
            elif 'Point' in layername:
                displaylayer.setIcon(0, QIcon('ui_files/icons/construction_layer_off.png'))
            elif 'Axis' in layername:
                displaylayer.setIcon(0, QIcon('ui_files/icons/construction_layer_off.png'))
            elif 'Plane' in layername:
                displaylayer.setIcon(0, QIcon('ui_files/icons/construction_layer_off.png'))
            elif 'Curve' in layername:
                displaylayer.setIcon(0, QIcon('ui_files/icons/construction_layer_off.png'))

    def change_layer_state(self, item):
        print (item)
        layer = item.text(0)
        print(str(layer))
        #self.ui.treelayers.takeTopLevelItem(self.ui.treelayers.indexOfTopLevelItem(item))
        #displaylayer = QTreeWidgetItem(self.ui.treelayers, [layer])
        with open ("cad_file_edit.pocc", "r") as cfe :
            self.ui.OCCedit.clear()
            lines = cfe.readlines()
            for line in lines:
                if 'display.Display' in line :
                    if str(layer) in line :
                        if line.startswith('#'):
                            line = line.strip('#')
                            self.ui.OCCedit.appendPlainText(line.strip('\n'))
                        else :
                            line = '#'+str(line)
                            self.ui.OCCedit.appendPlainText(line.strip('\n'))
                    else :
                        self.ui.OCCedit.appendPlainText(line.strip('\n'))
                elif 'layer' in line :
                    layer = layer.replace(" ", "")
                    if str(layer) in line :                        
                        if 'show' in line:
                            line = line.replace('show', 'hide')
                            self.ui.OCCedit.appendPlainText(line.strip('\n'))
                        else :
                            line = line.replace('hide', 'show')
                            self.ui.OCCedit.appendPlainText(line.strip('\n'))
                    else :
                        self.ui.OCCedit.appendPlainText(line.strip('\n'))
                else :
                    if "display = self." in line :
                        pass
                    elif line.startswith('display.FitAll()'):
                        pass
                    elif line == '\n':
                        self.ui.OCCedit.appendPlainText(line.strip('\n'))
                    else:
                        self.ui.OCCedit.appendPlainText(line.strip('\n'))

        cfe.close()
        self.render_file()

    def on_item_selection_changed(self):
        selected_items = self.ui.treelayers.selectedItems()
        if selected_items:
            selected_item = selected_items[0]  # Prendre le premier élément sélectionné
            self.selected_item =  str(selected_item.text(0))
            print("Nom:", selected_item.text(0))

    def set_active_layer(self):
        print(self.selected_item)
        if "layer" in self.selected_item:
            layer = self.selected_item
            print("layer = ", layer)
        else:
            layer = "base_layer" 
        self.active_layer = [layer, False] 
        print(self.active_layer)
        self.ui.active_layer_label.setText("active layer is " + str(self.active_layer[0]))

    def create_layer(self):
        dialog = CreateLayerDialog()
        name, color, transparency = dialog.get_user_input()
        line = name + "_layer = occ.Layer(display, color=" + str(color) + ", transparency=" + str(transparency) + ")"
        self.ui.OCCedit.appendPlainText(line)
        self.render_file()

    def add_shape_to_layer(self, shape_name):
        # active_layer = self.get_active_layer()
        self.ui.OCCedit.appendPlainText(self.active_layer[0] + '.add_shape(' + shape_name + ')')
        if not self.active_layer[1]:
            self.ui.OCCedit.appendPlainText(self.active_layer[0] + '.show()')
            self.active_layer[1] = True

    #PythonOCC functions :

    def make_maker(self, maker):
        # widget = ShapeMakerDialog(maker.parameters)
        # self.ui.shape_maker_layout.addWidget(widget)
        self.ui.tabWidget.setCurrentIndex(2)
        dialog = ShapeMakerDialog(maker, self.display)
        self.ui.shape_maker_layout.addWidget(dialog)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            line_input = dialog.get_input()
            print(f'line entered: {line_input}')

        # make_box = CenterPoint()
        print(maker.generate_prompt())


        command = maker.generate_command(line_input)
        self.ui.OCCedit.appendPlainText(command)
        print(command)
        shape_name = command.split(" =")[0]
        self.add_shape_to_layer(shape_name)
        self.ui.entryline.clear()
        self.render_file()
        self.ui.output.appendPlainText('Rendering file...')
        self.ui.OCCedit.setFocus()
    #Shape

    def center_point_face(self):
        maker = CenterPoint()
        self.make_maker(maker)

    def makebox(self):
        maker = MakeBox()
        self.make_maker(maker)

    def makecylinder(self):
        maker = MakeCylinder()
        self.make_maker(maker)
        
    def makesphere(self):

        def init():
            self.makingsphere = True
            self.radius_on = False
            self.name_on = False
            self.origin_on = False
            self.angle_on = False
            self.portion_on = False
            self.radius = '5'
            self.name = 'sphere'
            self.origin = 'gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))'
            self.angle = 'radians(90)'
            self.portion = 'radians(360)'
            self.ui.treelayers.clearSelection()
            self.ui.output.appendHtml('Press Enter or specify : <u>N</u>ame, <u>O</u>rigin (point,dir), <u>R</u>adius, <u>A</u>ngle, <u>P</u>ortion')
            self.ui.entryline.setFocus()

        def param():
            try :
                if self.ui.entryline.text() == '' and self.origin_on == False: #what's to be selected in the tree layer must be False
                    print('send')
                    send_param()
                elif self.ui.entryline.text() == 'r':
                    print('r')
                    self.ui.output.appendHtml('Specify radius')
                    self.radius_on = True
                    self.ui.entryline.selectAll()
                elif self.ui.entryline.text() == 'n':
                    print('n')
                    self.ui.output.appendHtml('Specify name')
                    self.name_on = True
                    self.ui.entryline.selectAll()
                elif self.ui.entryline.text() == 'o':
                    print('o')
                    self.ui.output.appendPlainText('Choose an axis in the layer tree or specify its coordinates x,y,z;Dx,Dy,Dz')
                    self.origin_on = True
                    self.ui.entryline.selectAll()
                elif self.ui.entryline.text() == 'a':
                    print('a')
                    self.ui.output.appendPlainText('Specify the angle in degrees')
                    self.angle_on = True
                    self.ui.entryline.selectAll()
                elif self.ui.entryline.text() == 'p':
                    print('p')
                    self.ui.output.appendPlainText('Specify the portion in degrees')
                    self.portion_on = True
                    self.ui.entryline.selectAll()
                else :
                    if self.radius_on == True:
                        print('r true')
                        self.radius = self.ui.entryline.text()
                        self.radius_on = False
                        self.ui.output.appendHtml(
                            '<u>N</u>ame : ' + str(self.name) + ' , <u>O</u>rigin : ' + str(
                                self.origin)+ ' , <u>R</u>adius : ' + str(self.radius) + ' ,<u>A</u>ngle : ' + str(
                                self.angle)+' ,<u>P</u>ortion : ' +str(self.portion))
                        self.ui.entryline.selectAll()
                    if self.name_on == True:
                        print('n true')
                        self.name = self.ui.entryline.text()
                        self.name_on = False
                        self.ui.output.appendHtml(
                            '<u>N</u>ame : ' + str(self.name) + ' , <u>O</u>rigin : ' + str(
                                self.origin) + ' , <u>R</u>adius : ' + str(self.radius) + ' ,<u>A</u>ngle : ' + str(
                                self.angle) + ' ,<u>P</u>ortion : ' + str(self.portion))
                        self.ui.entryline.selectAll()
                    if self.origin_on == True :
                        shapes = self.ui.treelayers.selectedItems()
                        print('o true')
                        print(shapes)
                        if len(shapes) > 0:
                            layer_axis = str(shapes[0].text(0))
                            print(layer_axis)
                            self.origin = layer_axis.replace('_Axis', '')
                            self.origin_on = False
                            self.ui.output.appendHtml(
                                '<u>N</u>ame : ' + str(self.name) + ' , <u>O</u>rigin : ' + str(
                                    self.origin) + ' , <u>R</u>adius : ' + str(self.radius) + ' ,<u>A</u>ngle : ' + str(
                                    self.angle) + ' ,<u>P</u>ortion : ' + str(self.portion))
                            self.ui.entryline.selectAll()
                        else :
                            sphereparam = self.ui.entryline.text().split(';', 1)
                            point = sphereparam[0]
                            dir = sphereparam[1]
                            self.origin = 'gp_Pnt('+ point +'), gp_Dir('+ dir +')'
                            self.origin_on = False
                            self.ui.output.appendHtml(
                                '<u>N</u>ame : ' + str(self.name) + ' , <u>O</u>rigin : ' + str(
                                    self.origin) + ' , <u>R</u>adius : ' + str(self.radius) + ' ,<u>A</u>ngle : ' + str(
                                    self.angle) + ' ,<u>P</u>ortion : ' + str(self.portion))
                            self.ui.entryline.selectAll()
                    if self.angle_on == True:
                        print('a true')
                        self.angle = 'radians('+ self.ui.entryline.text() +')'
                        self.angle_on = False
                        self.ui.output.appendHtml(
                            '<u>N</u>ame : ' + str(self.name) + ' , <u>O</u>rigin : ' + str(
                                self.origin) + ' , <u>R</u>adius : ' + str(self.radius) + ' ,<u>A</u>ngle : ' + str(
                                self.angle) + ' ,<u>P</u>ortion : ' + str(self.portion))
                        self.ui.entryline.selectAll()
                    if self.portion_on == True:
                        print('p true')
                        self.portion = 'radians('+ self.ui.entryline.text() +')'
                        self.portion_on = False
                        self.ui.output.appendHtml(
                            '<u>N</u>ame : ' + str(self.name) + ' , <u>O</u>rigin : ' + str(
                                self.origin) + ' , <u>R</u>adius : ' + str(self.radius) + ' ,<u>A</u>ngle : ' + str(
                                self.angle) + ' ,<u>P</u>ortion : ' + str(self.portion))
                        self.ui.entryline.selectAll()
            except Exception as e:
                self.ui.output.appendPlainText(str(e))

        def send_param():
            if self.makingsphere == True:
                try :
                    if self.sphere == False:
                        self.ui.OCCedit.appendPlainText('from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere\n\
from OCC.Core.gp import gp_Ax2 , gp_Dir , gp_Pnt\n\
from math import radians\n')
                        self.ui.OCCedit.appendPlainText(Shape.make_sphere(self.name, self.origin ,self.radius, self.angle, self.portion))
                        self.sphere = True
                    else:
                        self.ui.OCCedit.appendPlainText(Shape.make_sphere(self.name, self.origin , self.radius, self.angle, self.portion))
                    self.ui.entryline.clear()
                    self.render_file()
                    self.ui.output.appendPlainText('Rendering file...')
                    self.ui.OCCedit.setFocus()
                    self.makingsphere = False
                    self.ui.entryline.returnPressed.disconnect(param)
                except Exception as e:
                    print(str(e))
        init()
        self.ui.entryline.returnPressed.connect(param)

    #Boolean

    def boolcut(self):
        self.boolingcut = True
        self.ui.output.appendPlainText("select a basis and a cutter in [layers] and type a name then press OK")
        self.ui.entryline.setFocus()
        def send_param():
            if self.boolingcut == True:
                try:
                    if self.ui.entryline.text() == '' :
                        name = 'result'
                    else :
                        name = self.ui.entryline.text()
                    shapes = self.ui.treelayers.selectedItems()
                    layer_basis = str(shapes[0].text(0))
                    print(layer_basis)
                    basis = layer_basis.replace('_Shape', '')
                    print(basis)
                    layer_cutter = shapes[1].text(0)
                    cutter = str(layer_cutter).replace('_Shape','')
                    if self.booleancut == False :
                        self.ui.OCCedit.appendPlainText('from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut\nfrom OCC.Core.Graphic3d import Graphic3d_NOM_STEEL\n')
                        self.ui.OCCedit.appendPlainText(Boolean.bool_cut(name, basis, cutter))
                        self.booleancut = True
                    else :
                        self.ui.OCCedit.appendPlainText(Boolean.bool_cut(name, basis,cutter))
                    self.ui.entryline.clear()
                    self.render_file()
                    self.ui.output.appendPlainText('Rendering file...')
                    self.ui.OCCedit.setFocus()
                    self.boolingcut = False
                except Exception as e :
                    self.ui.Consult.appendPlainText(str(e))
        self.ui.entryline.returnPressed.connect(send_param)

    #Transformations

    def translate(self):#TODO ex method, to redefine
        if self.translate == False :
            self.ui.OCCedit.appendPlainText(sc.translate("imp"))
            self.translate = True
        else :
            self.ui.OCCedit.appendPlainText(sc.translate(''))

    #Constrution

    def drawpoint(self):
        self.drawingpoint = True
        self.ui.output.appendPlainText('draw point method : name;x,y,z')
        self.ui.entryline.setFocus()
        def send_param():
            if self.drawingpoint == True :
                try :
                    if self.ui.entryline.text() == '' :
                        name = 'point'
                        settings = '0,0,0'
                    else :
                        pointparam = self.ui.entryline.text().split(';', 1)
                        name = pointparam[0]
                        if name == '':
                            name = 'point'
                        settings = pointparam[1]
                        if settings == '':
                            settings = '0,0,0'
                    if self.point == False :
                        self.ui.OCCedit.appendPlainText('from OCC.Core.gp import gp_Pnt\n')
                        self.ui.OCCedit.appendPlainText(Construction.draw_point(name, settings))
                        self.point = True
                    else :
                        self.ui.OCCedit.appendPlainText(Construction.draw_point(name, settings))
                    self.ui.entryline.clear()
                    self.render_file()
                    self.ui.output.appendPlainText('Rendering file...')
                    self.ui.OCCedit.setFocus()
                    self.drawingpoint = False
                    self.ui.entryline.returnPressed.disconnect(send_param)
                except Exception as e:
                    self.ui.output.appendPlainText(str(e) + '\nTry with the method rule specified above (at list the good number of ";"')
        self.ui.entryline.returnPressed.connect(send_param)

    def drawaxis(self):
        self.drawingaxis = True
        self.ui.treelayers.clearSelection()
        self.ui.output.appendPlainText('Select a reference point in [layers] and type : name;dirx, y, z')
        self.ui.entryline.setFocus()
        def send_param():
            self.ui.output.appendPlainText(self.ui.entryline.text())
            if self.drawingaxis == True:
                try:
                    shapes = self.ui.treelayers.selectedItems()
                    if self.ui.entryline.text() == ''and len(shapes)==0 :
                        name = 'axis'
                        point = 'gp_Pnt(0, 0, 0)'
                        dir = '0,0,10'
                    elif self.ui.entryline.text() == '' and len(shapes) > 0:
                        name = 'axis'
                        layer_point = str(shapes[0].text(0))
                        print(layer_point)
                        point = layer_point.replace('_Point', '')
                        dir = '0,0,10'
                    else:
                        param = self.ui.entryline.text().split(';', 1)
                        name = param[0]
                        if name == '':
                            name = 'axis'
                        layer_point = str(shapes[0].text(0))
                        print(layer_point)
                        point = layer_point.replace('_Point', '')
                        dir = param[1]
                        if dir == '':
                            dir = '0,0,1'
                    if self.axis == False :
                        self.ui.OCCedit.appendPlainText('from OCC.Core.gp import gp_Ax2 , gp_Dir , gp_Pnt\nfrom OCCUtils.Construct import make_edge')
                        self.ui.OCCedit.appendPlainText(Construction.draw_axis(name, point, dir))
                        self.axis = True
                    else :
                        self.ui.OCCedit.appendPlainText(Construction.draw_axis(name, point, dir))
                    self.ui.entryline.clear()
                    self.ui.output.appendPlainText('Rendering file...')
                    self.render_file()
                    self.ui.OCCedit.setFocus()
                    self.drawingaxis = False
                    self.ui.entryline.returnPressed.disconnect(send_param)
                except Exception as e:
                    self.ui.output.appendPlainText(str(e) + '\nTry with the method rule specified above (at list the good number of ";"')
        self.ui.entryline.returnPressed.connect(send_param)

    #Exchange

    def exportstep(self):#TODO ex method, to redefine
        if self.expstep == False :
            self.ui.OCCedit.appendPlainText(sc.export_step("imp"))
            self.expstep = True
        else :
            self.ui.OCCedit.appendPlainText(sc.export_step(''))

class ShapeMakerDialog(QDialog):
    def __init__(self, maker, display):
        super().__init__()
        self.parameters = maker.parameters
        self.display = display
        self.to_pick = None
        self.shape_converter = ShapeConverter()
        self.shapemaker = maker
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.param_labels = {}
        self.param_lineedits = {}
        self.param_buttons = {}
        self.result_text = QtWidgets.QLabel() #QTextEdit()
        self.layout.addWidget(self.result_text)

        # Créer des champs de saisie pour chaque paramètre
        for param_name, param_type in self.parameters.items():
            if "pick" in param_name:
                if "pnt" in param_name:
                    self.display.SetSelectionModeVertex()
                    self.to_pick = "pnt"
                elif "face" in param_name:
                    self.display.SetSelectionModeFace()
                    self.to_pick = "face"
                elif "edge" in param_name:
                    self.display.SetSelectionModeEdge()
                    self.to_pick = "edge"
                self.pick_param_name = param_name
                label = QtWidgets.QLabel(f'{param_name}:')
                line_edit = QtWidgets.QLineEdit()
                button_pick = QtWidgets.QPushButton('pick shape')
                button_pick.clicked.connect(self.get_picked_shape)
                self.param_labels[param_name] = label
                self.param_lineedits[param_name] = line_edit
                self.param_buttons[param_name] = button_pick
                self.layout.addWidget(label)
                self.layout.addWidget(line_edit)
                self.layout.addWidget(button_pick)
            else:
                label = QtWidgets.QLabel(f'{param_name}:')
                line_edit = QtWidgets.QLineEdit()
                self.param_labels[param_name] = label
                self.param_lineedits[param_name] = line_edit
                self.layout.addWidget(label)
                self.layout.addWidget(line_edit)

        submit_button = QPushButton("Create Shape")
        submit_button.clicked.connect(self.create_shape)
        self.layout.addWidget(submit_button)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)  # Ferme la boîte de dialogue avec QDialog.Accepted
        self.layout.addWidget(ok_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Shape Maker')

    def get_picked_shape(self):
        if self.display.GetSelectedShape():
            if self.to_pick == "pnt":
                vertex = self.display.GetSelectedShape()
                gp_pnt = occ.BRep_Tool.Pnt(vertex)
                self.gp_pnt_coord = gp_pnt.Coord()
                self.param_lineedits[self.pick_param_name].setText("gp_Pnt"+str(self.gp_pnt_coord))
            elif self.to_pick == "face":
                face = self.display.GetSelectedShape()
                print(face)
                gp_pnt, _, _ = occ.measure_shape_mass_center_of_gravity(face)
                self.gp_pnt_coord = gp_pnt.Coord()
                self.param_lineedits[self.pick_param_name].setText("gp_Pnt"+str(self.gp_pnt_coord))
            elif self.to_pick == "edge":
                edge = self.display.GetSelectedShape()
                print(edge)
                dumped_shape_name = self.shape_converter.dump_shape(edge)
                self.shapemaker.set_name_dumped_shape(dumped_shape_name)

    def create_shape(self):
        # Récupérer les valeurs des paramètres depuis les QLineEdit
        self.input_line = {}
        for param_name, line_edit in self.param_lineedits.items():
            self.input_line[param_name] = line_edit.text()

        # Afficher le dictionnaire résultant dans le QLabel
        self.result_text.clear()
        self.result_text.setText(str(self.input_line))

    def get_input(self):
        return self.input_line
    
class CreateLayerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Saisie des informations')
        self.setGeometry(300, 300, 300, 200)

        self.layout = QVBoxLayout()

        self.name_label = QtWidgets.QLabel('Nom:')
        self.name_input = QtWidgets.QLineEdit()

        self.color_label = QtWidgets.QLabel('Couleur (0 par défaut):')
        self.color_input = QtWidgets.QLineEdit()
        self.color_input.setText("0")

        self.transparency_label = QtWidgets.QLabel('Transparence (100 par défaut):')
        self.transparency_input = QtWidgets.QLineEdit()
        self.transparency_input.setText("100")

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.color_label)
        self.layout.addWidget(self.color_input)
        self.layout.addWidget(self.transparency_label)
        self.layout.addWidget(self.transparency_input)

        self.submit_button = QPushButton('Valider')
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

        self.submit_button.clicked.connect(self.accept)

    def get_user_input(self):
        result = self.exec_()

        if result == QDialog.Accepted:
            name = self.name_input.text()
            color = self.color_input.text()
            transparency = self.transparency_input.text()
            return name, color, transparency
        else:
            return None, None, None