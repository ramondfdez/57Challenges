# Comparing one input to a known value is common enough,
# but you’ll often need to process a collection of inputs.
# Write a program that asks for three numbers. Check first to
# see that all numbers are different. If they’re not different,
# then exit the program. Otherwise, display the largest number
# of the three.
# 
# Example Output
# Enter the first number: 1
# Enter the second number: 51
# Enter the third number: 2
# The largest number is 51.
# 
# Constraint
# • Write the algorithm manually. Don’t use a built-in
# function for finding the largest number in a list.

first = input("Input the first number: ")
second = input("Input the second number: ")
third = input("Input the third number: ")

def check(a,b,c):
    if (a == b) or (a == c) or (b == c):
        return False
    else:
        return True
        
def greater(a,b,c):
    if(a > b):
        mayor = a
    else:
        mayor = b
    if mayor > c:
        return mayor
    else:
        return c
        
if(check(first,second,third)):
    print("The largest number is " + str(greater(first,second,third)))

else:
    print("Some numbers are equal. Please, enter different numbers.")


