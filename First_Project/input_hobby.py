''' File to be modified by Mihai '''

import re

def get_student_hobby():
    '''
    Function that asks the user to type their hobby and return the hobby as string value.
    The function should return a valid string that contains only charactes and has a maximun of 20 characters.
    Argument: None
    Return: String
    '''
    Valid_Hobby=False

    while Valid_Hobby is False:
        Hobby=input("What is your hobby? (input only characters) ")
        Hobby=Hobby.lower()
        size_of_string = len(Hobby)
        has_symbols=re.findall("[!@#$%^&*()_+=]",Hobby)
        has_numbers=re.search("[0-9]",Hobby)
        has_space_at_start=re.match(" ",Hobby)
      

        if has_numbers or has_symbols or has_space_at_start:
            print ("You either entered a symbol,a number or only a space. Please try again!")

        elif size_of_string > 20 or size_of_string == 0 :
            print("You either entered more than 20 characters or entered nothing. Please meet these conditions! ")
              
        else:Valid_Hobby = True
        
    return Hobby

if __name__ == "__main__":
    get_student_hobby()
 