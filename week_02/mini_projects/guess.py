'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''
import random
# Get random number inclusive of 1 to 100
x = random.randrange(1, 101)
# initialize y which will be used for user input of their guess.
guess = 0
while guess != x:
    print("Please enter a number between 1 and 100: ")
    guess = int(input())
print("You win!")
