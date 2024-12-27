import ast
import matplotlib.pyplot as plt

def histogramPlot(fileWorkers=None, useSelect=""):
    try:
        if useSelect.lower() == 'y':
            f = open(fileWorkers, "r")
            data1 = f.read()
            f.close()
            data1 = ast.literal_eval(data1)
            labelX = str(input("X label: "))
            labelY = str(input("Y label: "))
            plotTitle = str(input("Title: "))
            bins = str(input("Number of bins (or auto): "))
            if "auto" not in bins:
                bins = int(bins)
            plt.xlabel(labelX)
            plt.ylabel(labelY)
            plt.title(plotTitle)
            plt.hist(data1, bins=bins)
            plt.show()
        elif useSelect.lower() == 'n' or useSelect == "":
            file = str(input("File to work with (x): "))
            f = open(file, "r")
            data1 = f.read()
            f.close()
            data1 = ast.literal_eval(data1)
            labelX = str(input("X label: "))
            labelY = str(input("Y label: "))
            plotTitle = str(input("Title: "))
            bins = str(input("Number of bins (or auto): "))
            if "auto" not in bins:
                bins = int(bins)
            plt.xlabel(labelX)
            plt.ylabel(labelY)
            plt.title(plotTitle)
            plt.hist(data1, bins=bins)
            plt.show()
    except ValueError:
        print("Error: Did you enter a nonnegative integer?")
    except FileNotFoundError:
        print("Error: Please check the files that you have chosen. One or more do not exist.")

