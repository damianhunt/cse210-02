import random


class Card:

    """
    The card class is 

    Attributes:
    next.card (int): This is responsible with generating a new random card between 1 and 13
"""

    def __self__(self):
        self.nextcard = 0

    def drawCard(self):
        self.nextcard = random.randint(1, 13)
        return self.nextcard
