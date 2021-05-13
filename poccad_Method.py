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

        #ASSOCIATE Functions to display
        self.ui.render_button.clicked.connect(self.render_file)
        self.ui.isoview_button.clicked.connect(lambda : self.setview('Iso'))
        self.ui.topview_button.clicked.connect(lambda : self.setview('Top'))
        self.ui.leftview_button.clicked.connect(lambda: self.setview('Left'))
        self.ui.frontview_button.clicked.connect(lambda: self.setview('Front'))
        self.ui.rightview_button.clicked.connect(lambda: self.setview('Right'))
        self.ui.bottomview_button.clicked.connect(lambda: self.setview('Bottom'))
        self.ui.rearview_button.clicked.connect(lambda: self.setview('Rear'))

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

        self.ui.treeWidget.customContextMenuRequested.connect(self.on_contextmenu_tree)
        self.popTreeMenu = QtWidgets.QMenu(self)
        self.popTreeMenu.addAction("double click to display in 'Consult' Tab")

        self.cwd = os.getcwd()
        self.load_project_structure(self.cwd, self.ui.treeWidget)
        self.ui.treeWidget.itemDoubleClicked.connect(self.show_consult)
        self.ui.treelayers.itemDoubleClicked.connect(self.change_layer_state)

        self.lauching()

    def lauching(self):
        lauchingfile = 'files\\3axis.pocc'
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

    def show_consult(self, item):

        file = item.text(0)
        dir =  ([node.text(0) for node in self.getParents(item)])
        length = len(dir)
        if dir :
            if length == 6 :
                print(str(dir[5])+ '\\' +str(dir[4])+ '\\' +str(dir[3])+ '\\' + str(dir[2]) + '\\'+str(dir[1])+ '\\' + str(dir[0]) + '\\'+ str(file))
                consult_file = str(dir[5])+ '\\' +str(dir[4])+ '\\' +str(dir[3])+ '\\' + str(dir[2]) + '\\'+str(dir[1])+ '\\' + str(dir[0]) + '\\'+ str(file)
            if length == 5 :
                print(str(dir[4])+ '\\' +str(dir[3])+ '\\' + str(dir[2]) + '\\'+str(dir[1])+ '\\' + str(dir[0]) + '\\'+ str(file))
                consult_file = str(dir[4])+ '\\' +str(dir[3])+ '\\' + str(dir[2]) + '\\'+str(dir[1])+ '\\' + str(dir[0]) + '\\'+ str(file)
            if length == 4 :
                print(str(dir[3])+ '\\' + str(dir[2]) + '\\'+str(dir[1])+ '\\' + str(dir[0]) + '\\'+ str(file))
                consult_file = str(dir[3])+ '\\' + str(dir[2]) + '\\'+str(dir[1])+ '\\' + str(dir[0]) + '\\'+ str(file)
            if length == 3 :
                print(str(dir[2])+ '\\' +str(dir[1])+ '\\' +str(dir[0]) + '\\'+ str(file))
                consult_file = str(dir[2])+ '\\' +str(dir[1])+ '\\' +str(dir[0]) + '\\'+ str(file)
            if length == 2 :
                print(str(dir[1])+ '\\' + str(dir[0]) + '\\'+ str(file))
                consult_file = str(dir[1])+ '\\' + str(dir[0]) + '\\'+ str(file)
            if length == 1 :
                print(str(dir[0]) + '\\'+ str(file))
                consult_file = str(dir[0]) +'\\' + str(file)
        else :
            print (str(file))
            consult_file = (str(file))
        self.ui.Consult.clear()
        if 'html' in consult_file:
            html_file = os.path.abspath(consult_file)
            print(html_file)
            webbrowser.open_new_tab(html_file)
        else :
            with open (consult_file , 'r') as cf:
                for line in cf :
                    self.ui.Consult.appendPlainText(line.strip('\n'))

    def getParents(self, item):
        """
        Return a list containing all parent items of this item.
        The list is empty, if the item is a root item.
        """
        parents = []
        current_item = item
        current_parent = current_item.parent()

        # Walk up the tree and collect all parent items of this item
        while not current_parent is None:
            parents.append(current_parent)
            current_item = current_parent
            current_parent = current_item.parent()
        return parents

    def load_project_structure(self, startpath, tree):
        for element in os.listdir(startpath):
            path_info = startpath + "/" + element
            parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
            if os.path.isdir(path_info):
                self.load_project_structure(path_info, parent_itm)
                parent_itm.setIcon(0, QIcon('ui_files\icons\dir.png'))
            else:
                parent_itm.setIcon(0, QIcon('ui_files\icons\\file.png'))

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

    def setview(self, view):
        self.ui.activeview.setPixmap(QPixmap('ui_files\icons\\'+ (view) + '_on.png'))
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
        self.occ_file_path, _ = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, 'Select File to open',"","pocc Files (*.pocc);;All Files (*)")
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
        self.load_project_structure(self.cwd, self.ui.treeWidget)

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
        self.load_project_structure(self.cwd, self.ui.treeWidget)
        
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
        cad_edit = self.ui.OCCedit.toPlainText()
        with open ("cad_file_edit.pocc", "a") as cfe :
            cfe.write("display = self.display\n")
            for line in cad_edit:
                if line.startswith("display = self.") :
                    pass
                elif line.startswith('display.FitAll()'):
                    pass
                else :
                    cfe.writelines(line)
            cfe.write('\ndisplay.FitAll()')
        cfe.close()

        with open ("cad_file_edit.pocc", "r") as cfe :
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
            if 'Shape' in layername :
                displaylayer.setIcon(0, QIcon('ui_files\icons\shape_layer_on.png'))
            elif 'Point' in layername:
                displaylayer.setIcon(0, QIcon('ui_files\icons\construction_layer_on.png'))
            elif 'Axis' in layername:
                displaylayer.setIcon(0, QIcon('ui_files\icons\construction_layer_on.png'))
            elif 'Plane' in layername:
                displaylayer.setIcon(0, QIcon('ui_files\icons\construction_layer_on.png'))
            elif 'Curve' in layername:
                displaylayer.setIcon(0, QIcon('ui_files\icons\construction_layer_on.png'))
        if state == 'off':
            if 'Shape' in layername :
                displaylayer.setIcon(0, QIcon('ui_files\icons\shape_layer_off.png'))
            elif 'Point' in layername:
                displaylayer.setIcon(0, QIcon('ui_files\icons\construction_layer_off.png'))
            elif 'Axis' in layername:
                displaylayer.setIcon(0, QIcon('ui_files\icons\construction_layer_off.png'))
            elif 'Plane' in layername:
                displaylayer.setIcon(0, QIcon('ui_files\icons\construction_layer_off.png'))
            elif 'Curve' in layername:
                displaylayer.setIcon(0, QIcon('ui_files\icons\construction_layer_off.png'))

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


    #PythonOCC functions :
    #Shape

    def makebox(self):

        def init():
            self.makingbox = True
            self.size_on = False
            self.name_on = False
            self.name = 'box'
            self.point = 'gp_Pnt()'
            self.settings = '10,10,10'
            self.ui.treelayers.clearSelection()
            self.ui.output.appendHtml('Press Enter or specify : <u>N</u>ame, <u>P</u>oint, <u>S</u>ize (width,length,heigth)')
            self.ui.entryline.setFocus()

        def param():
            try :
                if self.ui.entryline.text() == '':
                    print('send')
                    send_param()
                elif self.ui.entryline.text() == 's':
                    print('s')
                    self.ui.output.appendHtml('Specify size')
                    self.size_on = True
                    self.ui.entryline.selectAll()
                elif self.ui.entryline.text() == 'n':
                    print('n')
                    self.ui.output.appendHtml('Specify name')
                    self.name_on = True
                    self.ui.entryline.selectAll()
                else :
                    if self.size_on == True:
                        print('s true')
                        self.settings = self.ui.entryline.text()
                        self.size_on = False
                        self.ui.output.appendHtml(
                            '<u>N</u>ame : ' + str(self.name) + ' , <u>P</u>oint : ' + str(self.point) + ' , <u>S</u>ize : ' + str(
                                self.settings))
                        self.ui.entryline.selectAll()
                    if self.name_on == True:
                        print('n true')
                        self.name = self.ui.entryline.text()
                        self.name_on = False
                        self.ui.output.appendHtml(
                            '<u>N</u>ame : ' + str(self.name) + ' , <u>P</u>oint : ' + str(self.point) + ' , <u>S</u>ize : ' + str(
                                self.settings))
                        self.ui.entryline.selectAll()
            except Exception as e:
                self.ui.output.appendPlainText(str(e))

        def send_param():
            if self.makingbox == True:
                try :
                    if self.box == False:
                        self.ui.OCCedit.appendPlainText(
                            'from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox\nfrom OCC.Core.gp import gp_Pnt')
                        self.ui.OCCedit.appendPlainText(Shape.make_box(self.name, self.point, self.settings))
                        self.box = True
                    else:
                        self.ui.OCCedit.appendPlainText(Shape.make_box(self.name, self.point, self.settings))
                    self.ui.entryline.clear()
                    self.render_file()
                    self.ui.output.appendPlainText('Rendering file...')
                    self.ui.OCCedit.setFocus()
                    self.makingbox = False
                    self.ui.entryline.returnPressed.disconnect(param)
                except Exception as e:
                    print(str(e))
        init()
        self.ui.entryline.returnPressed.connect(param)

    def makecylinder(self):
        self.makingcylinder = True
        self.ui.treelayers.clearSelection()
        self.ui.output.appendPlainText('Select a reference axis in [layers] and type : name;radius,length')
        self.ui.entryline.setFocus()
        def send_param():
            self.ui.output.appendPlainText(self.ui.entryline.text())
            print('cylinder function')
            if self.makingcylinder == True:
                try:
                    shapes = self.ui.treelayers.selectedItems()
                    if self.ui.entryline.text() == ''and len(shapes)==0 :
                        name = 'cylinder'
                        axis = 'gp_Ax2(gp_Pnt(0, 0, 5), gp_Dir(0, 0, 1))'
                        settings = '10,10'
                    elif self.ui.entryline.text() == '' and len(shapes) > 0:
                        name = 'cylinder'
                        layer_axis = str(shapes[0].text(0))
                        print(layer_axis)
                        axis = layer_axis.replace('_Axis', '')
                        settings = '10,10'
                    else:
                        cylinderparam = self.ui.entryline.text().split(';', 1)
                        name = cylinderparam[0]
                        if name == '':
                            name = 'cylinder'
                        layer_axis = str(shapes[0].text(0))
                        print(layer_axis)
                        axis = layer_axis.replace('_Axis', '')
                        settings = cylinderparam[1]
                        if settings == '':
                            settings = '10,10'
                    if self.cylinder == False:
                        self.ui.OCCedit.appendPlainText('from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder\nfrom OCC.Core.gp import gp_Ax2 , gp_Dir , gp_Pnt\n')
                        self.ui.OCCedit.appendPlainText(Shape.make_cylinder(name, axis, settings))
                        self.cylinder = True
                    else:
                        self.ui.OCCedit.appendPlainText(Shape.make_cylinder(name, axis, settings))
                    self.makingcylinder = False
                    print(self.makingcylinder)
                    self.ui.entryline.clear()
                    self.render_file()
                    self.ui.output.appendPlainText('Rendering file...')
                    self.ui.OCCedit.setFocus()
                    self.ui.entryline.returnPressed.disconnect(send_param)
                except Exception as e:
                    self.ui.output.appendPlainText(
                        str(e) + '\nTry with the method rule specified above (at list the good number of ";"')

        if self.makingcylinder == True :
            self.ui.entryline.returnPressed.connect(send_param)
        else :
            print('this is the end')
            return None

    def makesphere(self):#TODO ex method, to redefine
        if self.sphere == False :
            self.ui.OCCedit.appendPlainText(sc.make_sphere("imp"))
            self.sphere = True
        else :
            self.ui.OCCedit.appendPlainText(sc.make_sphere(''))

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

