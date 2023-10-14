''' File to be modified by Vali '''
import input_name
import input_age
import input_details
import util


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
    print(f"New student entering the club is: {student_name}, and s/he's {student_age} years old.")
    print(f"S/he is a student in {student_year_of_study} year of study in {student_field_of_study} field.")

if __name__ == "__main__":
    main()