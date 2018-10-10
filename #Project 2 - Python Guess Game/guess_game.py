# GUESS GAME

import random
import time

guess_number = random.randint(1,20)
numberOfGuesses = 6

while True:

    myGuess = int(input("Take a guess between 1 and 20 : \n"))

    if numberOfGuesses != 0:
        if myGuess > guess_number:
            print("Guess is too high")
            numberOfGuesses -= 1

        elif myGuess < guess_number:
            print("Guess is too low")
            numberOfGuesses -= 1

        elif myGuess == guess_number:
            print("You guessed it!")
            break

        else:
            print("Incorrect Value")

    else:
        print("No more guesses left")
        break

time.sleep(60)
