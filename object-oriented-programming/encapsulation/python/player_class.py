# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

class Player:

    def __init__(self, given_name):
        self.__name = given_name
        self.__score = 0

    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        self.__score = new_score
    

# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':
    # Instantiate an example Player object
    game_player = Player("Leona") 
    print(f"The player's name is: {game_player.get_name()}")
    print(f"The player's score is: {game_player.get_score()}")
    game_player.set_score(20)
    print(f"The player's score is now: {game_player.get_score()}")
