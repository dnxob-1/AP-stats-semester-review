import re


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
