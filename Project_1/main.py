"""File to be modified by Timotei -> Make it nice and print the details as you want.
Delete me (the comment when done)"""

def main():
    """Main function of the project.
    Arguments: None
    Return: None
    """
    print("Hello to the Python Club")
    student_name = get_student_name()
    student_age = get_student_age()
    student_year_of_study = get_year_of_study()
    student_field_of_study = get_field_of_study()
    print(f"New student entering the club is: {student_name}, and he's {student_age} years old.")
    print(f"He is a student in {student_year_of_study} year of study in {student_field_of_study} field.")


main()