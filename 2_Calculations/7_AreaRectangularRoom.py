# When working in a global environment, you’ll have to
# present information in both metric and Imperial units. And
# you’ll need to know when to do the conversion to ensure
# the most accurate results.
# Create a program that calculates the area of a room. Prompt
# the user for the length and width of the room in feet. Then
# display the area in both square feet and square meters.
# 
# Example Output
# What is the length of the room in feet? 15
# What is the width of the room in feet? 20
# You entered dimensions of 15 feet by 20 feet.
# The area is
# 300 square feet
# 27.871 square meters
# The formula for this conversion is
# m^2 = f^2 × 0.09290304
# 
# Constraints
# • Keep the calculations separate from the output.
# • Use a constant to hold the conversion factor.

FACTOR = 0.09290304

f_height = input("What is the length of the room in feet? ")
f_width = input("What is the width of the room in feet? ")

print("You entered dimensions of " + f_height+ " feet by " + f_width + " feet. ")

f_area = int(f_height) * int(f_width)

m_area = f_area * FACTOR

print("The area is ")
print( str(f_area) + " square feet")
print( str(m_area) + " square meters") 


