import statistics as stats
import re
import os
import ast
import random

def makeSet(n):
    maininput = str(input("Enter number of list: "))
    # input takes in a float, should not be possible

    numbers = re.findall(r"\d+", maininput)
    result = int("".join(map(str, numbers)))

    secondInput = [0] * result

    for i in range(result):
        try:
            secondInput[i] = float(input(f"Number {i}: "))
            f = open(f"set{n}.txt", "w")
            f.write(str(secondInput))
        except ValueError:
            print("Error: Please enter a number")
            exit(1)
    f.close()
    
def selectSet(fileWorker):
    directory = './'  

    text_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    print("Current .txt files in directory:")
    for file in text_files:
        print(file)

    fileWorker = input("Please choose a file to work with: ")
    for file in text_files:
        if fileWorker == file:
            print("ok")
            break

    return fileWorker

def mean(fileWorker):
    try:
        f = open(fileWorker, "r")
        readContent = f.read().strip()
        numbers = ast.literal_eval(readContent)
        print("μ:", stats.mean(numbers))
    except FileNotFoundError:
        print("Error: Are you sure you are using a correct file?")

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

def removeFiles():
    directory = './'  

    text_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    try:
        print("Current .txt files in directory:")
        for file in text_files:
            print(file)
        fileRemover = input("Please choose a file to remove: ")
        os.remove(fileRemover)
        print("Removed: ", fileRemover)
    except FileNotFoundError:
        print("Error: The file does not exist")

def zscore(fileWorker):
    xVal = int(input("X: "))
    try: 
        f = open(fileWorker, "r")
        readContent = f.read().strip()
        numbers = ast.literal_eval(readContent)
        z = xVal - stats.mean(numbers) / stats.stdev(numbers)
        print(f"z: {z}")
    except FileNotFoundError:
        print("Error: No file usage")
    except stats.StatisticsError:
        print("Error: Could not calculate. Number of inputs for stdev < 2")
    except ZeroDivisionError:
        print("Error: stdev is equal to 0. Cannot divide by 0")



def advancedSets():
    userChoice = str(input("(Sam)ple or (Pop)ulation: "))
    if "pop" in userChoice:
        print("Selected option: Population.")
        popNumber = int(input("Population amount: "))
        popRangeMin = int(input("Minimum number: "))
        popRangeMax = int(input("Maximum number: "))
        popSet = [0] * popNumber
        for i in range(len(popSet)):
            popSet[i] = random.randint(popRangeMin, popRangeMax)

        print(popSet)

def my_terminal():
    print("Welcome to my AP Stats project.'help' for help.")
    n = 0
    fileWorker = ""
    while True:
        command = input(">> ").strip().lower()
        if command == "exit":
            print("nighty!")
            break
        elif command == "help":
            print("Commands: help, clear, echo, exit, selector, set, mean, stdev, zscore, remove, set advanced")
        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command.startswith("echo "):
            print(command[5:])
        elif command == "selector":
            fileWorker = selectSet(fileWorker)
            print(fileWorker)
        elif command == "set":
            n += 1
            makeSet(n)
        elif command == "mean":
            mean(fileWorker)
        elif command == "stdev":
            stdev(fileWorker)
        elif command == "remove":
            removeFiles()
        elif command == "zscore":
            zscore(fileWorker)
        elif command == "set advanced":
            advancedSets()
        else:
            print("Unknown command.")


if __name__ == "__main__":
    my_terminal()
