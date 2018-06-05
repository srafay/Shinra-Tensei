# Make a single player Rock Paper Scissors game

# RULES
    # Rock beats scissors
    # Scissors beats paper
    # Paper beats rock

import random

options = ["Rock", "Scissor", "Paper"]

while (1):
    computerPlay = random.choice(options)

    print("\n*Computer has chosen it's option, now it's your turn*\n")
    humanPlay = input("Enter your choice: ")

    if ( humanPlay == computerPlay):
        print("Game Draw, computer chose {}" .format(computerPlay))
        
    elif (humanPlay == "Rock" and computerPlay == "Scissor"):
        print("You win, computer chose {}" .format(computerPlay))
    elif (humanPlay == "Scissor" and computerPlay == "Paper"):
        print("You win, computer chose {}" .format(computerPlay))
    elif (humanPlay == "Paper" and computerPlay == "Rock"):
        print("You win, computer chose {}" .format(computerPlay))
    else:
        print("Computer chose {}, you loose" .format(computerPlay))
