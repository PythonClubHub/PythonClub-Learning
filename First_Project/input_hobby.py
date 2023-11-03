''' File to be modified by Mihai '''

def get_student_hobby():
    '''
    Function that asks the user to type their hobby and return the hobby as string value.
    The function should return a valid string that contains only charactes and has a maximun of 20 characters.
    Argument: None
    Return: String
    '''
    Valid_Hobby=False

    while Valid_Hobby is False:
        Hobby=input("What are your hobbies? (input only characters) ")
        is_string=Hobby.isalpha()
        size_of_string = len(Hobby)

        if (is_string is True) and size_of_string > 0 and size_of_string <= 20 :
            Valid_Hobby = True
            return Hobby
        
        elif size_of_string > 20 or size_of_string == 0 :
            print("You either entered more than 20 characters or entered nothing. Please meet these conditions! ")

        else: print ("Please input only characters!")

get_student_hobby()
 