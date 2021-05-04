# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poccad.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_poccad(object):
    def setupUi(self, poccad):
        poccad.setObjectName("poccad")
        poccad.resize(1061, 863)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_files/icons/poccad.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        poccad.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(poccad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.splitter_3)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.splitter_2 = QtWidgets.QSplitter(self.horizontalLayoutWidget_4)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gridLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.output = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 65, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.output.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.output.setFont(font)
        self.output.setStyleSheet("background-color:rgb(65, 65, 65);\n"
"font: 9pt \"Consolas\";")
        self.output.setPlainText("")
        self.output.setOverwriteMode(False)
        self.output.setCursorWidth(0)
        self.output.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.output.setObjectName("output")
        self.verticalLayout_2.addWidget(self.output)
        self.entryline = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.entryline.setObjectName("entryline")
        self.verticalLayout_2.addWidget(self.entryline)
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.activeview = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activeview.sizePolicy().hasHeightForWidth())
        self.activeview.setSizePolicy(sizePolicy)
        self.activeview.setText("")
        self.activeview.setPixmap(QtGui.QPixmap("ui_files/icons/Iso_on.png"))
        self.activeview.setScaledContents(True)
        self.activeview.setObjectName("activeview")
        self.gridLayout_2.addWidget(self.activeview, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.isoview_button = QtWidgets.QPushButton(self.layoutWidget)
        self.isoview_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui_files/icons/Iso_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.isoview_button.setIcon(icon1)
        self.isoview_button.setObjectName("isoview_button")
        self.horizontalLayout_3.addWidget(self.isoview_button)
        self.topview_button = QtWidgets.QPushButton(self.layoutWidget)
        self.topview_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui_files/icons/Top_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.topview_button.setIcon(icon2)
        self.topview_button.setObjectName("topview_button")
        self.horizontalLayout_3.addWidget(self.topview_button)
        self.frontview_button = QtWidgets.QPushButton(self.layoutWidget)
        self.frontview_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui_files/icons/Front_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frontview_button.setIcon(icon3)
        self.frontview_button.setObjectName("frontview_button")
        self.horizontalLayout_3.addWidget(self.frontview_button)
        self.leftview_button = QtWidgets.QPushButton(self.layoutWidget)
        self.leftview_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui_files/icons/Left_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftview_button.setIcon(icon4)
        self.leftview_button.setObjectName("leftview_button")
        self.horizontalLayout_3.addWidget(self.leftview_button)
        self.bottomview_button = QtWidgets.QPushButton(self.layoutWidget)
        self.bottomview_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui_files/icons/Bottom_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bottomview_button.setIcon(icon5)
        self.bottomview_button.setObjectName("bottomview_button")
        self.horizontalLayout_3.addWidget(self.bottomview_button)
        self.rightview_button = QtWidgets.QPushButton(self.layoutWidget)
        self.rightview_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui_files/icons/Right_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightview_button.setIcon(icon6)
        self.rightview_button.setObjectName("rightview_button")
        self.horizontalLayout_3.addWidget(self.rightview_button)
        self.rearview_button = QtWidgets.QPushButton(self.layoutWidget)
        self.rearview_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui_files/icons/Rear_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rearview_button.setIcon(icon7)
        self.rearview_button.setObjectName("rearview_button")
        self.horizontalLayout_3.addWidget(self.rearview_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8.addWidget(self.splitter_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.splitter_3)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.splitter = QtWidgets.QSplitter(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setIndentation(15)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.horizontalLayout.addWidget(self.treeWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget_2)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy)
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.OCCedit = CodeEditor(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OCCedit.sizePolicy().hasHeightForWidth())
        self.OCCedit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.OCCedit.setFont(font)
        self.OCCedit.setTabChangesFocus(False)
        self.OCCedit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.OCCedit.setTabStopWidth(20)
        self.OCCedit.setObjectName("OCCedit")
        self.horizontalLayout_4.addWidget(self.OCCedit)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_4.sizePolicy().hasHeightForWidth())
        self.tab_4.setSizePolicy(sizePolicy)
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Consult = CodeEditor(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Consult.sizePolicy().hasHeightForWidth())
        self.Consult.setSizePolicy(sizePolicy)
        self.Consult.setStyleSheet("background-color:rgb(226, 226, 226)")
        self.Consult.setTabChangesFocus(False)
        self.Consult.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.Consult.setReadOnly(True)
        self.Consult.setTabStopWidth(20)
        self.Consult.setObjectName("Consult")
        self.horizontalLayout_2.addWidget(self.Consult)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.treelayers = QtWidgets.QTreeWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treelayers.sizePolicy().hasHeightForWidth())
        self.treelayers.setSizePolicy(sizePolicy)
        self.treelayers.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.treelayers.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.treelayers.setHeaderHidden(True)
        self.treelayers.setObjectName("treelayers")
        self.treelayers.headerItem().setText(0, "1")
        self.horizontalLayout_5.addWidget(self.treelayers)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout_6.addWidget(self.tabWidget)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.OCClayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.OCClayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.OCClayout.setContentsMargins(0, 0, 0, 0)
        self.OCClayout.setObjectName("OCClayout")
        self.render_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.render_button.sizePolicy().hasHeightForWidth())
        self.render_button.setSizePolicy(sizePolicy)
        self.render_button.setObjectName("render_button")
        self.OCClayout.addWidget(self.render_button)
        self.horizontalLayout_7.addWidget(self.splitter)
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
        poccad.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(poccad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuShape = QtWidgets.QMenu(self.menubar)
        self.menuShape.setObjectName("menuShape")
        self.menuBoolean = QtWidgets.QMenu(self.menubar)
        self.menuBoolean.setObjectName("menuBoolean")
        self.menuTransform = QtWidgets.QMenu(self.menubar)
        self.menuTransform.setObjectName("menuTransform")
        self.menuConstruction = QtWidgets.QMenu(self.menubar)
        self.menuConstruction.setObjectName("menuConstruction")
        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        poccad.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(poccad)
        self.statusbar.setObjectName("statusbar")
        poccad.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(poccad)
        self.actionQuit.setObjectName("actionQuit")
        self.actionBox = QtWidgets.QAction(poccad)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.actionBox.setFont(font)
        self.actionBox.setObjectName("actionBox")
        self.actionOpen = QtWidgets.QAction(poccad)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(poccad)
        self.actionSave.setObjectName("actionSave")
        self.actionSphere = QtWidgets.QAction(poccad)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(False)
        self.actionSphere.setFont(font)
        self.actionSphere.setObjectName("actionSphere")
        self.actionRead_Step = QtWidgets.QAction(poccad)
        self.actionRead_Step.setObjectName("actionRead_Step")
        self.actionCut = QtWidgets.QAction(poccad)
        self.actionCut.setObjectName("actionCut")
        self.actionPoint = QtWidgets.QAction(poccad)
        self.actionPoint.setObjectName("actionPoint")
        self.actionTranslate = QtWidgets.QAction(poccad)
        self.actionTranslate.setObjectName("actionTranslate")
        self.actionExportstep = QtWidgets.QAction(poccad)
        self.actionExportstep.setObjectName("actionExportstep")
        self.actionNew = QtWidgets.QAction(poccad)
        self.actionNew.setObjectName("actionNew")
        self.actionAbout = QtWidgets.QAction(poccad)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave_as = QtWidgets.QAction(poccad)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExport = QtWidgets.QAction(poccad)
        self.actionExport.setObjectName("actionExport")
        self.actionCylinder = QtWidgets.QAction(poccad)
        self.actionCylinder.setObjectName("actionCylinder")
        self.actionAxis = QtWidgets.QAction(poccad)
        self.actionAxis.setObjectName("actionAxis")
        self.actionUser_Guide = QtWidgets.QAction(poccad)
        self.actionUser_Guide.setObjectName("actionUser_Guide")
        self.menuMenu.addAction(self.actionNew)
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionSave_as)
        self.menuMenu.addAction(self.actionExport)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menuShape.addAction(self.actionBox)
        self.menuShape.addAction(self.actionCylinder)
        self.menuShape.addAction(self.actionSphere)
        self.menuShape.addAction(self.actionRead_Step)
        self.menuBoolean.addAction(self.actionCut)
        self.menuTransform.addAction(self.actionTranslate)
        self.menuConstruction.addAction(self.actionPoint)
        self.menuConstruction.addAction(self.actionAxis)
        self.menuExport.addAction(self.actionExportstep)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuShape.menuAction())
        self.menubar.addAction(self.menuConstruction.menuAction())
        self.menubar.addAction(self.menuBoolean.menuAction())
        self.menubar.addAction(self.menuTransform.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(poccad)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(poccad)

    def retranslateUi(self, poccad):
        _translate = QtCore.QCoreApplication.translate
        poccad.setWindowTitle(_translate("poccad", "poccad"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("poccad", "Edit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("poccad", "Consult"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("poccad", "Layers"))
        self.render_button.setText(_translate("poccad", "Render [F5]"))
        self.render_button.setShortcut(_translate("poccad", "F5"))
        self.menuMenu.setTitle(_translate("poccad", "Menu"))
        self.menuShape.setTitle(_translate("poccad", "Shape"))
        self.menuBoolean.setTitle(_translate("poccad", "Boolean"))
        self.menuTransform.setTitle(_translate("poccad", "Transform"))
        self.menuConstruction.setTitle(_translate("poccad", "Construction"))
        self.menuExport.setTitle(_translate("poccad", "Export"))
        self.menuHelp.setTitle(_translate("poccad", "Help"))
        self.actionQuit.setText(_translate("poccad", "Quit"))
        self.actionQuit.setShortcut(_translate("poccad", "Ctrl+Q"))
        self.actionBox.setText(_translate("poccad", "Box"))
        self.actionOpen.setText(_translate("poccad", "Open"))
        self.actionOpen.setShortcut(_translate("poccad", "Ctrl+O"))
        self.actionSave.setText(_translate("poccad", "Save"))
        self.actionSave.setShortcut(_translate("poccad", "Ctrl+S"))
        self.actionSphere.setText(_translate("poccad", "Sphere"))
        self.actionRead_Step.setText(_translate("poccad", "Read Step"))
        self.actionCut.setText(_translate("poccad", "Cut"))
        self.actionPoint.setText(_translate("poccad", "Point"))
        self.actionTranslate.setText(_translate("poccad", "Translate"))
        self.actionExportstep.setText(_translate("poccad", "Export step"))
        self.actionNew.setText(_translate("poccad", "New"))
        self.actionNew.setShortcut(_translate("poccad", "Ctrl+N"))
        self.actionAbout.setText(_translate("poccad", "About"))
        self.actionSave_as.setText(_translate("poccad", "Save as"))
        self.actionSave_as.setShortcut(_translate("poccad", "Ctrl+Shift+S"))
        self.actionExport.setText(_translate("poccad", "Export .py"))
        self.actionExport.setShortcut(_translate("poccad", "Ctrl+E"))
        self.actionCylinder.setText(_translate("poccad", "Cylinder"))
        self.actionAxis.setText(_translate("poccad", "Axis"))
        self.actionUser_Guide.setText(_translate("poccad", "User Guide"))
from lib.codeeditor import CodeEditor
