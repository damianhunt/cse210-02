import random


class Card:

    def __init__(self):
        self.value =  random.randint(1, 13)

    def generate_new_card(self):
        self.value = random.randint(1, 13)
 
    def display_card(self):
        print(f'The card is {self.value}')
        
    
    
         