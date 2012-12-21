# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commMonitorWindow.ui'
#
# Created: Mon Dec 10 04:44:54 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_commMonitor(object):
    def setupUi(self, commMonitor):
        commMonitor.setObjectName('commMonitor')
        commMonitor.resize(818, 418)
        self.gridLayout = QtGui.QGridLayout(commMonitor)
        self.gridLayout.setObjectName('gridLayout')
        self.lineEdit = QtGui.QLineEdit(commMonitor)
        self.lineEdit.setObjectName('lineEdit')
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.sendButton = QtGui.QPushButton(commMonitor)
        self.sendButton.setObjectName('sendButton')
        self.gridLayout.addWidget(self.sendButton, 1, 1, 1, 1)
        self.clearButton = QtGui.QPushButton(commMonitor)
        self.clearButton.setObjectName('clearButton')
        self.gridLayout.addWidget(self.clearButton, 1, 2, 1, 1)
        self.commLog = QtGui.QTextBrowser(commMonitor)
        self.commLog.setFrameShadow(QtGui.QFrame.Sunken)
        self.commLog.setObjectName('commLog')
        self.gridLayout.addWidget(self.commLog, 0, 0, 1, 3)

        self.retranslateUi(commMonitor)
        QtCore.QMetaObject.connectSlotsByName(commMonitor)

    def retranslateUi(self, commMonitor):
        commMonitor.setWindowTitle(QtGui.QApplication.translate("commMonitor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("commMonitor", "Send Command", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("commMonitor", "Clear", None, QtGui.QApplication.UnicodeUTF8))

