from card import Card

class Player:
    
    def __init__(self):
        
        self.guess = True
        self.game_in_progress = True
        self.initial_score = 300
        self.total_score = 300

    def start_game(self):

        while self.game_in_progress:

            self.obtain_inputs()
            self.obtain_updates()
            self.obtain_outputs()

        
    def obtain_inputs(self):
        guess = input('Higher or Lower: [H/L] ').upper()
        self.guess = (guess == 'H')
        
        play_game = input('Play again? [Y/N] ').upper()
        self.game_in_progress = (play_game == 'Y')

    def obtain_updates(self):

         if not self.game_in_progress:
            return 
        
