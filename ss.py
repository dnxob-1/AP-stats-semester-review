import ast
import random

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

    print("Sample:", finalSam)
    f = open(f"setSam{p}.txt", "w")
    f.write(str(finalSam))
    f.close()
