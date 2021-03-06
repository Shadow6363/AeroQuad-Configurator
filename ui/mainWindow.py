# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Sat Dec 15 02:24:37 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class ReturningComboBox(QtGui.QComboBox):
    def __init__(self, parent=None):
        super(ReturningComboBox, self).__init__(parent)

        self.return_handler = None

    def keyPressEvent(self, event):
        super(ReturningComboBox, self).keyPressEvent(event)

        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.return_handler()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/AQ/AeroQuadIcon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.status = QtGui.QLabel(self.centralwidget)
        self.status.setMinimumSize(QtCore.QSize(200, 0))
        self.status.setObjectName(_fromUtf8("status"))
        self.horizontalLayout.addWidget(self.status)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comPort = ReturningComboBox(self.centralwidget)
        self.comPort.setMinimumSize(QtCore.QSize(0, 0))
        self.comPort.setEditable(True)
        self.comPort.setObjectName(_fromUtf8("comPort"))
        self.horizontalLayout.addWidget(self.comPort)
        self.baudRate = QtGui.QComboBox(self.centralwidget)
        self.baudRate.setMinimumSize(QtCore.QSize(0, 0))
        self.baudRate.setEditable(True)
        self.baudRate.setObjectName(_fromUtf8("baudRate"))
        self.horizontalLayout.addWidget(self.baudRate)
        self.buttonConnect = QtGui.QPushButton(self.centralwidget)
        self.buttonConnect.setObjectName(_fromUtf8("buttonConnect"))
        self.horizontalLayout.addWidget(self.buttonConnect)
        self.buttonDisconnect = QtGui.QPushButton(self.centralwidget)
        self.buttonDisconnect.setObjectName(_fromUtf8("buttonDisconnect"))
        self.horizontalLayout.addWidget(self.buttonDisconnect)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.subPanel = QtGui.QStackedWidget(self.centralwidget)
        self.subPanel.setObjectName(_fromUtf8("subPanel"))
        self.gridLayout.addWidget(self.subPanel, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menuFile)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuCalibrations = QtGui.QMenu(self.menuFile)
        self.menuCalibrations.setObjectName(_fromUtf8("menuCalibrations"))
        self.menuPreferences = QtGui.QMenu(self.menuFile)
        self.menuPreferences.setObjectName(_fromUtf8("menuPreferences"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionOpenSettings = QtGui.QAction(MainWindow)
        self.actionOpenSettings.setObjectName(_fromUtf8("actionOpenSettings"))
        self.actionSaveSettings = QtGui.QAction(MainWindow)
        self.actionSaveSettings.setObjectName(_fromUtf8("actionSaveSettings"))
        self.actionOpenCalibrations = QtGui.QAction(MainWindow)
        self.actionOpenCalibrations.setObjectName(_fromUtf8("actionOpenCalibrations"))
        self.actionSaveCalibrations = QtGui.QAction(MainWindow)
        self.actionSaveCalibrations.setObjectName(_fromUtf8("actionSaveCalibrations"))
        self.actionBootUpDelay = QtGui.QAction(MainWindow)
        self.actionBootUpDelay.setObjectName(_fromUtf8("actionBootUpDelay"))
        self.actionCommTimeout = QtGui.QAction(MainWindow)
        self.actionCommTimeout.setObjectName(_fromUtf8("actionCommTimeout"))
        self.menuSettings.addAction(self.actionOpenSettings)
        self.menuSettings.addAction(self.actionSaveSettings)
        self.menuCalibrations.addAction(self.actionOpenCalibrations)
        self.menuCalibrations.addAction(self.actionSaveCalibrations)
        self.menuPreferences.addAction(self.actionBootUpDelay)
        self.menuPreferences.addAction(self.actionCommTimeout)
        self.menuFile.addAction(self.menuSettings.menuAction())
        self.menuFile.addAction(self.menuCalibrations.menuAction())
        self.menuFile.addAction(self.menuPreferences.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "AeroQuad Configurator", None, QtGui.QApplication.UnicodeUTF8))
        self.status.setText(QtGui.QApplication.translate("MainWindow", "Not connected to AeroQuad", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonConnect.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDisconnect.setText(QtGui.QApplication.translate("MainWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCalibrations.setTitle(QtGui.QApplication.translate("MainWindow", "Calibrations", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPreferences.setTitle(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenSettings.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveSettings.setText(QtGui.QApplication.translate("MainWindow", "Save...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenCalibrations.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveCalibrations.setText(QtGui.QApplication.translate("MainWindow", "Save....", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBootUpDelay.setText(QtGui.QApplication.translate("MainWindow", "Boot Up Delay...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCommTimeout.setText(QtGui.QApplication.translate("MainWindow", "Comm Timeout...", None, QtGui.QApplication.UnicodeUTF8))

import AQresources_rc
