'''
Created on Nov 21, 2012

@author: Ted Carancho
'''

# Major library imports
from PySide import QtCore, QtGui
#from pyface.qt import QtGui
from collections import deque
from numpy import arange, zeros
from scipy.special import jn

# Enthought library imports
from enable.api import Window
from traits.api import HasTraits

# Chaco imports
from chaco.api import OverlayPlotContainer, create_line_plot, add_default_axes, \
                                 add_default_grids
from chaco.tools.api import MoveTool, PanTool, ZoomTool

# AeroQuad imports
from subpanel.subPanelTemplate import subpanel
from subpanel.dataPlot.dataPlotWindow import Ui_plotWindow

COLOR_PALETTE = ("mediumslateblue", "maroon", "darkgreen", "goldenrod",
                 "purple", "indianred", "deepskyblue", "lime", "firebrick")
COLOR_PALETTE = (
    'blue', 'red', 'lime', 'cornflowerblue',
    'greenyellow', 'violet', 'orange',
    'deepskyblue', 'firebrick', 'aqua'
)


class AnimatedPlot(HasTraits):
    def __init__(self, x, y, color="blue", bgcolor="white"):
        self.x_values = x[:]
        self.y_values = y[:]
        self.numpoints = len(self.x_values)

        plot = create_line_plot((self.x_values,self.y_values),
                                color=color, bgcolor=bgcolor, width=2.0)
        plot.resizable = "hv"

        self.plot = plot

        self.current_index = 64
        self.increment = 1

    def timer_tick(self):
        self.plot.index.set_data(self.x_values)
        self.plot.value.set_data(self.y_values)
        self.plot.index_mapper.range.add(self.plot.index)
        self.plot.value_mapper.range.add(self.plot.value)
        self.plot.request_redraw()



class dataPlot(QtGui.QWidget, subpanel):
    def __init__(self, parent=None):
        super(dataPlot, self).__init__(parent)
        subpanel.__init__(self)

        self.loaded = False

        self.ui = Ui_plotWindow()
        self.ui.setupUi(self)

        #self.plotCount = 0
        #self.legend = None
        '''
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
        '''

    def _create_window(self):
        x = arange(128)
        y = [0.0] * 128

        container = OverlayPlotContainer(padding=40, bgcolor="white",
                                         use_backbuffer=True,
                                         border_visible=True,
                                         fill_padding=True)

        self.animated_plots = []
        index_mapper = None
        value_mapper = None
        for i in range(self.plotCount):
            animated_plot = AnimatedPlot(x, y, COLOR_PALETTE[i])
            if value_mapper is None:
                index_mapper = animated_plot.plot.index_mapper
                value_mapper = animated_plot.plot.value_mapper
                add_default_grids(animated_plot.plot)
                add_default_axes(animated_plot.plot)
            else:
                animated_plot.plot.index_mapper = index_mapper
                index_mapper.range.add(animated_plot.plot.index)
                animated_plot.plot.value_mapper = value_mapper
                value_mapper.range.add(animated_plot.plot.value)
            container.add(animated_plot.plot)
            self.animated_plots.append(animated_plot)

        self.container = container
        return Window(self, -1, component=container)


    def start(self, xmlSubPanel):
        '''This method starts a timer used for any long running loops in a subpanel'''
        self.xmlSubPanel = xmlSubPanel

        self.plotIndex = int(self.xml.find(self.xmlSubPanel + "/Index").text)
        plotSize = int(self.xml.find(self.xmlSubPanel + "/PlotSize").text)
        plotNames = self.xml.findall(self.xmlSubPanel + "/PlotName")
        self.plotCount = len(plotNames)

        if not self.loaded:
            '''
            self.enable_win = self._create_window()

            layout = QtGui.QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self.enable_win.control)

            self.setLayout(layout)
            '''

            self.enable_win = self._create_window()

            self.ui.gridLayout.addWidget(self.enable_win.control, 0, 1, 1, 1)

            self.loaded = True


        self.ui.treeWidget.clear()
        for i in range(self.plotCount):
            plotName = plotNames[i].text
            newLine = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            newLine.setCheckState(0, QtCore.Qt.Checked)
            newLine.setBackground(0, QtGui.QColor(COLOR_PALETTE[i]))
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

    def stop(self):
        '''This method enables a flag which closes the continuous serial read thread'''
        if self.comm.isConnected() == True:
            if self.timer != None:
                self.timer.timeout.disconnect(self.readContinuousData)
                self.timer.stop()

    def readContinuousData(self):
        '''This method continually reads telemetry from the AeroQuad'''
        if self.comm.isConnected() == True:
            if self.comm.dataAvailable():
                rawData = self.comm.read()
                data = rawData.split(",")

                for i in range(self.plotCount):
                    legendRow = self.legend.child(i)
                    if legendRow.checkState(0) == 2:
                        self.animated_plots[i].plot.visible = True
                        try:
                            dataValue = data[i + self.plotIndex]
                            self.animated_plots[i].y_values.insert(0, float(dataValue))
                            self.animated_plots[i].y_values.pop()

                            legendRow.setText(2, dataValue)
                        except:
                            pass # Do not update output data if invalid number detected from comm read
                    else:
                        dataValue = '0.000'
                        self.animated_plots[i].y_values = [0.0] * 128
                        self.animated_plots[i].plot.visible = False

                        legendRow.setText(2, dataValue)

                    self.animated_plots[i].timer_tick()