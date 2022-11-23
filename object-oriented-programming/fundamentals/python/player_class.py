# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

class Player:

    def __init__(self, given_name):
        self.__name = given_name
        self.__score = 0
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    # Instantiate an example Player object
    player_name = input("Enter your name ")
    game_player = Player(player_name)
