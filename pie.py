import ast
import matplotlib.pyplot as plt
import os


def piePlot(fileWorkers=None, useSelect=""):
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
            data1 = ast.literal_eval(data1)
            plotTitle = str(input("Title: "))
            categories = str(input("Categories: ")).split()
            plt.title(plotTitle)
            plt.pie(data1, labels=categories, autopct="%1.1f%%")
            plt.show()
        elif useSelect.lower() == "n" or useSelect == "":
            file = str(input("File to work with (x): "))
            f = open(file, "r")
            data1 = f.read()
            f.close()
            data1 = ast.literal_eval(data1)
            plotTitle = str(input("Title: "))
            categories = str(input("Categories: ")).split()
            plt.title(plotTitle)
            plt.pie(data1, labels=categories, autopct="%1.1f%%")
            plt.show()
    except ValueError:
        print(
            "Error: Did you enter a nonnegative integer? Your categories must be the length of x."
        )
    except FileNotFoundError:
        print(
            "Error: Please check the files that you have chosen. One or more do not exist."
        )
