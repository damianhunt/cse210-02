from hilogame.cardmodule import Card


class Playing:

    """"
   A computer randomly select a  number from 1 to 13.
   A player should guess whether the next choice is either
   higher number or lower. The player control the game. Can choose
   to play or stop playing until score = 0.

   Attributes:
   ContinuePlaying (boolean): The value is supposed to be always True as long as the player is still playing or score is greater than zero
   score (int): The score starts as 300 and changes according to the users predicitions
   hilo (str): Users prediction which eithe be H for high or L for low
   theCard(): This is when an instance of the card class is created.
   currentcard (int): Hold the value of the current card
   nextcard (int): Holds the value of the next card that will be compared against currentcard
   play_Again (str): Determines if the user wants to continue playing if they still have a score greater than 1
"""

    def __init__(self):
        self.ContinuePlaying = True
        self.score = 300
        self.hilo = ""
        self.theCard = Card()
        self.currentCard = 0
        self.nextCard = 0
        self.play_Again = "Y"

    def scoringSystem(self):
        """
      This is the method responsible with calculating the new score by comparing the user prediction against the outcome from the Program
      A positive prediction will get a 100 added to the current score and wrong prediction the user losses 75 points
    """

        if self.hilo == "H":
            if self.currentCard < self.nextCard:
                self.score += 100
            else:
                self.score -= 75
        else:
            if self.currentCard > self.nextCard:
                self.score += 100
            else:
                self.score -= 75

        if self.score < 1:
            self.ContinuePlaying = False

        print(f"Your Score is {self.score}")

    def playAgain(self):
        """
    User will confirm with either a Y if they still want to play again or N if they dont want to continue playing

    """
        self.currentCard = self.nextCard  # Previous random card becomes the new current card
        self.play_Again = input("Play again? [y/n] ").upper()
        if self.play_Again != "Y":
            self.ContinuePlaying = False

    def userGuess(self):
        """
        User predictions is entered within this module
    """
        self.hilo = input("Higher or Lower? [h/l] ").upper()

    def startGame(self):
        """
        This is the main method responsible with the running of the game. All the other methods will be called within this module.
    """
        # This is only generated the first time the program starts working
        self.currentCard = self.theCard.drawCard()
        print()
        while self.ContinuePlaying:  # Loop continues running until score ContinuePlaying becomes False

            # Displays the current card
            print(f"The card is: {self.currentCard}")
            Playing.userGuess(self)  # Player enters their prediction

            # Computer generates the random card that will be compared against the current card.
            self.nextCard = self.theCard.drawCard()

            # The random card is displayed here
            print(f"The next card is {self.nextCard}")

            Playing.scoringSystem(self)  # New score is generated and displayed
            Playing.playAgain(self)

            print()
            print()

        print("--- Game Ended ---")
