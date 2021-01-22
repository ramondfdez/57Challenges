# Sometimes you have to perform a more complex calculation
# based on some provided inputs and then use that result to
# make a determination.
# Create a program that prompts for your weight, gender,
# number of drinks, the amount of alcohol by volume of the
# drinks consumed, and the amount of time since your last
# drink. Calculate your blood alcohol content (BAC) using this
# formula
# BAC = (A × 5.14 / W × r) − .015 × H
# where
# • A is total alcohol consumed, in ounces (oz).
# • W is body weight in pounds.
# • r is the alcohol distribution ratio:
# – 0.73 for men
# – 0.66 for women
# • H is number of hours since the last drink.
# Display whether or not it’s legal to drive by comparing the
# blood alcohol content to 0.08.
# 
# Example Output
# Your BAC is 0.08
# It is not legal for you to drive.
# 
# Constraint
# • Prevent the user from entering non-numeric values.

while 1:
    try:

        weight = float(input("What is your weigth? "))
        gender = input("What is your gender? ")
        n_drinks = int(input("What is the number of drinks? "))
        amount_alcohol = int(input("What is the amount of alcohol? "))
        time = int(input("What is the amount of time since your last drink? "))
        break
    except ValueError:
        print('You have to enter numeric values')


if (gender.upper() == "MAN" or gender.upper() == "M" or gender.upper() == "MALE"):
    ratio = 0.73
elif(gender.upper() == "WOMAN" or gender.upper() == "F"or gender.upper() == "FEMALE"):
    ratio = 0.66
else:
    print('Enter a valid gender')


bac = round(((amount_alcohol * 5.14) / (weight * ratio)) - (0.015 * time), 2)

if bac <= 0.08:
    print("Your BAC is " + str(bac))
    print("It's legal for you to drive")
else:
    print("Your BAC is " + str(bac))
    print("It's not legal for you to drive")