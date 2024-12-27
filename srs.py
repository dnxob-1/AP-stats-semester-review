import random

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
