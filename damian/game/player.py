from game.card import Card
import random

class Player:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        values = ""
        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        first_card = 0
        card = 0


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.first_card()
            self.get_inputs()
            self.draw_card()
            self.do_updates()
            self.guess_card()
            self.do_outputs()
        

    def first_card(self):
        if not self.is_playing:
            return 
        first_card = random.randint(1, 13)
        if self.total_score == 300:
            print(f"First Card: {first_card}")
        return first_card


    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        draw_card = input("Draw Card? [y/n] ").upper()
        self.is_playing = (draw_card == "Y")
    
    def draw_card(self):
        if not self.is_playing:
            return 
        card = Card.draw(self)
        print(f"Next card was: {card}")
        return card
    

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        guess_card = input("Select High or Lower [H/L]: ").lower
        #current_card = Card.draw(self)
        return guess_card
        #if current_card >= Player.first_card(self) and guess_card == "H":
        #    self.score += 100
        #elif current_card <= Player.first_card(self) and guess_card == "H":
        #    self.score -= 70
        #elif current_card >= Player.first_card(self) and guess_card == "L":
        #    self.score -= 75
        #elif current_card <= Player.first_card(self) and guess_card == "L":
        #    self.score += 100


    def guess_card(self):
        if not self.is_playing:
            return

        if Player.do_updates(self) == 'h' and Player.current_card > Player.first_card(self):
            return True
        elif Player.do_updates(self) == 'l' and Player.current_card < Player.first_card(self):
            return True
        else:
            return False


    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        check_guess_result = ''
        #self.total_score += self.score
        if Player.guess_card(self) == True:
            self.score = 100
        else: 
            self.score = -75   

        self.total_score += self.score

        
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.total_score > 0)