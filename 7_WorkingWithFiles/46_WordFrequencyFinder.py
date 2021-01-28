# Knowing how often a word appears in a sentence or block
# of text is helpful for creating word clouds and other types
# of word analysis. And it’s more useful when running it
# against lots of text.
# Create a program thatreads in a file and counts the frequency of words in the file. Then construct a histogram displaying
# the words and the frequency, and display the histogram to
# the screen.
# 
# Example Output
# Given the text file words.txt with this content
# badger badger badger badger mushroom mushroom
# snake badger badger badger
# the program would produce the following output:
# badger: *******
# mushroom: **
# snake: *
# 
# Constraint
# • Ensure that the most used word is at the top of the report
# and the least used words are at the bottom.

file = open("Files/words.txt")

def  buscar (palabra, lista):
    cont = 0
    for i in lista:
        if i == palabra:
            return cont
        else:
            cont += 1
    return -1

text = file.read()
lista = text.split(" ")

cont = 0

for palabra in lista:
    encontrado = buscar(palabra, lista) 
    while( encontrado!= -1):
        lista.pop(encontrado)
        cont += 1
        encontrado = buscar(palabra, lista) 
    print( palabra + ": " + str(cont))
    cont = 0