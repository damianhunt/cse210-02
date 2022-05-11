import random

class Card:

    def __init__(self):
        
        self.points = 0
        self.value = 0

    def draw(self):
        self.value = random.randint(1, 13)
        ##self.points = 100 if self.value == 1 else 50 if self.value == 5 else 0
        
        