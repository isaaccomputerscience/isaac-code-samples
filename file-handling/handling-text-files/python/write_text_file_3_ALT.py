# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def write_to_file():
    """Simple example of writing records to a text file"""
    filename = "playlist.txt"
    track1 = "Happy, Pharrell Williams, 3.55"
    track2 = "Reach, S Club 7, 4.02"
    
    with open(filename, mode = "a") as playlist:
        playlist.write(track1)
        playlist.write("\n")
        playlist.write(track2)
        playlist.write("\n")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    write_to_file()
