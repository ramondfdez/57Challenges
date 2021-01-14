# Large functions aren’t very usable or maintainable. It makes
# a lot of sense to break down the logic of a program into
# smaller functions that do one thing each. The program can
# then call these functions in sequence to perform the work.
# Write a program that prompts for a first name, last name,
# employee ID, and ZIP code. Ensure that the input is valid
# according to these rules:
# • The first name must be filled in.
# • The last name must be filled in.
# • The first and last names must be at least two characters
# long.
# • An employee ID is in the format AA-1234. So, two letters, a hyphen, and four numbers.
# • The ZIP code must be a number.
# Display appropriate error messages on incorrect data.
# 
# Example Output
# Enter the first name: J
# Enter the last name:
# Enter the ZIP code: ABCDE
# Enter an employee ID: A12-1234
# "J" is not a valid first name. It is too short.
# The last name must be filled in.
# The ZIP code must be numeric.
# A12-1234 is not a valid ID.
# Or
# Enter the first name: Jimmy
# Enter the last name: James
# Enter the ZIP code: 55555
# Enter an employee ID: TK-421
# There were no errors found.
# 
# Constraints
# • Create a function for each type of validation you need
# to write. Then create a validateInput function that takes
# in all of the input data and invokes the specific validation functions.
# • Use a single output statement to display the outputs.

def validateName(first_name):
        if first_name == "":
            return -1
        else:
            if len(first_name) < 2:
                return 0
            else:
                return 1

def validate_zip_code(zip_code):
    if zip_code == "":
        return -1
    else:
        if zip_code.isdigit() == True:
            return 1
        else:
            return 0


def validate_employee_id(emp_id):
    if emp_id == "":
        return -1
    else:
        if (
            len(emp_id) == 7
            and emp_id[0:1].isalpha()
            and emp_id[2] == "-"
            and emp_id[3:-1].isdigit()
        ):
            return 1
        else:
            return 0

def validateInput(first_name, last_name, zip_code, emp_id):
    if validateName(first_name) == -1:
        print("The first name must be filled in.")
    elif validateName(first_name) == 0:
        print(first_name + " is not a valid first name. It is too short. ")
    if validateName(last_name) == -1:
        print("The first name must be filled in.")
    elif validateName(last_name) == 0:
        print(last_name + " is not a valid last name. It is too short. ")
    if validate_zip_code(zip_code) == -1:
        print("The zip code must be filled in. ")
    elif validate_zip_code(zip_code) == 0:
        print("The ZIP code must be numeric. ")
    if validate_employee_id(emp_id) == -1:
        print( "The employee id must be filled in. ")
    elif validate_employee_id(emp_id) == 0:
        print(emp_id + "is not a valid ID.")

    return 

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
zip_code = input("Enter the zip code: ")
emp_id = input("Enter an employee ID: ")


validateInput(first_name, last_name, zip_code, emp_id)