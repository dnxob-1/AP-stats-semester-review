import numpy as np
import ast

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
