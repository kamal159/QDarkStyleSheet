# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dw_displays.ui'
#
# Created: Thu Oct 25 01:26:33 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(703, 632)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtGui.QTextBrowser(self.dockWidgetContents)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 1, 1, 1)
        self.label_77 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.gridLayout.addWidget(self.label_77, 0, 1, 1, 1)
        self.label_78 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.gridLayout.addWidget(self.label_78, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_79 = QtGui.QLabel(self.dockWidgetContents)
        self.label_79.setEnabled(False)
        self.label_79.setObjectName("label_79")
        self.gridLayout.addWidget(self.label_79, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.dockWidgetContents)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.textBrowserDis = QtGui.QTextBrowser(self.dockWidgetContents)
        self.textBrowserDis.setEnabled(False)
        self.textBrowserDis.setObjectName("textBrowserDis")
        self.gridLayout.addWidget(self.textBrowserDis, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.dockWidgetContents)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(self.dockWidgetContents)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 3, 1, 1, 1)
        self.graphicsViewDis = QtGui.QGraphicsView(self.dockWidgetContents)
        self.graphicsViewDis.setEnabled(False)
        self.graphicsViewDis.setObjectName("graphicsViewDis")
        self.gridLayout.addWidget(self.graphicsViewDis, 3, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.dockWidgetContents)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.calendarWidget = QtGui.QCalendarWidget(self.dockWidgetContents)
        self.calendarWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.calendarWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 4, 1, 1, 1)
        self.calendarWidgetDis = QtGui.QCalendarWidget(self.dockWidgetContents)
        self.calendarWidgetDis.setEnabled(False)
        self.calendarWidgetDis.setObjectName("calendarWidgetDis")
        self.gridLayout.addWidget(self.calendarWidgetDis, 4, 2, 1, 1)
        self.lcdNumberDis = QtGui.QLCDNumber(self.dockWidgetContents)
        self.lcdNumberDis.setEnabled(False)
        self.lcdNumberDis.setObjectName("lcdNumberDis")
        self.gridLayout.addWidget(self.lcdNumberDis, 5, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.dockWidgetContents)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.dockWidgetContents)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 0))
        self.lcdNumber.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 5, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.dockWidgetContents)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.dockWidgetContents)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 6, 1, 1, 1)
        self.progressBarDis = QtGui.QProgressBar(self.dockWidgetContents)
        self.progressBarDis.setEnabled(False)
        self.progressBarDis.setProperty("value", 24)
        self.progressBarDis.setObjectName("progressBarDis")
        self.gridLayout.addWidget(self.progressBarDis, 6, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.dockWidgetContents)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.lineH = QtGui.QFrame(self.dockWidgetContents)
        self.lineH.setMinimumSize(QtCore.QSize(0, 0))
        self.lineH.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineH.setFrameShape(QtGui.QFrame.HLine)
        self.lineH.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineH.setObjectName("lineH")
        self.gridLayout.addWidget(self.lineH, 7, 1, 1, 1)
        self.lineHDis = QtGui.QFrame(self.dockWidgetContents)
        self.lineHDis.setEnabled(False)
        self.lineHDis.setFrameShape(QtGui.QFrame.HLine)
        self.lineHDis.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineHDis.setObjectName("lineHDis")
        self.gridLayout.addWidget(self.lineHDis, 7, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.dockWidgetContents)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.lineV = QtGui.QFrame(self.dockWidgetContents)
        self.lineV.setMinimumSize(QtCore.QSize(0, 50))
        self.lineV.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineV.setFrameShape(QtGui.QFrame.VLine)
        self.lineV.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineV.setObjectName("lineV")
        self.gridLayout.addWidget(self.lineV, 8, 1, 1, 1)
        self.lineVDis = QtGui.QFrame(self.dockWidgetContents)
        self.lineVDis.setEnabled(False)
        self.lineVDis.setMinimumSize(QtCore.QSize(0, 50))
        self.lineVDis.setFrameShape(QtGui.QFrame.VLine)
        self.lineVDis.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineVDis.setObjectName("lineVDis")
        self.gridLayout.addWidget(self.lineVDis, 8, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 1)
        self.label_37 = QtGui.QLabel(self.dockWidgetContents)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 10, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QObject.connect(self.calendarWidget, QtCore.SIGNAL("currentPageChanged(int,int)"), self.calendarWidgetDis.setCurrentPage)
        QtCore.QObject.connect(self.calendarWidget, QtCore.SIGNAL("clicked(QDate)"), self.calendarWidgetDis.setSelectedDate)
        QtCore.QObject.connect(self.progressBar, QtCore.SIGNAL("valueChanged(int)"), self.progressBarDis.setValue)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QtGui.QApplication.translate("DockWidget", "Displays", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("DockWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Testing</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_77.setText(QtGui.QApplication.translate("DockWidget", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_78.setText(QtGui.QApplication.translate("DockWidget", "Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DockWidget", "Label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_79.setText(QtGui.QApplication.translate("DockWidget", "Testing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DockWidget", "TextBrowser", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowserDis.setHtml(QtGui.QApplication.translate("DockWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Testing</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DockWidget", "GraphicsView", None, QtGui.QApplication.UnicodeUTF8))
        self.graphicsView.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.graphicsView.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.graphicsView.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DockWidget", "CalendarWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.calendarWidget.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.calendarWidget.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.calendarWidget.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DockWidget", "LCDNumber", None, QtGui.QApplication.UnicodeUTF8))
        self.lcdNumber.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.lcdNumber.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.lcdNumber.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DockWidget", "ProgressBar", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DockWidget", "Line - H", None, QtGui.QApplication.UnicodeUTF8))
        self.lineH.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.lineH.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.lineH.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("DockWidget", "Line - V", None, QtGui.QApplication.UnicodeUTF8))
        self.lineV.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.lineV.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.lineV.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("DockWidget", "Inside DockWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DockWidget", "Testing", None, QtGui.QApplication.UnicodeUTF8))

