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
      
        
    def play_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Game): an instance of Game.
        """
        while self.is_playing:
            self.display_instructions
            self.prompt_for_guess()
            self.check_guess()
            self.update_score()
            self.print_score
            self.play_again

    
    def display_instructions():
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
        return user_input
    #check_guess(guess, current_card.value, next_card.value)
    def check_guess(self,guess, current_card_value, next_card_value):
        """Check to see if the player win or lost     

        Args:
         self (Game): an instance of Game.
            guess: the user input value
            current_card_value : the value of the current card
            next_card_value : the value of the next card

        """    
        if guess == 'h'.lower and next_card_value > current_card_value:
            return True
        elif guess == 'l'.lower and next_card_value < current_card_value:
            return True
        else:
            return False
     
    
    def update_score(self, check_guess_result):
        """Updates the score points

        Args:
            self (Game): an instance of Game.
            guess: Uses guess result to update the score
        """
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