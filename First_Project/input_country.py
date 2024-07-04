''' File to be modified by Newbie 5 '''

def get_student_country():
    '''
    Function that asks the user which country they are from.
    The function should return a valid string that contains only letters and has a maximum length of 20 characters.
    Argument: None
    Return: String
    '''
    while True:
        country = input()
        if country.isalpha() and len(country) <= 20:
            return country
        else:
            print("Error")



print(get_student_country())
