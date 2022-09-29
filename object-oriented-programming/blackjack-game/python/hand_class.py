# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


class Hand:

    def __init__(self):
        """Constructor"""
        self.__cards = []
        self.__value = 0  # value of hand
        self.__aces = 0  # number of aces in hand

    def add_card(self, card):
        """Adds a card to the hand and calculates the new value of the hand"""
        self.__cards.append(card)
        if card.get_rank() == "Ace":
            self.__aces += 1
        self.__value += card.get_value()
        if self.__value > 21:  # if the value of hand is over 21
            aces = self.__aces  # get number of aces in hand
            while self.__value > 21 and aces > 0:  # if there are aces left to evaluate and value of hand is still over 21
                self.__value -= 10  # take the value of an ace as 1
                aces -= 1  # adjust number of aces to evaluate

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
