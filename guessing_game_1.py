# Generate a random number between 1 and 9 (including 1 and 9)
# Ask the user to guess the number, then tell them whether
# they guessed too low, too high, or exactly right

from random import randint

number = randint(1, 9)
userNumber = input( "Enter a number [1-9]: " )

numberOfAttempts = 0

while(userNumber != "exit"):
    if ( number - int(userNumber) > 0 ):
        print("Too low")
    elif (number - int(userNumber) < 0):
        print("Too high")
    else:
        print("Correct guess")
        numberOfAttempts += 1
        break
    numberOfAttempts += 1
    userNumber = input( "Enter a number [1-9]: " )

print("Total number of attempts: {}" .format(numberOfAttempts))
