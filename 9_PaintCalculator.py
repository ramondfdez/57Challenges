# Sometimes you have to round up to the next number rather
# than follow standard rounding rules.
# Calculate gallons of paint needed to paint the ceiling of a
# room. Prompt for the length and width, and assume one
# gallon covers 350 square feet. Display the number of gallons
# needed to paint the ceiling as a whole number.
# 
# Example Output
# You will need to purchase 2 gallons of
# paint to cover 360 square feet.
# Remember, you can’t buy a partial gallon of paint. You must
# round up to the next whole gallon.
# 
# Constraints
# • Use a constant to hold the conversion rate.
# • Ensure that you round up to the next whole number.

import math 

FACTOR = 350

length = input("What is the length of the room in feet? ")
width = input("What is the width of the room in feet? ")

square_feet = int(length) * int(width) 

gallons = math.ceil(square_feet / FACTOR)

print("You will need to purchase " + str(gallons) + " gallons of paint to cover " + str(square_feet) + " square feet." )
