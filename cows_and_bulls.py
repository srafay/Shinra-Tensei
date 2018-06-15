# Create a program that will play the “cows and bulls” game with the user
# If you are unsure of the game read https://en.wikipedia.org/wiki/Bulls_and_Cows

import random
import string

def cows_and_bulls(secretNum, guessedNum):
    cows = bulls = 0
    for i in range(len(guessedNum)):
        if guessedNum[i] == secretNum[i]:
            bulls += 1
        elif guessedNum[i] in secretNum:
            cows += 1
    return [cows, bulls]

# get a list of digits of length 4
secretNum = random.sample(string.digits, 4)
# convert the list into str and then into int
secretNum = ''.join(secretNum)

guessedNum = input("Guess the 4-digit number: ")

cows, bulls = cows_and_bulls(secretNum, guessedNum)

print ("Secret number: {}" .format(secretNum))
print ("You guessed : {}" .format(guessedNum))
print ("Cows: {}, Bulls: {} " .format(cows, bulls))
