import os
import os.path
import sys
import time
import PyQt5
from qtpy import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QInputDialog, QFileDialog

from OCC.Display.backend import load_backend
load_backend('qt-pyqt5')

import OCC.Display.qtDisplay as qtDisplay

import lib.occImports as i
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
        self.ui.open_button.clicked.connect(self.open_file)
        self.ui.save_button.clicked.connect(self.save_file)
        self.ui.render_button.clicked.connect(self.render_file)
        self.ui.isoview_button.clicked.connect(lambda : self.setview('Iso'))
        self.ui.topview_button.clicked.connect(lambda : self.setview('Top'))
        self.ui.leftview_button.clicked.connect(lambda: self.setview('Left'))
        self.ui.frontview_button.clicked.connect(lambda: self.setview('Front'))
        self.ui.rightview_button.clicked.connect(lambda: self.setview('Right'))
        self.ui.bottomview_button.clicked.connect(lambda: self.setview('Bottom'))
        self.ui.rearview_button.clicked.connect(lambda: self.setview('Rear'))

        self.ui.actionQuit.triggered.connect(self.quit)

        self.changeviewval = 0
        self.render = False

        self.ui.OCCedit.setPlainText('#Auto append for render :\n#import occImports as i\n#display = self.display\n#display.FitAll()' )

    def setview(self, view):
        self.ui.activeview_button.setIcon(QtGui.QIcon('ui_files\icons\\'+ (view) + '_on.png'))
        dispview = 'self.display.View_' + (view)+'()'
        exec (dispview)
        self.display.FitAll()

    def open_file(self):
        print('open')
        self.occ_file_path, _ = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, 'Select File')
        print(self.occ_file_path)
        self.ui.OCCedit.clear()
        with open (self.occ_file_path, "r") as opened_file:
            for line in opened_file:
                if line == "\n" :
                    pass
                else :
                    self.ui.OCCedit.appendPlainText(line.strip('\n'))
        
    def save_file(self):
        print('save')
        text, ok = QInputDialog.getText(self, 'Save file', 'Name of the file?')
        if ok:
            saved_file = (str(text)+'.occ')
            cad_edit = self.ui.OCCedit.toPlainText()
            with open (saved_file, "a") as cfe :
                for line in cad_edit:
                    if line.startswith("display = self.display"):
                        pass
                    if line.startswith('import lib.occImports as i'):
                        pass
                    if line.startswith('display.FitAll()'):
                        pass
                    else:
                        cfe.writelines(line)
        else :
            pass
        
    def render_file(self):
        print('render')
        if os.path.isfile("cad_file_edit.occ"):
            os.remove("cad_file_edit.occ")
        self.display.EraseAll()
        cad_edit = self.ui.OCCedit.toPlainText()
        with open ("cad_file_edit.occ", "a") as cfe :
            cfe.write("import lib.occImports as i\n")
            cfe.write("display = self.display\n")
            for line in cad_edit:
                if line.startswith("display = self.") :
                    pass
                if line.startswith('import lib.occImports as i'):
                    pass
                if line.startswith('display.FitAll()'):
                    pass
                else :
                    cfe.writelines(line)
            cfe.write('\ndisplay.FitAll()')
        exec(open("cad_file_edit.occ").read())
        self.render = True

    def quit(self):
        os.remove("cad_file_edit.occ")
        sys.exit()
