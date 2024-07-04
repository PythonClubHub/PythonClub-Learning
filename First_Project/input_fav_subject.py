''' File to be modified by Newbie 4 '''

import re

def get_student_favourite_subject():
    '''
    Function that asks the user to type their favourite subject and return it as string value.
    The function should return a valid string that contains only charactes and has a maximum of 20 characters.
    Argument: None
    Return: String
    '''


    while True:

        favoriteSubject=input('Input your favorite subject: ')
        isToLong=len(favoriteSubject)
        hasNumbers=re.search('[0-9]',favoriteSubject)

        if isToLong>20:
            print("Input to long, it shoud have no more than 20 characters!\n")

        elif hasNumbers:
            print("Input has numbers1, please enter only characters!\n")
        
        else:
             return favoriteSubject
        
        

if __name__=='__main__':
    get_student_favourite_subject()
