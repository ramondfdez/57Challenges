# Sometimes input you collect will need to be filtered down.
# Data structures and loops can make this process easier.
# Create a program that prompts for a list of numbers, separated by spaces. Have the program print out a new list containing only the even numbers.
# 
# Example Output
# Enter a list of numbers, separated by spaces: 1 2 3 4 5 6 7 8
# The even numbers are 2 4 6 8.
# 
# Constraints
# • Convert the input to an array. Many languages can
# easily convert strings to arrays with a built-in function
# that splits apart a string based on a specified delimiter.
# • Write your own algorithm—don’trely on the language’s
# built-in filter or similar enumeration feature.
# • Use a function called filterEvenNumbers to encapsulate the
# logic for this. The function takes in the old array and
# returns the new array.

def filterEvenNumbers(lista):
    pares = []
    for i in lista:
        if (int(i) % 2) == 0:
            pares.append(i)
    return pares


entrada = input("Enter a list of numbers, separated by spaces: ")

numeros = list(entrada.split(" "))

lista = filterEvenNumbers(numeros)

salida = ' '.join(lista)

print("The even numbers are " + salida)

