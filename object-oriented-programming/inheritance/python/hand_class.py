# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

from deck_class import Deck
# Requires the Deck and Card classes to exist inside the same folder
# otherwise this will cause an error

class Hand(Deck):

    def __init__(self):
        super().__init__()
    
    def get_value(self):
        # Code to calculate the values of the cards in a hand
        pass

            
# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':
    my_hand = Hand() 
