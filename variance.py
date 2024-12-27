import ast
import statistics as stats

def variance(fileWorker):
    try:
        f = open(fileWorker, "r")
        readContent = f.read().strip()
        numbers = ast.literal_eval(readContent)
        print("σ^2:", stats.variance(numbers))
    except FileNotFoundError:
        print("Error: Are you sure you are using a correct file?")
