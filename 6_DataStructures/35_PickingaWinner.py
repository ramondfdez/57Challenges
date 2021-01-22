# Arrays don’t have to be hard-coded. You can take userinput
# and store it in an array and then work with it.
# Create a program that picks a winner for a contest or prize
# drawing. Prompt for names of contestants until the user
# leaves the entry blank. Then randomly select a winner.
# 
# Example Output
# Enter a name: Homer
# Enter a name: Bart
# Enter a name: Maggie
# Enter a name: Lisa
# Enter a name: Moe
# Enter a name:
# The winner is... Maggie.
# 
# Constraints
# • Use a loop to capture user input into an array.
# • Use a random number generator to pluck a value from
# the array.
# • Don’t include a blank entry in the array.
# • Some languages require that you define the length of
# the array ahead of time. You may need to find another
# data structure, like an ArrayList.
import random

nombres = []
while True:
    nombre = input("Enter a name: ")
    if nombre != "":
        nombres.append(nombre)
    else:
        break

index = random.randint(0, len(nombres)-1)
print("The winner is: " + nombres[index])