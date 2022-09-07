# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# BETA VERSION

from card_class import Card

SUITS = ["Hearts", "Spades","Clubs", "Diamonds"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
VALUES = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random

class Deck:
    """Defines a standard 52-card deck of cards"""

    def __init__(self):
        self.__cards = []     
        for i in range(4):
            for j in range(13):
                new_card = Card(SUITS[i], RANKS[j], VALUES[j])
                self.__cards.append(new_card)
        self.shuffle()
        
    
    def shuffle(self):
        # Shuffles cards
        random.shuffle(self.__cards)
    

    def deal(self):
        # Removes and returns the first card in the deck        
        return self.__cards.pop()

    def reset(self):
        self.__cards = []
        for i in range(4):
            for j in range(13):
                new_card = Card(SUITS[i], RANKS[j], VALUES[j])
                self.__cards.append(new_card)
        self.shuffle()


# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':       
    my_deck = Deck() # Instantiate an example Deck object
