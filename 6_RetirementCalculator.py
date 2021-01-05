# Your computer knows what the current yearis, which means
# you can incorporate that into your programs. You just have
# to figure out how your programming language can provide
# you with that information.
# Create a program that determines how many years you have
# left until retirement and the year you can retire. It should
# prompt for your current age and the age you want to retire
# and display the output as shown in the example that follows.
# 
# Example Output
# What is your current age? 25
# At what age would you like to retire? 65
# You have 40 years left until you can retire.
# It's 2015, so you can retire in 2055.
# 
# Constraints
# • Again, be sure to convert the input to numerical data
# before doing any math.
# • Don’t hard-code the current year into your program.
# Get it from the system time via your programming language.

from datetime import date


edad_actual = input("What is your current age? ")
edad_jubilacion = input("At what age would you like to retire? ")

anos_restantes = int(edad_jubilacion) - int(edad_actual)
ano_actual = date.today().year

ano_jubilacion = ano_actual + anos_restantes

print("You have " + str(anos_restantes)  + " years until you can retire. ")
print("It's " + str(ano_actual)+ ", so you can retire in " + str(ano_jubilacion))