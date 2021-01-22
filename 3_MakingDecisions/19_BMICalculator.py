# You’ll often need to see if one value is within a certain range
# and alter the flow of a program as a result.
# Create a program to calculate the body mass index (BMI)
# for a person using the person’s height in inches and weight
# in pounds. The program should prompt the user for weight
# and height.
# Calculate the BMI by using the following formula:
# bmi = (weight / (height × height))* 703
# If the BMI is between 18.5 and 25, display that the person is
# at a normal weight. If they are out of that range, tell them if
# they are underweight or overweight and tell them to consult
# their doctor.
# 
# Example Output
# Your BMI is 19.5.
# You are within the ideal weight range.
# or
# Your BMI is 32.5.
# You are overweight. You should see your doctor.
# 
# Constraint
# • Ensure your program takes only numeric data. Don’t
# let the user continue unless the data is valid.

while 1:
    try:

        weight = float(input("What is your weigth in pounds? "))
        height = float(input("What is your height in inches? "))
        break
    except ValueError:
        print('You have to enter numeric values')

bmi = ((weight/(height*height))*703)

if bmi < 18.5:
    print("You are underweight. You should see your doctor. ")
elif bmi > 25:
    print("You are overweight. You should see your doctor. ")
else:
    print("You are within the ideal weight range. ")
