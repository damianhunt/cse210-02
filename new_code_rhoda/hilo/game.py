from re import U
from hilo.card import Card


class Game:
    """A computer directs the game. It selects a random number 
    asks the player to guess if the next number is higher or lower.
    if guess correctly a reward of 100 points is given but if failed
    to guess a penalty of deduction of 75 points is given. 
    
    """
    
    def __init__(self):
        
        self.score = 300
        self.is_playing = True
        self.current_card = Card()
        self.next_card = Card()
        self.total_score = 0
        self.check_guess = True
      
        
    def play_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Game): an instance of Game.
        """
        while self.is_playing:
            self.display_instructions()
            self.prompt_for_guess()
            self.update_score()
            self.print_score()
            self.play_again()

    
    def display_instructions(self):
        """Prints instructions for the user to see and know what to do
           Args:
            self (Game): an instance of Game.
        """

        print('This is a Hilo game. All you have to do is pick a number from 1 to 13.')
        print('Guess if the next number is higher or lower.')
       
    def prompt_for_guess(self):
        """ Prompts the user to guess a number.
        
        Args:
            self (Game): an instance of Game.
    
        """
        user_input = input('Is the the next card higher or lower? [h/l]: ')
        self.is_playing = (user_input == 'y')
    #check_guess(guess, current_card.value, next_card.value)
    def check_guess(self):
        """Check to see if the player win or lost     

        Args:
         self (Game): an instance of Game.
            guess: the user input value
            current_card_value : the value of the current card
            next_card_value : the value of the next card

        """   
        if not self.is_playing:
            return
        guess = self.is_playing
        current_card = self.current_card.value
        next_card = self.next_card.value
        
        self.check_guess = guess
        if guess == 'h'.lower and next_card > current_card:
            return True
        elif guess == 'l'.lower and next_card < current_card:
            return True
        else:
            return False
     
    
    def update_score(self):
        """Updates the score points

        Args:
            self (Game): an instance of Game.
            guess: Uses guess result to update the score
        """
        if not self.is_playing:
            return
        check_guess_result = ''
        self.total_score =+ self.score
        if check_guess_result == True:
            self.score = 100
        else: 
            self.score = -75   
        
    
    def print_score(self):
        """ Print the score of the results for the user to see
        
        Args:
            self (Game): an instance of Game.
        """
        
        print(f'Your new score is {self.score} ')
        
    
    def play_again(self):
        """ Asks the player to keep playing
        
        Args:
            self (Game): an instance of Game.
        """
        print('Do you want to play again? [y/n]: ')