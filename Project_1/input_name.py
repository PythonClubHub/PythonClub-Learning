# File to be modified by Alex

from sre_constants import LITERAL_UNI_IGNORE


# name + last = maxim 30

# fiecare in parte oricat de lungi
# in caz ca sar de 30 vom taia din name iau pana la 30


# str = "test  "
# str = str.strip()

# print(len(str))

def get_student_name():
    """Function that asks the user to type the name of a student and return the name with first letter in each name as Upper case.
    The function should return a valid name that contains only charactes and has a maximun of 30 characters.
    Argument: None
    Return: a string
    """
    name = str(input("What's your name?: "))
    name = name.strip()
    validation_name = name.isalpha()
    
    # if(len(name) > 10):
    #     print('Too long')

    name_long = len(name)
    # print(name_long)

    while(validation_name == False):
        print("You texted a wrong name, please use only letters")
        name = str(input("What's your name?: "))
        validation_name = name.isalpha()
    
    lastName = str(input("What's your last name?: "))
    lastName = lastName.strip()
    validation_lastName = lastName.isalpha()

    lastName_long = len(lastName)
    # print(lastName_long)

    total_long = name_long + lastName_long

    # print("Avem in total " + str(total_long) + " characters")
    
    while(validation_lastName == False):
        print("You texted a wrong last name, please use only letters")
        lastName = str(input("What's your last name?: "))
        validation_lastName = lastName.isalpha()
        
    if(total_long > 30):
        print("Your name and last name are over 30 characters")
        print("It is possible the name will become short")

        # Here I calculated how many letters are over
        number_letters_over = total_long - 30

        # print("Am depasit cu " + str(number_letters_over) + " litere")

        # Here I calculated how many letters the name have to contain
        new_name_long = name_long - number_letters_over
        
        # print("Acum numele trebuie sa aiba " + str(new_name_long) + " litere")

        print(lastName.capitalize() + " " + name[0:new_name_long].capitalize())
        return lastName.capitalize() + " " + name[0:new_name_long].capitalize() 

    else:
        print(lastName.capitalize() + " " + name.capitalize())
        return lastName.capitalize() + " " + name.capitalize()

if __name__ == "__main__":
    get_student_name()