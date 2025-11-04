import matplotlib.pyplot as plt
import ast
import os


def scatterPlot(fileWorkers=None, useSelect=""):
    try:

        directory = "./"
        print("Files in directory: ")
        textFilesInDir = [f for f in os.listdir(directory) if f.endswith(".txt")]
        for file in textFilesInDir:
            print(file)
        if useSelect.lower() == "y":
            f = open(fileWorkers, "r")
            data1 = f.read()
            f.close()
            file = str(input("Second file to work with (y): "))
            f = open(file, "r")
            data2 = f.read()
            f.close()
            data1 = ast.literal_eval(data1)
            data2 = ast.literal_eval(data2)
            labelX = str(input("X label: "))
            labelY = str(input("Y label: "))
            plotTitle = str(input("Title: "))
            plt.xlabel(labelX)
            plt.ylabel(labelY)
            plt.title(plotTitle)
            plt.scatter(data1, data2)
            plt.show()
        elif useSelect.lower() == "n" or useSelect == "":
            file = str(input("File to work with (x): "))
            f = open(file, "r")
            data1 = f.read()
            f.close()
            file = str(input("Second file to work with (y): "))
            f = open(file, "r")
            data2 = f.read()
            f.close()
            data1 = ast.literal_eval(data1)
            data2 = ast.literal_eval(data2)
            labelX = str(input("X label: "))
            labelY = str(input("Y label: "))
            plotTitle = str(input("Title: "))
            plt.xlabel(labelX)
            plt.ylabel(labelY)
            plt.title(plotTitle)
            plt.scatter(data1, data2)
            plt.show()
    except ValueError:
        print("Error: Did you enter a nonnegative integer?")
    except FileNotFoundError:
        print(
            "Error: Please check the files that you have chosen. One or more do not exist."
        )
