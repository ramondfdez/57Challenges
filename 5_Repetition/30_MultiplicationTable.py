# Create a program that generates multiplication tables for
# the numbers 0 through 12.
# 
# Example Output
# 0 X 0 = 0
# 0 X 1 = 0
# ....
# 12 x 11 = 132
# 12 x 12 = 144
# 
# Constraint
# • Use a nested loop to complete this program.

numbers = list(range(0,13))

for i in numbers:
    for j in numbers:
        print(str(i) + "x" + str(j) + " = " + str(i*j) )

