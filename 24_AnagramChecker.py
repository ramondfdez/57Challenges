# Using functions to abstract the logic away from the rest of
# your code makes it easier to read and easier to maintain.
# Create a program that compares two strings and determines
# if the two strings are anagrams. The program should prompt
# for both input strings and display the output as shown in
# the example that follows.
# 
# Example Output
# Enter two strings and I'll tell you if they
# are anagrams:
# Enter the first string: note
# Enter the second string: tone
# "note" and "tone" are anagrams.
# 
# Constraints
# • Implement the program using a function called isAnagram, which takes in two words as its arguments and
# returns true orfalse. Invoke this function from your main
# program.
# • Check that both words are the same length.

print("Enter two strings and I'll tell you if they are anagrams: ")
first = input("Enter the first string: ")
second = input("Enter the second string: ")

def myAnagram(a,b):
    if (len(a) == len(b)):
        cont = 0
        for letra in a:
            if letra in b:
                cont = cont + 1
            else:
                return False
        return cont == len(b)
    else:
        return False

if(myAnagram(first,second)):
    print(first + " and " + second + " are anagrams" )
else:
    print(first + " and " + second + " are not anagrams" )