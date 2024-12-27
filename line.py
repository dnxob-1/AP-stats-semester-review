import ast
import matplotlib.pyplot as plt

def linePlot(fileWorkers=None, useSelect=""):
    try:
        if useSelect.lower() == 'y':
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
            print("Marker styles: . , o v ^ < > 1 2 3 4 s p * h H + x D d _ None")
            marker = str(input("Marker: "))
            plt.xlabel(labelX)
            plt.ylabel(labelY)
            plt.title(plotTitle)
            plt.plot(data1, data2, marker=marker)
            plt.show()
        elif useSelect.lower() == 'n' or useSelect == "":
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
            print("Marker styles: . , o v ^ < > 1 2 3 4 s p * h H + x D d _ None")
            marker = str(input("Marker: "))
            plt.xlabel(labelX)
            plt.ylabel(labelY)
            plt.title(plotTitle)
            plt.plot(data1, data2, marker=marker)
            plt.show()
    except ValueError:
        print("Error: Did you enter a nonnegative integer or did you enter a correct marker?")
    except FileNotFoundError:
        print("Error: Please check the files that you have chosen. One or more do not exist.")

