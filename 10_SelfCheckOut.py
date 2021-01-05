# Working with multiple inputs and currency can introduce
# some tricky precision issues.
# Create a simple self-checkout system. Prompt for the prices
# and quantities of three items. Calculate the subtotal of the
# items. Then calculate the tax using a tax rate of 5.5%. Print
# out the line items with the quantity and total, and then print
# out the subtotal, tax amount, and total.
# 
# Example Output
# Enter the price of item 1: 25
# Enter the quantity of item 1: 2
# Enter the price of item 2: 10
# Enter the quantity of item 2: 1
# Enter the price of item 3: 4
# Enter the quantity of item 3: 1
# Subtotal: $64.00
# Tax: $3.52
# Total: $67.52
# 
# Constraints
# • Keep the input, processing, and output parts of your
# program separate. Collect the input, then do the math
# operations and string building, and then print out the
# output.
# • Be sure you explicitly convert input to numerical data
# before doing any calculations.

TAX_RATE = 5.5

item1 = input("Enter the price of item 1: ")
quantity1 = input("Enter the quantity of item 1: ")
item2 = input("Enter the price of item 2: ")
quantity2 = input("Enter the quantity of item 2: ")
item3 = input("Enter the price of item 3: ")
quantity3 = input("Enter the quantity of item 3: ")

subtotal = float(item1) * float(quantity1) + float(item2) * float(quantity2) + float(item3) * float(quantity3)
tax = subtotal * TAX_RATE / 100
total = subtotal + tax

print("Subtotal: $" + str(subtotal))
print("Tax: $" + str(tax))
print("Total: $" + str(total))