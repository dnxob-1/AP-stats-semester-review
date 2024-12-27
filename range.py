import ast
import statistics as stats

def range(fileWorker):
    try:
        f = open(fileWorker, "r")
        readContent = f.read().strip()
        numbers = ast.literal_eval(readContent)
        print("Range:", max(numbers) - min(numbers))
    except FileNotFoundError:
        print("Error: Are you sure you are using a correct file?")
