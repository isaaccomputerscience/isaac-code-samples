# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# Requires the files deck_class and hand_class to exist inside the same folder
# otherwise the import statement will throw an error

from deck_class import Deck


class Hand(Deck):

    def __init__(self):
        super().__init__()  # Call Deck constructor
        # Extra code for Hand constructor
    
    def get_value(self):
        # Code to calculate the values of the cards in a hand
        pass

            
# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':
    my_hand = Hand() 
