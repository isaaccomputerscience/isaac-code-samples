# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def write_to_file():
    """Simple example of writing records to a text file"""
    with open("playlist.txt", mode = "a") as playlist:
        new_track = "Happy, Pharrell Williams, 3.55"
        playlist.write(new_track)
        playlist.write("\n")
        new_track = "Reach, S Club 7, 4.02"
        playlist.write(new_track)
        playlist.write("\n")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    write_to_file()
