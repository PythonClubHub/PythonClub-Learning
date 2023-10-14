''' File to be modified by Andreea Stef '''
from util import *

def get_student_age():
    """Function that asks the user to type the age of a student and return the age as numerical value.
    The function should return a valid age that contains only numbers and has a maximum value of 99.
    Argument: None
    Return: a numerical value
    """

    valid_student_age = True
    
    while valid_student_age == True:
        try :
            student_age = int(input("Insert your age please (must be a numerical value between 0 and 99) : "))
        except:
            print("You must enter a valid number ( 0-99)")
            continue
    
        if student_age in range(0,99):
            valid_student_age = False 
            debug_print()
        else:
            print("You must enter a valid number ( 0-99)")
    
    return student_age

if __name__ == "__main__":
    get_student_age()

