# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def create_file():
    """Simple example of creating a text file"""
    filename = "playlist.txt"
    playlist = open(filename, mode = "w")
    playlist.close()  
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    create_file()
