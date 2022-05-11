from card import Card

class Player:
    
    def __init__(self):
        
        self.card = []
        self.guess = True
        self.game_in_progress = True
        self.score = 0
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

        for i in range(len(self.card)):
            card = self.card[i]
            card.draw()
            self.score += card.points 
        self.total_score += self.score
        self.score = 0

    def obtain_outputs(self):

        if not self.game_in_progress:
            return
        