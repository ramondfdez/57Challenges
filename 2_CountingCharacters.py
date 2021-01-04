# Create a program that prompts for an input string and displays output that shows the input string and the number of
# characters the string contains.
#
# Example Output
# What is the input string? Homer
# Homer has 5 characters.
#
# Constraints
# • Be sure the output contains the original string.
# • Use a single output statement to construct the output.
# • Use a built-in function of the programming language to
# determine the length of the string.

def contar_letras(palabra):
    i = 0;
    while (i < len(palabra)):
        i = i + 1;
    return i


palabra = input("What is the input string? ")
numero = contar_letras(palabra)
print(palabra + " has " + str(numero) + " characters.")