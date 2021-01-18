# Write a Guess the Number game that has three levels of
# difficulty. The first level of difficulty would be a number
# between 1 and 10. The second difficulty set would be
# between 1 and 100. The third difficulty set would be between
# 1 and 1000.
# Prompt for the difficulty level, and then start the game. The
# computer picks a random numberin thatrange and prompts
# the player to guess that number. Each time the player
# guesses, the computer should give the player a hint as to
# whether the number is too high or too low. The computer
# should also keep track of the number of guesses. Once the
# player guesses the correct number, the computer should
# present the number of guesses and ask if the player would
# like to play again.
# 
# Example Output
# Let's play Guess the Number.
# Pick a difficulty level (1, 2, or 3): 1
# I have my number. What's your guess? 1
# Too low. Guess again: 5
# Too high. Guess again: 2
# You got it in 3 guesses!
# Play again? n
# Goodbye!
# 
# Constraints
# • Don’t allow any non-numeric data entry.
# • During the game, count non-numeric entries as wrong
# guesses.

import random

repeat = True
while repeat:

    print("Let's play Guess the Number.")

    while True:
        try:
            difficulty = int(input("Pick a difficulty level (1, 2, or 3): "))
            if difficulty == 1:
                number = random.randint(1,10)
                break
            elif difficulty == 2:
                number = random.randint(1,100)
                break
            elif difficulty == 3:
                number = random.randint(1,1000)
                break
            else:
                print("Enter a valid difficulty")
        except ValueError:
            print("Enter a valid difficulty")

    attemps = 0
    while True:
        attemps += 1
        try:
            guess = int(input("I have my number. What's your guess? "))    
            break
        except ValueError:
            print("Enter a valid number")

    while True:
        if guess > number:
            attemps += 1
            try:
                guess = int(input("Too high. Guess again: "))
            except ValueError:
                print("Enter a valid number")

        elif guess < number:
            attemps += 1
            try:
                guess = int(input("Too low. Guess again: "))
            except ValueError:
                print("Enter a valid number")

        else:
            print("You got it in " + str(attemps) + " guesses!")
            break

    while True:
        again = input("Play again? ")

        if again.upper() == "YES" or again.upper() == "Y" :
            repeat = True
            break
        elif again.upper() == "NO" or again.upper() == "N":
            repeat = False
            break
        else:
            print("Enter a valid answer")




