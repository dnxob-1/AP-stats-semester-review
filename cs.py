import ast
import numpy as np
import random

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

