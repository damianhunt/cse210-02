import random


class Card:

    """
    The card class has 1 method which is drawCard()

    Attributes:
    nextcard (int): This is responsible with generating a new random card between 1 and 13
"""

    def __init__(self):
        self.nextcard = 0

    def drawCard(self):
        """
        The drawCard method is the one which generates a random card between 1 and 13 everytime its called
    """
        self.nextcard = random.randint(1, 13)
        return self.nextcard
