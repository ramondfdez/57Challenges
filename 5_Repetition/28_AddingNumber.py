# In previous programs, you asked the userforrepeated input
# by writing the input statements multiple times. But it’s more
# efficient to use loops to deal with repeated input.
# Write a program that prompts the userforfive numbers and
# computes the total of the numbers.
# 
# Example Output
# Enter a number: 1
# Enter a number: 2
# Enter a number: 3
# Enter a number: 4
# Enter a number: 5
# The total is 15.
# 
# Constraints
# • The prompting must use repetition, such as a counted
# loop, not three separate prompts.
# • Create a flowchart before writing the program.

cont = 0
suma = 0

while (cont < 5):
    number = int(input("Enter a number: "))
    suma = suma + number
    cont = cont + 1

print("The total is " + str(suma))


