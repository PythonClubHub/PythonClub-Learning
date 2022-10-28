# File to be modified by Alex


def get_student_name():
    """Function that asks the user to type the name of a student and return the name with first letter in each name as Upper case.
    The function should return a valid name that contains only charactes and has a maximun of 30 characters.
    Argument: None
    Return: a string
    """
    name = str(input("What's your name?: "))
    lastName = str(input("What's your last name?: "))

    name_user = name[:15]
    lastName_user = lastName[:15]

    validation_name = name_user.isalpha()
    validation_lastName = lastName_user.isalpha()

    while(validation_name == False):
        print("Ati tastat un nume gresit, va rog sa folositi doar litere")
        name = str(input("What's your name?: "))
        name_user = name[:15]
    
    while(validation_lastName == False):
        print("Ati tastat un prenume gresit, va rog sa folositi doar litere")
        lastName = str(input("What's your last name?: "))
        lastName_user = lastName[:15]

    # return "John Doe"

    print(name_user.capitalize() + " " + lastName_user.capitalize())
    return name.capitalize() + " " + lastName.capitalize()


get_student_name()