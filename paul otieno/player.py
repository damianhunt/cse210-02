import random

class Player:

    def __init__(self):
        
        self.card_number = 0
        self.player = 0
        self.score = 300

    def get_card_number(self):
        self.card_number = random.randint(1, 13)
    
    def points_earned(self):
        self.get_card_number()
        guess_card = input("Select High or Lower [H/L]: ")
        second_number = random.randint(1, 13)
        if second_number >= self.card_number and guess_card == "H":
            self.score += 100
        elif second_number <= self.card_number and guess_card == "H":
            self.score -= 70
        elif second_number >= self.card_number and guess_card == "L":
            self.score -= 75
        elif second_number <= self.card_number and guess_card == "L":
            self.score += 100
        print(f"The next card was: {second_number}")
        print(f"Your acore is: {self.score}")        
        