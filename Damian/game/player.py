from game.card import Card
import random

    

class Player:
    """"
   A computer randomly select a  number from 1 to 13. 
   A player should guess whether the next choice is either
   higher number or lower. The player control the game. Can choose
   to play or stop playing until scoe = 0.
   
   Attributes:
   Guess: A list of guess options
   is_playing( boolean): The player is either playing or not playing
   inti_score(int): Starting score
   score(int):  The score of one round
   total score(): The score of the entire game
"""
   
    
    def __init__(self):
        """
         Contructs a new player.
    
        Args:
        self (player): an instance of player.
         """

        self.card = []
        self.guess = ""
        self.game_in_progress = True
        self.score = 0
        self.total_score = 300
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (player): an instance of player.
        """
        self.initial_card()
        while self.game_in_progress:

            self.obtain_inputs()
            self.card_draw()
            self.do_updates()
            self.do_outputs()

    def initial_card(self):
        card = self.card
        Card.draw()
        initial_card = card.value
        print (f"Your card is: {initial_card}")
        return initial_card

        
    def obtain_inputs(self):
        """Ask the player if they want to play the game.
        
        Args:
            self (player): an instance of player.
        """
        print (f"Your card is: {self.initial_card}")

        guess = input('Higher or Lower: [H/L] ').upper()
        self.guess = guess
        

    def card_draw(self):
        card = self.card
        Card.draw()
        current_card = card.value
        print (f"Next card is: {current_card}")
        return current_card

    def do_updates(self):
        """Updates the player's score.
        
        Args:
            self (player): an instance of player.
        """

        if not self.game_in_progress:
            return 

        if self.guess == "H":
            if Card.draw() > self.initial_card:
                self.score += 100
            else:
                self.score - 75
        elif self.guess == "L":
            if Card.draw() < self.initial_card:
                self.score += 100
            else:
                self.score - 75
        

        
    def do_outputs(self):
        """Displays the score. Also asks the player if they want to roll again. 

        Args:
            self (player): An instance of player.
        """
        if not self.game_in_progress:
            return
        
        print(f"Your score is: {self.total_score}\n")
        self.initial_card = self.card_draw

        if self.total_score == 0:
            self.game_in_progress == False

        play_game = input('Play again? [Y/N] ').upper()
        if play_game == "Y":
            self.game_in_progress = True
        

        
