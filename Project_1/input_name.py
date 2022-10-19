# File to be modified by Alex

def get_student_name():
    """Function that asks the user to type the name of a student and return the name with first letter in each name as Upper case.
    The function should return a valid name that contains only charactes and has a maximun of 30 characters.
    Argument: None
    Return: a string
    """
    name = str(input("What's your name?: "))
    lastName = str(input("What's your last name?: "))

    print(name.capitalize()+ " " + lastName.capitalize())

    # return "John Doe"

    return name.capitalize() + " " + lastName.capitalize()

get_student_name()