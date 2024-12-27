import ast
import statistics as stats

def mean(fileWorker):
    try:
        f = open(fileWorker, "r")
        readContent = f.read().strip()
        numbers = ast.literal_eval(readContent)
        print("μ:", stats.mean(numbers))
    except FileNotFoundError:
        print("Error: Are you sure you are using a correct file?")
