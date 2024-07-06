''' File to be modified by Newbie 4 '''

def get_student_favourite_subject():
    '''
    Function that asks the user to type their favourite subject and return it as string value.
    The function should return a valid string that contains only charactes and has a maximum of 20 characters.
    Argument: None
    Return: String
    '''


    while True:

        favoriteSubject=input('Input your favorite subject: ')
        hasOnlyCharacters=favoriteSubject.isalpha()

        if not hasOnlyCharacters:
            print("Please enter only alphabetical characters\n")
        
        else:
             return favoriteSubject
        
        

if __name__=='__main__':
    get_student_favourite_subject()
