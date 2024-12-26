import statistics as stats
import re
import os
import ast
import random
import numpy as np

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

    textFilesInDir = [f for f in os.listdir(directory) if f.endswith('.txt')]

    if textFilesInDir:
        print("Current .txt files in directory:")
        for file in textFilesInDir:
            print(file)

        fileWorker = input("Please choose a file to work with: ")
        for file in textFilesInDir:
            if fileWorker == file:
                print("ok")
                break

    else:
        print("No text files in current directory. Make a new set first.")
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

    textFilesInDir = [f for f in os.listdir(directory) if f.endswith('.txt')]

    if textFilesInDir:
        try:
            print("Current .txt files in directory:")
            for file in textFilesInDir:
                print(file)
            fileRemover = input("Please choose a file to remove: ")
            os.remove(fileRemover)
            print("Removed: ", fileRemover)
        except FileNotFoundError:
            print("Error: The file does not exist")

    else:
        print("No text files left in this current directory.")

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

    f.close()


def displayCurrentlySelectedSet(fileWorker):
    print("Current file: ", fileWorker)

def simpleSample(fileChoice, p):
    try:
        numberOfSample = int(input("Enter Number of samples: "))
        fi = open(fileChoice, "r")
        temp = fi.read().split()
        samSet = random.sample(temp, numberOfSample)
        print("ok. Sample set: ", samSet)
        fi.close()
        f = open(f"setSam{p}.txt", "w")
        f.write(str(samSet))
        f.close()
    except ValueError:
        print("Error: Enter a sample number less than the population or enter a nonnegative number for the sample size.")

def stratifiedSample(fileChoice, p):
    strataSize = int(input("Enter size of stratums: "))
    samStrata = int(input("Enter number of samples: "))
    strata = {}
    finalSam = []
    fi = open(fileChoice, "r")
    samSet = fi.read()
    fi.close()
    samSet = ast.literal_eval(samSet)
    for value in samSet:
        stratum = (value // strataSize) * strataSize  
        
        if stratum not in strata:
            strata[stratum] = []
        
        strata[stratum].append(value)

    
    for stratum, values in strata.items():
        if len(values) >= samStrata:
            finalSam.extend(random.sample(values, samStrata))
        else:
            finalSam.extend(values)

    print(finalSam)
    f = open(f"setSam{p}.txt", "w")
    f.write(str(finalSam))
    f.close()
 
def systematicSample(fileChoice, p):
    try:
        fi = open(fileChoice, "r")
        samSet = fi.read()
        fi.close()
        samSet = ast.literal_eval(samSet)
        k = int(input("Number of steps: "))
        numOfSample = int(input("Number of samples: "))
        start = np.random.randint(0, k)
        finalSam = samSet[start::k][:numOfSample]
        f = open(f"setSam{p}.txt", "w")
        f.write(str(finalSam))
        f.close()
        print("Sampled set: ", finalSam)
    except ValueError:
        print("Error: The max number of samples cannot be exceeded")

    
def clusterSample(fileChoice, p):
    try:
        clusterAmount = int(input("Cluster number: "))
        clusterPoints = int(input("Cluster points: "))
        wantedCluster = int(input("Clusters: "))
        fi = open(fileChoice, "r")
        samSet = fi.read()
        fi.close()
        samSet = ast.literal_eval(samSet)
        samSet = np.array(samSet)
        samSet = samSet.reshape(clusterAmount, clusterPoints)
        clusters = random.sample(range(samSet.shape[0]), wantedCluster)
        f = open(f"setSam{p}.txt", "w")
        f.write(str(clusters))
        f.close()
        print("Sampled set: ", clusters)
    except ValueError:
        print("Error: Enter a nonnegative integer")


def advancedSets(j, p):
    userChoice = str(input("(Sam)ple or (Pop)ulation: "))
    directory = './'  
    print(userChoice)
    if userChoice.lower() == 'pop':
        print("Selected option: Population.")
        manOrNot = str(input("Manually enter population (Y/n): "))
        if manOrNot.lower() == 'y':
            numOfPop = int(input("Enter number of list: "))
    
            arrToFile = [0] * numOfPop 

            for i in range(numOfPop):
                try:
                    arrToFile[i] = float(input(f"Number {i}: "))
                    f = open(f"setPop{j}.txt", "w")
                    f.write(str(arrToFile))
                except ValueError:
                    print("Error: Please enter a number")
                    exit(1)
            f.close()
        elif manOrNot.lower() == 'n':
            try:
                popNumber = int(input("Population amount: "))
                popRangeMin = int(input("Minimum number: "))
                popRangeMax = int(input("Maximum number: "))
                popSet = [0] * popNumber
                for i in range(len(popSet)):
                    popSet[i] = random.randint(popRangeMin, popRangeMax)
                f = open(f"setPop{j}.txt", "w")
                f.write(str(popSet))
            except ValueError:
                print("Error: Enter an integer")
    elif userChoice.lower() == 'sam':
        # p does not increment
        print("Selected option: Sample.")
        textFilesInDir = [f for f in os.listdir(directory) if f.startswith('setPop')]
        if textFilesInDir:
            print("Current population files in directory:")
            for file in textFilesInDir:
                print(file)
            fileChoice = str(input("Choose a file to work with: "))
            print(fileChoice, "has been chosen.")
            try:
                print("Techniques: Simple Random Sampling(SRS), Stratified Sampling(SS), Systematic Sampling(SYS), Cluster Sampling(CS)")
                samTech = str(input("Choose a Sampling technique: "))
                if samTech.lower() == 'srs':
                    simpleSample(fileChoice, p)
                elif samTech.lower() == 'ss':
                    stratifiedSample(fileChoice, p)
                elif samTech.lower() == 'sys':
                    systematicSample(fileChoice, p)
                elif samTech.lower() == 'cs':
                    clusterSample(fileChoice, p)
            except FileNotFoundError:
                p -= 1
                j -= 1
                print("Error: File not found. Correct file?")

        else:
            print("No population files in current directory. Choose the Pop option.")


#def plotData():


def my_terminal():
    print("Welcome to my AP Stats project. 'help' for help.")
    n = 0
    j = 0
    p = 0
    fileWorker = ""
    while True:
        command = input(">> ").strip().lower()
        if command == "exit":
            print("nighty!")
            break
        elif command == "help":
            print("Commands: help, clear, echo, exit, selector, set, mean, stdev, zscore, remove, set advanced, display")
        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command.startswith("echo "):
            print(command[5:])
        elif command == "selector":
            fileWorker = selectSet(fileWorker)
        elif command == "set":
            n += 1
            makeSet(n)
        elif command == "mean":
            mean(fileWorker)
        elif command == "stdev":
            stdev(fileWorker)
        elif command == "remove":
            removeFiles()
            #make it so that it can be ran from the terminal and not a different function 
        elif command == "zscore":
            zscore(fileWorker)
        elif command == "set advanced":
            j += 1
            p += 1
            advancedSets(j, p)
        elif command == "display":
            displayCurrentlySelectedSet(fileWorker)
        else:
            print("Unknown command.")


if __name__ == "__main__":
    my_terminal()
