# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


class Hand:

    def __init__(self):
        """Constructor"""
        self.__cards = []
        self.__value = 0
        self.__aces = 0

    def add_card(self, card):
        """Adds a card to the hand and calculates the new value of the hand"""
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
        """Returns the cards in the hand"""
        return self.__cards

    def get_value(self):
        """Returns the value of the hand"""
        return self.__value

    def clear(self):
        """Clears the hand"""
        self.__cards = []
        self.__value = 0
        self.__aces = 0
                
                   
# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':    
    player_hand = Hand()  # Test instantiation
