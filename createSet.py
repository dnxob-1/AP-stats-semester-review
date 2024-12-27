import re


def makeSet(n):
    try:
        mainInput = int(input("Enter number of list: "))
        secondInput = [0] * mainInput 

        for i in range(mainInput):
            try:
                secondInput[i] = float(input(f"Number {i}: "))
                f = open(f"set{n}.txt", "w")
                f.write(str(secondInput))
            except ValueError:
                print("Error: Please enter a number")
                exit(1)
        f.close()
    except ValueError:
        print("Error: Enter a valid integer")
    except UnboundLocalError:
        print("Error: Enter a valid integer")
