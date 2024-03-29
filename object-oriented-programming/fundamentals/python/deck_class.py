# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# Make sure the file card_class.py is in the same folder as this file

from card_class import PlayingCard

class Deck:

    def __init__(self):
        self.__cards = []
        
        # Generate a deck of cards
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        
            
        for i in range(4):
            for j in range(13):
                new_card = PlayingCard(suits[i], ranks[j], values[j])
                self.__cards.append(new_card)
        
    
    def shuffle(self):
        # Code to shuffle cards here
        pass
    

    def deal(self, num_cards):
        # Code to remove and return cards here
        pass


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':   
    # Instantiate an example Deck object
    my_deck = Deck() 
