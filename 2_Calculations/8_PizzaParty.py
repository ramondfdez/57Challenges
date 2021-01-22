# Division isn’t always exact, and sometimes you’ll write
# programs that will need to deal with the leftovers as a whole
# number instead of a decimal.
# Write a program to evenly divide pizzas. Prompt for the
# number of people, the number of pizzas, and the number of
# slices per pizza. Ensure that the number of pieces comes out
# even. Display the number of pieces of pizza each person
# should get. If there are leftovers, show the number of leftover
# pieces.
# 
# Example Output
# How many people? 8
# How many pizzas do you have? 2
# 8 people with 2 pizzas
# Each person gets 2 pieces of pizza.
# There are 0 leftover pieces.

import math

people = input("How many people? ")
pizzas = input("How many pizzas do you have? ")
slices_per_pizza = input("How many slices per pizza? ")

print( people + " people with " + pizzas + " pizzas")

slices = int(pizzas) * int(slices_per_pizza)
slice_per_person = math.floor(int(slices) / int(people))
rest = slices % slice_per_person

print("Each person gets " + str(slice_per_person) + " pieces of pizza. ")
print("There are " + str(rest) + " leftover pieces. ")