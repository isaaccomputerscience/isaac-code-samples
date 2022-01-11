# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import pickle  # Module for working with binary files

def write_file(player_stats):
    """Simple example of writing to a binary file"""
    with open ("treasure.game", "wb") as gamefile:
        pickle.dump(player_stats, gamefile)


def read_file():
    """Simple example of reading from a binary file"""
    with open ("treasure.game", "rb") as gamefile:
        player_stats = pickle.load(gamefile)
    return player_stats
    
    
if __name__ == '__main__':
    player_stats = {"health": 100, "hunger":10, "money": 20.00, "lives":3}
    write_file(player_stats)
    player_stats = read_file()
    print(player_stats)
    print(type(player_stats))  # Just to prove it is a dictionary!

