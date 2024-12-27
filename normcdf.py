import ast
import numpy as np
from scipy.stats import norm
import statistics as stats

def cumulativeDistFunc(fileWorker):
    try:
        f = open(fileWorker, "r")
        readContent = f.read().strip()
        numbers = ast.literal_eval(readContent)
        mean = stats.mean(numbers)
        stdev = stats.stdev(numbers)
        xStart = float(input("Enter start number: "))
        xEnd = float(input("Enter end number: "))
        pointNum = int(input("Enter number of points: "))
        x = np.linspace(xStart, xEnd, pointNum)
        print("Normalcdf:", norm.cdf(x, loc=mean, scale=stdev))
    except FileNotFoundError:
        print("Error: Are you sure you are using a correct file?")
