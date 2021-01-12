# Functions help you abstract away complex operations, but
# they also help you build reusable components.
# Create a program that determines the complexity of a given
# password based on these rules:
# • A very weak password contains only numbers and is
# fewer than eight characters.
# • A weak password contains only letters and is fewerthan
# eight characters.
# • A strong password contains letters and at least one
# number and is at least eight characters.
# • A very strong password contains letters, numbers, and
# special characters and is at least eight characters.
# 
# Example Output
# The password '12345' is a very weak password.
# The password 'abcdef' is a weak password.
# The password 'abc123xyz' is a strong password.
# The password '1337h@xor!' is a very strong password.
# 
# Constraints
# • Create a passwordValidator function that takes in the
# password as its argument and returns a value you can
# evaluate to determine the password strength. Do not
# have the function return a string—you may need to
# support multiple languages in the future.
# • Use a single output statement.


def passwordValidator(password):
    if len(password) < 8:
        if password.isdigit():
            return 0
        elif password.isalpha():
            return 1
        else:
            return 2
    else:
        if password.isdigit() or password.isalpha():
            return 2
        elif password.isalnum():
            return 3
        else:
            return 4


password = input("What is your password? ")

level = passwordValidator(password)

if level == 0:
    print("The password \'" + password + "\' is a very weak password.")
elif level == 1:
    print("The password \'" + password + "\' is a weak password.")
elif level == 2:
    print("The password \'" + password + "\' is a normal password.")
elif level == 3:
    print("The password \'" + password + "\' is a strong password.")
elif level == 4:
    print("The password \'" + password + "\' is a very strong password.")
else:
    print("ERROR")