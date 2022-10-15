# File to be modified by Alex

def get_student_name():
    """Function that asks the user to type the name of a student and return the name with first letter in each name as Upper case.
    The function should return a valid name that contains only charactes and has a maximun of 30 characters.
    Argument: None
    Return: a string
    """
    name = str(input("What's your name?: "))
    lastName = str(input("What's your last name?: "))
    firstLetterOfTheName = name[0]
    firstLetterOfTheLastName = lastName[0]

    print(firstLetterOfTheName.upper()+ " " + firstLetterOfTheLastName.upper())

    # return "John Doe"

    return firstLetterOfTheName + " " + firstLetterOfTheLastName

get_student_name()