# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def create_playlist():
    """Simple example of creating a text file"""
    playlist = open("playlist.txt", mode = "w")
    playlist.close()  
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    create_playlist()
