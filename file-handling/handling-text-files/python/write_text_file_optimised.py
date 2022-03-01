# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def write_to_file(data):
    """Appends data to a file and adds a new line"""
    filename = "playlist.txt"
    with open(filename, mode = "a") as playlist:
        playlist.write(data)
        playlist.write("\n")
        playlist.close()


def main():
    track1 = "Happy, Pharrell Williams, 03:55"
    write_to_file(track1)
    
    track2 = "Reach, S Club 7, 04:02"
    write_to_file(track2)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main() 
