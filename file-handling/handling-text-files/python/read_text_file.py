# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def read_file():
    """Read and display each record from a file"""
    with open("playlist.txt", mode = "r") as playlist:
        for track in playlist:
            print(track)   
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    read_file()
