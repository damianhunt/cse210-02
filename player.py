from card import Card

    

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
        ##initial.card = []
        ##self.card = []
        self.guess = ""
        self.game_in_progress = True
        self.score = 0
        self.total_score = 300
        
        ##for i in range(13):
        ##    card = Card()
        ##    self.card.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (player): an instance of player.
        """
        print(f"The card is: {c}")
        while self.game_in_progress:
            ##Card.draw = self.card
            ##Card.draw()
            self.obtain_inputs()
            self.do_updates()
            self.do_outputs()

        
    def obtain_inputs(self):
        """Ask the player if they want to play the game.
        
        Args:
            self (player): an instance of player.
        """
        

        guess = input('Higher or Lower: [H/L] ').upper()
        self.guess = (guess == 'H')
        
        play_game = input('Play again? [Y/N] ').upper()
        self.game_in_progress = (play_game == 'Y')


    def do_updates(self):
        """Updates the player's score.
        
        Args:
            self (player): an instance of player.
        """

        if not self.game_in_progress:
            return 
        for i in range(len(self.guess)):
            card = self.guess[i]
            card.guess()
            self.initial_score += card.points
        self.total_score += self.initial_score
        
    def do_outputs(self):
        """Displays the score. Also asks the player if they want to roll again. 

        Args:
            self (player): An instance of player.
        """
        if not self.game_in_progress:
            return
        
        values = ''
        for i in range(len(self.guess)):
            card = self.guess[i]
            values += f"{card.value} "

        print(f"You guessed: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.game_in_progress == (self.initial_score> 0)    
        
