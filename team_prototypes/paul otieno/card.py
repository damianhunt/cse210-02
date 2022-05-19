from player import Player
    

class Card:

    def __init__(self):
        """
         Contructs a new player.
    
        Args:
        self (player): an instance of player.
         """
        self.game_in_progress = True
        self.player = Player()
        
    def input(self):

        self.player.get_card_number()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (player): an instance of player.
        """

        while self.game_in_progress:

            self.updates()
            self.outputs()
            self.input()
            self.keep()

    def updates(self):
        """Updates the player's score.
        
        Args:
            self (player): an instance of player.
        """
        return self.player.points_earned()
        
    def out_puts(self):
        """Displays the score. Also asks the player if they want to roll again. 

        Args:
            self (player): An instance of player.
        """
        self.player.get_card_number()
        print(f"The card is {self.player.card_number}")

    def keep(self):
        keep = input("keep playing? [y/n]")
        if keep == "y":
            self.game_in_progress = True
        elif keep =="n":
            self.game_in_progress = False