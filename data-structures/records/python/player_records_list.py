# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


class PlayerRecord():
    """Use a class to represent a player as a record"""
    
    def __init__ (self):
        self.player_id = None
        self.first_name = None
        self.last_name = None
        self.date_of_birth = None
        self.position = None
        self.injured = None


def create_player(p_id, f_name, l_name, dob, pos, inj):
    """Create a new player record with the given data"""
    
    # Create a new player record
    player = PlayerRecord()

    # Store the details of the player
    player.player_id = p_id
    player.first_name = f_name
    player.last_name = l_name
    player.date_of_birth = dob
    player.position = pos
    player.injured = inj

    # Return the player record
    return player


def display_players(players_list):
    """Display some of the player details from each player record"""
    
    print("### List of player records ###")

    # Repeat for each player in the players list of records
    for player in players_list:
        # Display the player's number, name and position
        print(f"\nNumber: {player.player_id}")
        print(f"Name: {player.first_name} {player.last_name}")
        print(f"Position: {player.position}")


def main():
    """Create a list of player records with the details of each player"""

    # Declare a list to store the player records
    first_team = []

    # Testing - create 4 players and add them to the list
    player1 = create_player(1, "Maria", "Oarps", "03/07/1994",
                            "Goalkeeper", False)
    first_team.append(player1)
    
    player2 = create_player(2, "Lucie", "Gold", "18/10/1991",
                            "Defender", True)
    first_team.append(player2)

    player3 = create_player(3, "Raquel", "Weekly", "12/06/1992",
                            "Defender", False)
    first_team.append(player3)
    
    player4 = create_player(4, "Kiera", "Welsh", "04/08/1998",
                            "Midfielder", False)
    first_team.append(player4)
    
    # Display information about each player
    display_players(first_team)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
