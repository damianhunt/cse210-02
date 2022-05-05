import random

class Card:

    def __init__(self):
        
        self.points = 0
        self.value = 0

    def draw_card(self):
        self.value = random.randint(1, 13)
        
        
        