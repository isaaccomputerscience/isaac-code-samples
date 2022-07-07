# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# BETA VERSION

class Hand:

    def __init__(self):
        self.__cards = []
        self.__value = 0
        self.__aces = 0

    def add_card(self, card):
        self.__cards.append(card)
        if card.get_rank() == "Ace":
            self.__aces += 1
        self.__value += card.get_value()
        if self.__value > 21: # adjust for aces
            aces = self.__aces
            while self.__value > 21 and aces > 0:
                self.__value -= 10
                self.__aces -= 1

    def get_cards(self):
        return self.__cards

    def get_value(self):
        return self.__value

    def clear(self):
        self.__cards = []
        self.__value = 0
        self.__aces = 0
                
                   
# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':    
    player_hand = Hand() # Instantiate an example Hand object
