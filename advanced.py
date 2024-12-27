from srs import simpleSample
from ss import stratifiedSample
from syS import systematicSample
from cs import clusterSample
import random
import os

def advancedSets(j, p):
    userChoice = str(input("(Sam)ple or (Pop)ulation: "))
    directory = './'  
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

