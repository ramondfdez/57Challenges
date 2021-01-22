# Write a program that prompts for response times from a
# website in milliseconds. It should keep asking for values
# until the user enters “done.”
# The program should print the average time (mean), the
# minimum time, the maximum time, and the standard deviation.
# To compute the average (mean)
# 1. Compute the sum of all values.
# 2. Divide the sum by the number of values.
# To compute the standard deviation
# 1. Calculate the difference from the mean for each number
# and square it.
# 2. Compute the mean of the squared values.
# 3. Take the square root of the mean.
# 
# Example Output
# Enter a number: 100
# Enter a number: 200
# Enter a number: 1000
# Enter a number: 300
# Enter a number: done
# Numbers: 100, 200, 1000, 300
# The average is 400.
# The minimum is 100.
# The maximum is 1000.
# The standard deviation is 400.25.
# 
# Constraints
# • Use loops and arrays to perform the input and mathematical operations.
# • Be sure to exclude the “done” entry from the array of
# inputs.
# • Be sure to properly convert numeric values to strings.
# • Keep the input separate from the processing and the
# output.
import math

def media(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma/len(lista)

def minimo(lista):
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo

def maximo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

def desviacion(lista):
    lista2 = []
    for numero in lista:
        msqr = math.pow(numero-media(lista), 2)
        lista2.append(msqr) 
    media2 = media(lista2)
    return math.sqrt(media2)

numbers = []
msg = "Numbers: "
while True:
    number = input("Enter a number: ")
    if number != "done":
        numbers.append(int(number))
    else:
        break
for number in numbers:
    msg = msg + str(number) + ", "
    
print(msg)
print("The average is " + str(media(numbers)))
print("The minimun is " + str(minimo(numbers)))
print("The maximun is " + str(maximo(numbers)))
print("The standard deviation is " + str(desviacion(numbers)))