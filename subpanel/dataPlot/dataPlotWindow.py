# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataPlotWindow.ui'
#
# Created: Wed Nov 28 09:19:21 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar2

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_plotWindow(object):
    def setupUi(self, plotWindow):
        plotWindow.setObjectName(_fromUtf8("plotWindow"))
        plotWindow.resize(540, 350)
        plotWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtGui.QGridLayout(plotWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        window_color = QtGui.QApplication.palette().color(QtGui.QPalette.Window)
        facecolor    = (window_color.redF(), window_color.greenF(), window_color.blueF())

        self.figure = Figure((5.5, 3.5), dpi=110, facecolor=facecolor, tight_layout=True)
        #self.axes = self.figure.add_subplot(111)

        self.graphicsView = FigureCanvas(self.figure)

        FigureCanvas.setSizePolicy(self.graphicsView,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)

        

        #self.graphicsView = PlotWidget(plotWindow)
        #self.graphicsView.setFrameShape(QtGui.QFrame.StyledPanel)
        #self.graphicsView.setFrameShadow(QtGui.QFrame.Plain)
        #self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)

        #self.navigation_toolbar = NavigationToolbar2(self.graphicsView, plotWindow)
        #self.gridLayout.addWidget(self.navigation_toolbar, 1, 1, 1, 1)

        self.treeWidget = QtGui.QTreeWidget(plotWindow)
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
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

#from pyqtgraph import PlotWidget
