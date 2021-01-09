# More complex programs may have decisions nested in other
# decisions, so that when one decision is made, additional
# decisions must be made.
# Create a tax calculator that handles multiple states and
# multiple counties within each state. The program prompts
# the user for the order amount and the state where the order
# will be shipped.
# For Wisconsin residents, prompt forthe county ofresidence.
# • For Eau Claire county residents, add an additional 0.005
# tax.
# • For Dunn county residents, add an additional 0.004 tax.
# Illinois residents must be charged 8% sales tax with no
# additional county-level charge. All other states are not
# charged tax. The program then displays the tax and the total
# for Wisconsin and Illinois residents but just the total for
# everyone else.
# 
# Example Output
# What is the order amount? 10
# What state do you live in? Wisconsin
# The tax is $0.50.
# The total is $10.50.
# 
# Constraints
# • Ensure that all money is rounded up to the nearest cent.
# • Use a single output statement at the end of the program
# to display the program results.

amount = input("What is the order amount? ")
state = input("What is the state do you live in? ")

if state.upper() == "WISCONSIN":
    county = input("In which county do you live in? ")
    if county.upper() == "EAU CLAIRE":
        tax =  0.05
    elif county.upper() == "DUNN":
        tax =  0.04
    else:
        tax = 0
elif state.upper() == "ILLINOIS": 
    tax =  0.08
else:
    tax = 0

total = round(float(amount) + ((float(amount)*tax)/100), 2)

if  tax != 0:
    mensaje = "The tax is $" + str(tax) +   '\n' +  "The total is $"+ str(total)
else:
    mensaje = "The total is $"+ str(total)

print(mensaje)