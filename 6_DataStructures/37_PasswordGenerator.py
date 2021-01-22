# Create a program that generates a secure password. Prompt
# the user for the minimum length, the number of special
# characters, and the number of numbers. Then generate a
# password for the user using those inputs.
# 
# Example Output
# What's the minimum length? 8
# How many special characters? 2
# How many numbers? 2
# Your password is
# aurn2$1s#
# 
# Constraints
# • Use lists to store the characters you’ll use to generate
# the passwords.
# • Add some randomness to the password generation.

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
sp_char = ['!','@','£','$','%','^','&','*','(',')','.','?']

def genera_password (min_len, size_sc, size_numbers):
    password = ""
    cont = 0
    sc = 0
    num = 0
    while (cont < min_len):
        while (sc < size_sc):
            password += random.choice(sp_char)
            sc += 1
            cont += 1
        while (num < size_numbers):
            password += random.choice(numbers)
            num += 1
            cont += 1

        password+= random.choice(letters)
        cont += 1
        l = list(password)
        random.shuffle(l)
        out = ''.join(l)
    return out


min_len = int(input("What's the minimum length? " ))
size_sc = int(input("How many special characters? " ))
size_numbers = int(input("How many numbers? " ))

print("Your password is:")
print(genera_password (min_len, size_sc,size_numbers))



