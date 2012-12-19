'''
Created on Nov 21, 2012

@author: Ted Carancho
'''

from PyQt4 import QtGui, QtCore
from collections import deque
from subpanel.subPanelTemplate import subpanel
from subpanel.dataPlot.dataPlotWindow import Ui_plotWindow
from matplotlib import animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

import numpy as np
import pylab

#import pyqtgraph as pg

class dataPlot(QtGui.QWidget, subpanel):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        subpanel.__init__(self)

        #pg.setConfigOption('background', (255,255,255))
        #pg.setConfigOption('foreground', (128,128,128))
        
        self.ui = Ui_plotWindow()
        self.ui.setupUi(self)
        

        #self.ui.axes.set_axis_bgcolor('white')
        #self.ui.axes.get_title().set_visible(False)
        #self.ui.axes.get_xaxis().set_visible(False)

        #pylab.setp(self.ui.axes.get_yticklabels(), fontsize=8)

        #self.ui.axes.grid(True, color='gray')


        #self.ui.graphicsView.hideAxis('bottom')
        #self.ui.graphicsView.showGrid(y=True)
        #self.ui.graphicsView.getAxis('top').setHeight(10)
        #self.ui.graphicsView.getAxis('bottom').setHeight(10)
        #self.ui.graphicsView.getAxis('left').setWidth(50)
        #self.ui.graphicsView.enableAutoRange(False)
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

        #window_color = QtGui.QApplication.palette().color(QtGui.QPalette.Window)
        #facecolor    = (window_color.redF(), window_color.greenF(), window_color.blueF())

        #self.ui.figure = Figure((5.5, 3.5), dpi=110, facecolor=facecolor, tight_layout=True)
        #self.ui.axes = self.ui.figure.add_subplot(111)

        #self.ui.axes.clear()
        #self.ui.axes.cla()

        #self.ui.figure.clear()
        #self.ui.axes.clear()

        #window_color = QtGui.QApplication.palette().color(QtGui.QPalette.Window)
        #facecolor    = (window_color.redF(), window_color.greenF(), window_color.blueF())

        #self.ui.figure = Figure((5.5, 3.5), dpi=110, facecolor=facecolor, tight_layout=True)
        #self.ui.axes = self.ui.figure.add_subplot(111)

        #self.ui.graphicsView = FigureCanvas(self.ui.figure)

        #FigureCanvas.setSizePolicy(self.ui.graphicsView,
        #                           QtGui.QSizePolicy.Expanding,
        #                           QtGui.QSizePolicy.Expanding)

        

        #self.graphicsView = PlotWidget(plotWindow)
        #self.graphicsView.setFrameShape(QtGui.QFrame.StyledPanel)
        #self.graphicsView.setFrameShadow(QtGui.QFrame.Plain)
        #self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        #self.ui.gridLayout.addWidget(self.ui.graphicsView, 0, 1, 1, 1)

        #self.ui.graphicsView.refresh()
        #self.ui.graphicsView.show()

        self.ui.axes = self.ui.figure.add_subplot(111)

        self.ui.axes.get_xaxis().set_visible(False)

        pylab.setp(self.ui.axes.get_yticklabels(), fontsize=8)

        self.ui.axes.grid(True, color='gray')

        self.lines = []
        self.output = []
        for i in range(self.plotCount):
            self.output.append(deque([0.0]*plotSize))
            self.lines.append(self.ui.axes.plot(
                [], 
                linewidth=1.5,
                color=(self.colors[i].redF(), self.colors[i].greenF(), self.colors[i].blueF())
            )[0])
            
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

        self.anim = animation.FuncAnimation(self.ui.graphicsView.figure, self.animate, init_func=self.init, frames=200, interval=20, blit=True)

        #self.ui.graphicsView.draw()

        #self.ui.axes.get_yaxis().set_visible(True)

            
        if self.comm.isConnected() == True:
            telemetry = self.xml.find(self.xmlSubPanel + "/Telemetry").text
            if telemetry != "":
                self.comm.write(telemetry)
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.readContinuousData)
            self.timer.start(20)
    
    def stop(self):
        '''This method enables a flag which closes the continuous serial read thread'''
        self.anim._stop()
        #for i in range(self.plotCount):
        #    self.output[i].clear()
        #self.ui.axes.cla()
        #self.ui.figure.delaxes(self.ui.axes)
        #self.ui.gridLayout.removeWidget(self.ui.graphicsView)

        if self.comm.isConnected() == True:
            if self.timer != None:
                self.timer.timeout.disconnect(self.readContinuousData)
                self.timer.stop()
        
        #self.anim = None
        
        #self.ui.figure.clf()
        #self.ui.figure.clear()
        #self.ui.graphicsView.figure.clear()
        #self.ui.graphicsView.stop_event_loop()
        #self.ui.graphicsView.flush_events()
        #self.ui.graphicsView.close()
        #self.ui.gridLayout.removeWidget(self.ui.graphicsView)

        #self.clear()
        #self.ui.axes.clear()
        #self.ui.figure.clf()
        #self.ui.graphicsView.figure.clear()
        #self.ui.axes = self.ui.figure.add_subplot(111)
        #self.ui.graphicsView = FigureCanvas(self.ui.figure)
        #print 'stopped'
        #self.anim = None
        #self.ui.axes.clear()

    def init(self):
        #self.ui.axes.get_yaxis().set_visible(False)
        changed = []
        for line in self.lines:
            line.set_data([], [])
            changed.append(line)
        #changed.append(self.ui.axes.get_yaxis())

        return changed

    def animate(self, i):
        #self.ui.axes.get_yaxis().set_visible(True)
        changed = []

        for j in range(self.plotCount):
            self.lines[j].set_data(np.arange(len(self.output[j])), np.array(self.output[j]))
            changed.append(self.lines[j])
        #changed.append(self.ui.axes.get_yaxis())
        
        return changed



    def readContinuousData(self):
        '''This method continually reads telemetry from the AeroQuad'''
        if self.comm.isConnected() == True: 
            if self.comm.dataAvailable():
                yMinimum, yMaximum = 9999999, -9999999

                rawData = self.comm.read()
                data = rawData.split(",")
                #self.ui.graphicsView.clear()
                for i in range(self.plotCount):
                    legendRow = self.legend.child(i)
                    if legendRow.checkState(0) == 2:
                        if len(self.output[i]) == 0:
                            self.output[i] = deque([0.0] * self.value)
                        try:
                            dataValue = data[i + self.plotIndex]
                            self.output[i].appendleft(float(dataValue))
                            #if len(self.output[i]) > self.plotSize:
                            self.output[i].pop()
                            legendRow.setText(2, dataValue)
                        except:
                            pass # Do not update output data if invalid number detected from comm read
                        #self.ui.graphicsView.plot(y=list(self.output[i]), pen=pg.mkPen(self.colors[i], width=2))
                        

                        yMinimum = round(min(yMinimum, min(self.output[i])), 0) - 1
                        yMaximum = round(max(yMaximum, max(self.output[i])), 0) + 1

                        #print yMinimum

                        self.ui.axes.set_xbound(lower=0, upper=128)
                        self.ui.axes.set_ybound(lower=yMinimum, upper=yMaximum)

                        #self.plots[i].set_xdata(numpy.arange(len(self.output[i])))
                        #self.plots[i].set_ydata(numpy.array(self.output[i]))
                    else:
                        self.output[i].clear()
                        #self.ui.axes.relim()

                    #yMinimum = round(min(yMinimum, min(self.output[i])), 0) - 1
                    #yMaximum = round(max(yMaximum, max(self.output[i])), 0) + 1

                    #self.ui.axes.set_xbound(lower=0, upper=128)
                    #self.ui.axes.set_ybound(lower=yMinimum, upper=yMaximum)
            #self.ui.graphicsView.draw()
