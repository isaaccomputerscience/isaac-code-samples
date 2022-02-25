# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def write_to_file(data):
    """Writes data to a file"""
    filename = "playlist.txt"
    with open(filename, mode = "a") as playlist:
        playlist.write(data)
        playlist.write("\n")
        playlist.close()


def main():
    track1 = "Happy, Pharrell Williams, 3:55"
    write_to_file(track1)
    track2 = "Reach, S Club 7, 4:02"
    write_to_file(track2)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main() 
