# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

from hand_class import Hand

class Player:

    def __init__(self, given_name):
        self.__name = given_name
        self.__score = 0
        self.__hand = Hand()

    def get_name(self):
        """Returns the player's name"""
        return self.__name

    def get_hand(self):
        """Returns the player's hand"""
        return self.__hand

    def get_score(self):
        """Returns the player's score"""
        return self.__score

    def set_score(self, new_score):
        """Sets the player's score"""
        self.__score = new_score
    

# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':    
    game_player = Player("Leona")  # Test instantiation
    name = game_player.get_name()  # Test method
    print(name)
