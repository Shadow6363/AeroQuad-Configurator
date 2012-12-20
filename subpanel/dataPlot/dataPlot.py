'''
Created on Nov 21, 2012

@author: Ted Carancho
'''

# Major library imports
from PySide import QtGui, QtCore
from collections import deque
from numpy import arange
from scipy.special import jn

# Enthought library imports
from enable.api import Window
from enable.example_support import DemoFrame, demo_main
from traits.api import HasTraits

# Chaco imports
from chaco.api import OverlayPlotContainer, create_line_plot, add_default_axes, \
                                 add_default_grids
from chaco.tools.api import MoveTool, PanTool, ZoomTool

# AeroQuad imports
from subpanel.subPanelTemplate import subpanel
from subpanel.dataPlot.dataPlotWindow import Ui_plotWindow

COLOR_PALETTE = ("mediumslateblue", "maroon", "darkgreen", "goldenrod",
                 "purple", "indianred")


class AnimatedPlot(HasTraits):
    def __init__(self, x, y, color="blue", bgcolor="white"):
        self.x_values = x[:]
        self.y_values = y[:]
        self.numpoints = len(self.x_values)

        plot = create_line_plot((self.x_values,self.y_values),
                                color=color, bgcolor=bgcolor, width=2.0)
        plot.resizable = "hv"
        plot.bounds = [1000, 600]

        self.plot = plot

        self.current_index = self.numpoints/2
        self.increment = 1

    def timer_tick(self):
        self.current_index += self.increment
        if self.current_index > self.numpoints:
            self.current_index = self.numpoints
        self.plot.index.set_data(self.x_values[self.current_index - 100:self.current_index])
        self.plot.value.set_data(self.y_values[self.current_index - 100:self.current_index])
        self.plot.index_mapper.range.add(self.plot.index)
        self.plot.value_mapper.range.add(self.plot.value)
        self.plot.request_redraw()



class dataPlot(QtGui.QWidget, subpanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        subpanel.__init__(self)

        self.ui = Ui_plotWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.hideAxis('bottom')
        self.ui.graphicsView.getAxis('top').setHeight(10)
        self.ui.graphicsView.getAxis('bottom').setHeight(10)
        self.ui.graphicsView.getAxis('left').setWidth(50)
        self.ui.graphicsView.setBackground((255,255,255))
        self.plotCount = 0
        self.legend = None
        self.colors = [QtGui.QColor('blue'),
                       QtGui.QColor('red'),
                       QtGui.QColor('lime'),
                       QtGui.QColor('cornflowerblue'),
                       QtGui.QColor('greenyellow'),
                       QtGui.QColor('violet'),
                       QtGui.QColor('orange'),
                       QtGui.QColor('deepskyblue'),
                       QtGui.QColor('firebrick'),
                       QtGui.QColor('aqua')]

    def start(self, xmlSubPanel):
        '''This method starts a timer used for any long running loops in a subpanel'''
        self.xmlSubPanel = xmlSubPanel

        self.plotIndex = int(self.xml.find(self.xmlSubPanel + "/Index").text)
        plotSize = int(self.xml.find(self.xmlSubPanel + "/PlotSize").text)
        plotNames = self.xml.findall(self.xmlSubPanel + "/PlotName")
        self.plotCount = len(plotNames)

        self.output = []
        for i in range(self.plotCount):
            self.output.append(deque([0.0]*plotSize))

        self.axis = deque(range(plotSize))
        self.value = plotSize

        self.ui.treeWidget.clear()
        for i in range(self.plotCount):
            plotName = plotNames[i].text
            newLine = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            newLine.setCheckState(0, 2)
            newLine.setBackgroundColor(0, self.colors[i])
            newLine.setText(1, plotName + "   ")
            newLine.setText(2, "0.000")
        self.ui.treeWidget.resizeColumnToContents(0)
        self.ui.treeWidget.resizeColumnToContents(1)
        self.legend = self.ui.treeWidget.invisibleRootItem()

        if self.comm.isConnected() == True:
            telemetry = self.xml.find(self.xmlSubPanel + "/Telemetry").text
            if telemetry != "":
                self.comm.write(telemetry)
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.readContinuousData)
            self.timer.start(5)

    def readContinuousData(self):
        '''This method continually reads telemetry from the AeroQuad'''
        if self.comm.isConnected() == True:
            if self.comm.dataAvailable():
                rawData = self.comm.read()
                data = rawData.split(",")
                self.ui.graphicsView.clear()
                for i in range(self.plotCount):
                    legendRow = self.legend.child(i)
                    if legendRow.checkState(0) == 2:
                        try:
                            dataValue = data[i + self.plotIndex]
                            self.output[i].appendleft(float(dataValue))
                            self.output[i].pop()
                        except:
                            pass # Do not update output data if invalid number detected from comm read
                        self.ui.graphicsView.plot(y=list(self.output[i]), pen=pg.mkPen(self.colors[i], width=3))
                        legendRow.setText(2, dataValue)

