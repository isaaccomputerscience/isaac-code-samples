# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# BETA VERSION

class PlayingCard:
    """Defines a standard playing card"""

    def __init__(self, given_suit, given_rank, given_value):
        self.__suit = given_suit
        self.__rank = given_rank
        self.__value = given_value

    def get_suit(self):
        """Returns the suit of the card"""
        return self.__suit

    def get_rank(self):
        """Returns the rank of the card"""
        return self.__rank

    def get_value(self):
        """Returns the value of the card"""
        return self.__value

    def get_description(self):
        """Returns suit and rank as a string"""
        return(f"{self.__rank} of {self.__suit}")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':        
    my_card = Card("clubs", "2", 2) # Instantiate an example Card object
    description = my_card.get_description()
    print(description)
