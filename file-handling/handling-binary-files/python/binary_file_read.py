# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import pickle # Module for working with binary files

def read_binary_file():
    """Read data from a binary file"""
    filename = "treasure.game"
    with open(filename, mode="rb") as gamefile:
        player_stats = pickle.load(gamefile)
    return player_stats


def main():
    player_stats = read_binary_file()
    print(player_stats)
    print(type(player_stats)) # to prove it is a dictionary!
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main()
