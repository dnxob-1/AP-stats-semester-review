from scatter import scatterPlot
from histogram import histogramPlot
from line import linePlot
from pie import piePlot
from bar import barPlot

def plotData(fileWorker):
    print("Possible types of plots: scatter, histo, line, pie, bar")
    typeOfPlot = str(input("Enter type: "))
    if fileWorker:
        useSelect = str(input("Use selected file? (Y/n): "))
        if "scatter" in typeOfPlot:
            scatterPlot(fileWorker, useSelect)
        elif "histo" in typeOfPlot:
            histogramPlot(fileWorker, useSelect)
        elif "line" in typeOfPlot:
            linePlot(fileWorker, useSelect)
        elif "pie" in typeOfPlot:
            piePlot(fileWorker, useSelect)
        elif "bar" in typeOfPlot:
            barPlot(fileWorker, useSelect)
    else:
        if "scatter" in typeOfPlot:
            scatterPlot()
        elif "histo" in typeOfPlot:
            histogramPlot()
        elif "line" in typeOfPlot:
            linePlot()
        elif "pie" in typeOfPlot:
            piePlot()
        elif "bar" in typeOfPlot:
            barPlot()
