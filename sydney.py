import random

# Initialize Variables
scoreValue = 300
keepPlaying = True
currentCard = random.randint(1, 13)


def playAgain():
    p = input("Play Again: [Y/N] ").upper()
    if p == "Y":
        keepPlaying = True
    else:
        keepPlaying = False

    return keepPlaying


def userGuess():
    user_Guess = input("Higher or Lower? [H/L] ").upper()
    return user_Guess


def nextCard():
    next_Card = random.randint(1, 13)
    return next_Card


def scoringSystem(cc, nc, ug, scoreValue):
    if ug == "H":
        if cc > nc:
            # user guess was correct, user gains points
            scoreValue = scoreValue - 75
            return scoreValue
        else:
            scoreValue = scoreValue + 100
            return scoreValue
    else:  # ug == "L"
        if cc > nc:
            # user guess was correct, user gains points
            scoreValue = scoreValue + 100
            return scoreValue
        else:
            scoreValue = scoreValue - 75
            return scoreValue


# Below is the main code were the program is running from within the while... loop
while keepPlaying == True:

    print()
    print()
    print(f"The Card is: {currentCard}")  # Display Current Card
    ug = userGuess()
    nc = nextCard()
    print(f"Next card was: {nc}")  # Displaying the random card
    # Calculates the score based on the provided info
    scoreValue = scoringSystem(currentCard, nc, ug, scoreValue)
    print(f"Your Score is: {scoreValue}")
    currentCard = nc  # The new random card becomes the next current
    print()
    if scoreValue > 0:
        keepPlaying = playAgain()
    else:
        keepPlaying = False

print("....The End....")
