# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

class PlayingCard:

    def __init__(self, given_suit, given_rank, given_value):
        self.__suit = given_suit
        self.__rank = given_rank
        self.__value = given_value
    
    def get_suit(self):
        return self.__suit
    
    def get_rank(self):
        return self.__rank
    
    def get_value(self):
        return self.__value

    """
    Alternative version using decorators

    def suit(self):
        return self.__suit
    
    @suit.setter
    def suit(self, new_suit):
        self.__suit = new_suit    
    """

# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':    
    # Instantiate an example PlayingCard object
    two_of_clubs = PlayingCard("clubs", "2", 2)
