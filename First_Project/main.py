''' File to be modified by Vali '''
import input_name
import input_age
import input_details
import util
import input_music_taste
import input_hobby

def main():
    """
    Main function of the project.
    Arguments: None
    Return: None
    """
    
    print("Hello to the Python Club")
    student_name = input_name.get_student_name()
    student_age = input_age.get_student_age()
    student_year_of_study = input_details.get_year_of_study()
    student_field_of_study = input_details.get_field_of_study()
    student_hobby=input_hobby.get_student_hobby()
    student_music_taste=input_music_taste.get_student_music_taste()
    ordinal_ind="th"
    if(student_year_of_study==1):
        ordinal_ind="st"
    elif(student_year_of_study==2):
        ordinal_ind="nd"
    elif(student_year_of_study==3):
        ordinal_ind="rd" 
    print(f"New student entering the club is: {student_name}, and she/he's {student_age} years old.")
    print(f"She/He is a student in {student_year_of_study}{ordinal_ind} year of study in {student_field_of_study} field.")
    print (f"She/He loves to {student_hobby} and usualy listens to {student_music_taste} music.")

if __name__ == "__main__":
    main()