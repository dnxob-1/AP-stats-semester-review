import ast
import statistics as stats
import numpy as np

def iqr(fileWorker):
    try:
        f = open(fileWorker, "r")
        readContent = f.read().strip()
        numbers = ast.literal_eval(readContent)
        q1 = np.percentile(numbers, 25)
        q3 = np.percentile(numbers, 75)
        iqr = q3 - q1
        print("IQR:", iqr)
    except FileNotFoundError:
        print("Error: Are you sure you are using a correct file?")
