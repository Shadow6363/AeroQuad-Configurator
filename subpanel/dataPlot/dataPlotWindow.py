# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataPlotWindow.ui'
#
# Created: Wed Nov 28 09:19:21 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_plotWindow(object):
    def setupUi(self, plotWindow):
        plotWindow.setObjectName('plotWindow')
        plotWindow.resize(540, 350)
        plotWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtGui.QGridLayout(plotWindow)
        self.gridLayout.setObjectName('gridLayout')
        #self.graphicsView = QtGui.QVBoxLayout(plotWindow)
        #self.graphicsView.setContentsMargins(0, 0, 0, 0)
        #self.graphicsView = PlotWidget(plotWindow)
        #self.graphicsView.setFrameShape(QtGui.QFrame.StyledPanel)
        #self.graphicsView.setFrameShadow(QtGui.QFrame.Plain)
        #self.graphicsView.setObjectName('graphicsView')
        #self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(plotWindow)
        self.treeWidget.setMaximumSize(QtCore.QSize(220, 16777215))
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName('treeWidget')
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setDefaultSectionSize(80)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.retranslateUi(plotWindow)
        QtCore.QMetaObject.connectSlotsByName(plotWindow)

    def retranslateUi(self, plotWindow):
        plotWindow.setWindowTitle(QtGui.QApplication.translate("plotWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("plotWindow", "Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("plotWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("plotWindow", "Value", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
