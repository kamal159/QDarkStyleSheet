# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw_menus.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 307)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_71 = QtWidgets.QLabel(self.centralwidget)
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_71")
        self.verticalLayout_4.addWidget(self.label_71)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 28))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuMenuSub = QtWidgets.QMenu(self.menuMenu)
        self.menuMenuSub.setObjectName("menuMenuSub")
        self.menuMenuDelayed = QtWidgets.QMenu(self.menubar)
        self.menuMenuDelayed.setObjectName("menuMenuDelayed")
        self.menuMenuSubDelayed = QtWidgets.QMenu(self.menuMenuDelayed)
        self.menuMenuSubDelayed.setObjectName("menuMenuSubDelayed")
        self.menuMenuCheckale = QtWidgets.QMenu(self.menubar)
        self.menuMenuCheckale.setObjectName("menuMenuCheckale")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBarDelayed = QtWidgets.QToolBar(MainWindow)
        self.toolBarDelayed.setObjectName("toolBarDelayed")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarDelayed)
        self.toolBarCheckable = QtWidgets.QToolBar(MainWindow)
        self.toolBarCheckable.setObjectName("toolBarCheckable")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBarCheckable)
        self.actionActionA = QtWidgets.QAction(MainWindow)
        self.actionActionA.setObjectName("actionActionA")
        self.actionActionSubA = QtWidgets.QAction(MainWindow)
        self.actionActionSubA.setObjectName("actionActionSubA")
        self.actionActionSubB = QtWidgets.QAction(MainWindow)
        self.actionActionSubB.setObjectName("actionActionSubB")
        self.actionActionDelayedA = QtWidgets.QAction(MainWindow)
        self.actionActionDelayedA.setObjectName("actionActionDelayedA")
        self.actionActionDelayedSubA = QtWidgets.QAction(MainWindow)
        self.actionActionDelayedSubA.setObjectName("actionActionDelayedSubA")
        self.actionActionCheckableA = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableA.setCheckable(True)
        self.actionActionCheckableA.setObjectName("actionActionCheckableA")
        self.actionActionCheckableSubAChecked = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableSubAChecked.setCheckable(True)
        self.actionActionCheckableSubAChecked.setChecked(True)
        self.actionActionCheckableSubAChecked.setObjectName("actionActionCheckableSubAChecked")
        self.actionActionCheckableSubAUnchecked = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableSubAUnchecked.setCheckable(True)
        self.actionActionCheckableSubAUnchecked.setObjectName("actionActionCheckableSubAUnchecked")
        self.menuMenuSub.addAction(self.actionActionSubA)
        self.menuMenuSub.addAction(self.actionActionSubB)
        self.menuMenu.addAction(self.actionActionA)
        self.menuMenu.addAction(self.menuMenuSub.menuAction())
        self.menuMenuSubDelayed.addAction(self.actionActionDelayedSubA)
        self.menuMenuDelayed.addAction(self.actionActionDelayedA)
        self.menuMenuDelayed.addAction(self.menuMenuSubDelayed.menuAction())
        self.menuMenuCheckale.addAction(self.actionActionCheckableA)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuMenuDelayed.menuAction())
        self.menubar.addAction(self.menuMenuCheckale.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionActionA)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionActionSubA)
        self.toolBar.addAction(self.actionActionSubB)
        self.toolBarDelayed.addAction(self.actionActionDelayedA)
        self.toolBarDelayed.addSeparator()
        self.toolBarDelayed.addAction(self.actionActionDelayedSubA)
        self.toolBarCheckable.addAction(self.actionActionCheckableA)
        self.toolBarCheckable.addSeparator()
        self.toolBarCheckable.addAction(self.actionActionCheckableSubAChecked)
        self.toolBarCheckable.addAction(self.actionActionCheckableSubAUnchecked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_71.setText(_translate("MainWindow", "Inside Central Widget"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><a href=\"https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues/112\"><span style=\" text-decoration: underline; color:#0000ff;\">Hyperlink Example</span></a></p><p align=\"center\"><a href=\"https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues/112\"><span style=\" text-decoration: underline; color:#aa0000;\">CSS for the documents (RichText) </span></a></p><p align=\"center\"><a href=\"https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues/112\"><span style=\" text-decoration: underline; color:#aa0000;\">is not the same as the application.</span></a></p><p align=\"center\"><a href=\"https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues/112\"><span style=\" text-decoration: underline; color:#aa0000;\">We cannot change the internal </span></a></p><p align=\"center\"><a href=\"https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues/112\"><span style=\" text-decoration: underline; color:#aa0000;\">content CSS, e.g., hyperlinks.</span></a></p><p align=\"center\"><a href=\"https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues/112\"><span style=\" text-decoration: underline; color:#4d545b;\">See issue #112.</span></a></p></body></html>"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuMenuSub.setTitle(_translate("MainWindow", "Menu Sub"))
        self.menuMenuDelayed.setTitle(_translate("MainWindow", "Menu Delayed"))
        self.menuMenuSubDelayed.setTitle(_translate("MainWindow", "Menu Sub Delayed"))
        self.menuMenuCheckale.setTitle(_translate("MainWindow", "Menu Checkable"))
        self.menuAbout.setTitle(_translate("MainWindow", "About QDarkStyle"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Tool bar actions"))
        self.toolBarDelayed.setWindowTitle(_translate("MainWindow", "Tool bar actions delayed"))
        self.toolBarCheckable.setWindowTitle(_translate("MainWindow", "Tool bar action checkable"))
        self.actionActionA.setText(_translate("MainWindow", "Action A"))
        self.actionActionSubA.setText(_translate("MainWindow", "Action A Sub"))
        self.actionActionSubA.setToolTip(_translate("MainWindow", "Action A Sub"))
        self.actionActionSubB.setText(_translate("MainWindow", "Action B Sub"))
        self.actionActionDelayedA.setText(_translate("MainWindow", "Action Delayed A"))
        self.actionActionDelayedA.setToolTip(_translate("MainWindow", "Action Delayed A"))
        self.actionActionDelayedSubA.setText(_translate("MainWindow", "Action Delayed Sub A"))
        self.actionActionDelayedSubA.setToolTip(_translate("MainWindow", "Action Delayed Sub A"))
        self.actionActionCheckableA.setText(_translate("MainWindow", "Action Checkable A"))
        self.actionActionCheckableA.setToolTip(_translate("MainWindow", "Action Checkable A"))
        self.actionActionCheckableSubAChecked.setText(_translate("MainWindow", "Action Checkable Sub A Checked"))
        self.actionActionCheckableSubAChecked.setToolTip(_translate("MainWindow", "Action Checkable Sub A Checked"))
        self.actionActionCheckableSubAUnchecked.setText(_translate("MainWindow", "Action Checkable Sub A Unchecked"))
        self.actionActionCheckableSubAUnchecked.setToolTip(_translate("MainWindow", "Action Checkable Sub A Unchecked"))

