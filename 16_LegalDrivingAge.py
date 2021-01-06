# You can test for equality, but you may need to test to see
# how a number compares to a known value and display a
# message if the number is too low or too high.
# Write a program that asks the userfortheir age and compare
# it to the legal driving age of sixteen. If the user is sixteen or
# older, then the program should display “You are old enough
# to legally drive.” If the user is under sixteen, the program
# should display “You are not old enough to legally drive.”
# 
# Example Output
# What is your age? 15
# You are not old enough to legally drive.
# Or
# What is your age? 35
# You are old enough to legally drive.
# 
# Constraints
# • Use a single output statement.
# • Use a ternary operator to write this program. If your
# language doesn’t support a ternary operator, use a regular if/else statement, and still use a single output statement to display the message.

LEGAL_AGE = 18

age = input("What is your age? ")

mensaje = "You are not old enough to legally drive." if int(age) < LEGAL_AGE else "You are old enough to legally drive."

print(mensaje)