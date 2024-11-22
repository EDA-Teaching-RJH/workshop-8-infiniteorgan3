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
        # add

def functionofcode():
    validchoices = ["find", "add", "display"]
    print("In this program, you can:\nAdd a student's information- 'add'\nDisplay the information of all students- 'display'\nFind a specific student in the data- 'find'")
    attempts = 3
    while choice not in validchoices and attempts > 0:
        choice = input("What would you like to do?\n").lower()
    
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
            ageinput = input("What is the age of the student you would like to enter into the data set?\n")
            tries = 3
            while age == "" and tries > 0:
                age = validateage(ageinput)
            if age == "":
                print("An invalid age was entered, and so the program will close.")
                return False
            gradeinput = ""
            tries = 3
            while grade == "" and tries > 0
            grade = validategrade()
            
            add_student(name, age, grade)
            

def validateage(age):
    try:
        age = float(age)
    except ValueError:
        print("This is an invalid age to enter, as it is not numeric.")
        return ""
    else:
        if age < 0:
            print("This is an invalid age to enter, as it is negative.")
            return ""
        elif int(age) != age:
            print("This is an invalid age to enter, as it is a decimal value.")
        else:
            return age
        
def validategrade(grade):
    try:
        grade = float(grade)
    except ValueError:
        print("This is an invalid grade to enter, as it is not numeric.")
        return ""
    else:
        if 0 <= grade <= 100:
            return grade
        else:
            print("This is an invalid grade as it is outside the boundaries of a grade's possible value.")
            return ""