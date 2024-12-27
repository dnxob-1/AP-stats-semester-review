import ast
import statistics as stats

def stdev(fileWorker):
    try:
        f = open(fileWorker, "r")
        readContent = f.read().strip()
        numbers = ast.literal_eval(readContent)
        print("σ:", stats.stdev(numbers))
    except FileNotFoundError:
        print("Error: Are you sure you are using a correct file?")
    except stats.StatisticsError:
        print("Error: Could not calculate. Number of inputs < 2")
