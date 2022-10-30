# File to be modified by Andreea

from Project_1.util import DEBUG
import main
import util

def get_student_age():
    """Function that asks the user to type the age of a student and return the age as numerical value.
    The function should return a valid age that contains only numbers and has a maximum value of 99.
    Argument: None
    Return: a numerical value
    """
    
    while True:
        try :
            student_age = int(input("Insert your age please (must be a numerical value between 0 and 99) : "))
            break
        except:
            print("You must enter a valid number ( 0-99)")
    
    if student_age in range(1,98):
        if DEBUG:
            print(student_age)
        return student_age
    else:
        print("You must enter a valid number ( 0-99)")
        get_student_age()

