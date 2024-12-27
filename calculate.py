def calculate():
    try:
        userCalculation = str(input("Enter calculation: "))
        print(eval(userCalculation))
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except NameError:
        print("Error: Enter an integer.")
    except SyntaxError:
        print("Error: Variables are not allowed.")
