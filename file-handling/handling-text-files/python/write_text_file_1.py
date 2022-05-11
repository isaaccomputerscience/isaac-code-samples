# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def write_to_file():
    """Simple example of writing a record to a text file"""
    new_track = "Happy, Pharrell Williams, 3:55"
    with open("playlist.txt", mode = "a") as playlist:
        playlist.write(new_track)

    
# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    write_to_file()