# You’ll often need to determine which part of a program is
# run based on user input or other events.
# Create a program that converts temperatures from Fahrenheit to Celsius or from Celsius to Fahrenheit. Prompt for the
# starting temperature. The program should prompt for the
# type of conversion and then perform the conversion.
# The formulas are
# C = (F − 32) × 5 / 9
# and
# F = (C × 9 / 5) + 32
# 
# Example Output
# Press C to convert from Fahrenheit to Celsius.
# Press F to convert from Celsius to Fahrenheit.
# Your choice: C
# Please enter the temperature in Fahrenheit: 32
# The temperature in Celsius is 0.
# 
# Constraints
# • Ensure that you allow upper or lowercase values for C
# and F.
# • Use as few output statements as possible and avoid
# repeating output strings.

print("Press C to convert from Fahrenheit to Celsius.")
print("Press F to convert from Celsius to Fahrenheit.")
choice = input("Your choice: ")

if (choice.upper() == 'C'):
    temperature = float(input("Please enter the temperature in Fahrenheit: "))
    unit = "Celsius"
    res  = (temperature-32) * (5/9)


elif (choice.upper() == 'F'):
    temperature = float(input("Please enter the temperature in Celsius: "))
    unit = "Fahrenheit"
    res = (temperature * (9/5)) + 32

else:
    print("Only C and F are valid")

print("The temperature in " + unit + " is " + str(round(res,2))) 