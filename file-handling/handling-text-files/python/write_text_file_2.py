# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def write_to_file():
    """Example of appending a record to a text file"""
    filename = "playlist.txt"
    new_track = "Reach, S Club 7, 04:02"
    
    with open(filename, mode = "a") as playlist:
        playlist.write(new_track)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    write_to_file()
