import ast
import statistics as stats

def zscore(fileWorker):
    xVal = int(input("X: "))
    try: 
        f = open(fileWorker, "r") 
        readContent = f.read().strip()
        numbers = ast.literal_eval(readContent)
        z = xVal - stats.mean(numbers) / stats.stdev(numbers)
        print(f"z: {z}")
        f.close()
    except FileNotFoundError:
        print("Error: No file usage")
    except stats.StatisticsError:
        print("Error: Could not calculate. Number of inputs for stdev < 2")
    except ZeroDivisionError:
        print("Error: stdev is equal to 0. Cannot divide by 0")
    except ValueError:
        print("Error: Enter an integer")
