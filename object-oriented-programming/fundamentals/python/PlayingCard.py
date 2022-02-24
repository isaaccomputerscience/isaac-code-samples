# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

class PlayingCard:

    def __init__(self, given_suit, given_rank, given_value):
        self.__suit = given_suit
        self.__rank = given_rank
        self.__value = given_value
    

if __name__ == '__main__':    
    # Instantiate an example PlayingCard object
    two_of_clubs = PlayingCard("clubs", "2", 2)
