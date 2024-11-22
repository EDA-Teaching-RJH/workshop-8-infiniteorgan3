def add_student(name, age, grade):
    with open("students.txt", "a") as file:
        file.write(f"{name}, Age: {age}, Grade: {grade}\n")


def display_students():
    with open("students.txt", "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line)


def find_student(name):
    with open("students.txt", "r") as reader:
        while True:
            line = reader.readline()
            if not line:
                break
            lineparts = line.split(",")
            if lineparts[0] == name:
                break
    
    if line != "":
        print(line)
    else:
        print("Sorry, the student for which you have searched could not be found.")

def main():
    continuing = "y"
    while continuing == "y":
        if functionofcode() == False:
            print("Program closing...")
            exit(0)
        else:
            continuing = continuechoice()
            
def continuechoice():
    choice = ""
    attempts = 3
    while choice != "y" and choice != "n" and attempts > 0:
        choice = input("Would you like to perform another operation in the program? y/n\n").lower()
    
    if choice != "y" and choice != "n":
        choice = "n"
    return choice
               

def functionofcode():
    validchoices = ["find", "add", "display"]
    print("In this program, you can:\nAdd a student's information- 'add'\nDisplay the information of all students- 'display'\nFind a specific student in the data- 'find'")
    attempts = 3
    choice = ""
    while choice not in validchoices and attempts > 0:
        choice = input("What would you like to do?\n").lower()
        attempts -= 1
    
    if choice not in validchoices:
        print("An invalid choice was not entered, so the program will close.")
        return False
    
    match choice:
        case "display":
            display_students()
        case "find":
            name = input("What is the name of the student you are attempting to find?\n").title()
            find_student(name)
        case "add":
            name = input("What is the name of the student you would like to enter into the data set?\n").title()
            age = ""
            tries = 3
            while age == "" and tries > 0:
                ageinput = input("What is the age of the student you would like to enter into the data set?\n")
                age = validateage(ageinput)
                tries -= 1
            if age == "":
                print("An invalid age was entered, and so the program will close.")
                return False
            grade = ""
            gradeinput = ""
            tries = 3
            while grade == "" and tries > 0:
                gradeinput = input("What is the grade of the student?\n")
                grade = validategrade(gradeinput)
                tries -= 1
                
            if grade == "":
                print("An invalid grade was not entered, so the program will close.")
                return False
            
            add_student(name, age, grade)
    return True
            

def validateage(age):
    try:
        agenum = float(age)
    except ValueError:
        print("This is an invalid age to enter, as it is not numeric.")
        return ""
    else:
        if agenum < 0:
            print("This is an invalid age to enter, as it is negative.")
            return ""
        elif int(agenum) != agenum:
            print("This is an invalid age to enter, as it is a decimal value.")
            return ""
        else:
            return agenum
        
def validategrade(grade):
    try:
        gradenum = float(grade)
    except ValueError:
        print("This is an invalid grade to enter, as it is not numeric.")
        return ""
    else:
        if 0 <= gradenum <= 100:
            return gradenum
        else:
            print("This is an invalid grade as it is outside the boundaries of a grade's possible value.")
            return ""

if __name__ == "__main__":
    main()