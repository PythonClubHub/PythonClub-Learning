#File to be modified by Andrei
from Project_1.util import debug_print

def get_year_of_study():
    """Function that asks the user to type the year of study of a student and return the year of study as numerical value.
    The function should return a valid study year that contains only numbers and has a maximun value of 4.
    Argument: None
    Return: a numerical value
    """
    valid_student_year_of_study = True

    while valid_student_year_of_study is True :
        try:
            student_year_of_study = int(input("What year of study are you in?(only numbers 1-4)"))
        except:
            print("You either entered a number outside the range , 1-4, or a literal character")
            continue
        
        if student_year_of_study in range(1,5):
            debug_print()
            valid_student_year_of_study = False
            break
        else:
            print("You either entered a number outside the range , 1-4, or a literal character")
    
    return student_year_of_study


def get_field_of_study():
    """Function that asks the user to type the field of study for a student and return the name with Upper case for all letters.
    The function should return a valid name for the field that contains only charactes and has a maximun of 30 characters.
    Argument: None
    Return: a string
    """
    return "EM"

if __name__ == "__main__":
    get_year_of_study()