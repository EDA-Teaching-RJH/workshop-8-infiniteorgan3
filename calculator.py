def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: You cannot divide by zero."

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    continuing = "y"
    validchoices = ["div", "multiply", "add", "subtract"]
    while continuing == "y":
        tries = 3
        choice = ""
        while choice not in validchoices and tries > 0:
            choice = input("Which calculator function would you like to use?\n")
        if choice in validchoices:
            inputa = ""
            while validatenum(inputa) == False:
                inputa = input("The first number: ")
            inputb = ""
            while validatenum(inputb) == False:
                inputb = input("The second number: ")
            match choice:
                case "div":
                    result = divide(inputa, inputb)
                case "multiply":
                    result = multiply(inputa, inputb)
                case "add":
                    result = add(inputa, inputb)
                case "subtract":
                    result = subtract(inputa, inputb)
            print(f"Result: {result}")
            contchoice = ""
            attempts = 3
            while contchoice != "y" and contchoice != "n" and attempts > 0:
                contchoice = input("Would you like to continue the program? y/n")
            if contchoice != "y" and contchoice != "n":
                continuing = "n"
            else:
                continuing = contchoice
        else:
            print("You have not entered a suitable function, so the program will exit.")
            continuing = "n"

   
def validatenum(input):
    try:
        intinput = int(input)
    except ValueError:
        print("Not a valid number.")
        return False
    else:
        return intinput
        
if __name__ == "__main__":
    main()