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

        for i in range(5):
            card = Card()
            self.cards.append(card)

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
            self.do_outputs()
        

    def first_card(self):
        if not self.is_playing:
            return 
        first_card = random.randint(1, 13)
        if self.total_score == 300:
            print(f"First Card: {first_card}")


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

        guess_card = input("Select High or Lower [H/L]: ")
        current_card = card.roll(self) 
        if current_card >= self.card_number and guess_card == "H":
            self.score += 100
        elif current_card <= self.card_number and guess_card == "H":
            self.score -= 70
        elif current_card >= self.card_number and guess_card == "L":
            self.score -= 75
        elif current_card <= self.card_number and guess_card == "L":
            self.score += 100
        
        self.total_score += self.score

        values = ""
        current_card = card.roll() 
        current_card.append(self.cards)
        card = self.cards[-1]
        values += f"{card.value} "
        print(f"Your new card: {values}")
        #for i in range(len(self.cards)):
        #    card = self.cards[i]
        #    card.draw()
        #    self.score += card.points 
        #self.total_score += self.score
        #self.score = 0

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        #values = ""
        #current_card = card.roll() 
        #current_card.append(self.cards)
        #card = self.cards[-1]
        #values += f"{card.value} "

        #self.draw()
        #guess_card = input("Select High or Lower [H/L]: ")
        #second_number = random.randint(1, 13)
        #if second_number >= self.card_number and guess_card == "H":
        #    self.score += 100
        #elif second_number <= self.card_number and guess_card == "H":
        #    self.score -= 70
        #elif second_number >= self.card_number and guess_card == "L":
        #    self.score -= 75
        #elif second_number <= self.card_number and guess_card == "L":
        #    self.score += 100
        #print(f"The next card was: {second_number}")
        #print(f"Your acore is: {self.score}") 
        
        #print(f"The next card was: {second_number}")
        #print(f"Your acore is: {self.total_score}")        
       
        
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)