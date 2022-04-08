# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def create_file():
    """Create an empty text file"""
    file_object = open("playlist.txt", mode = "w")
    file_object.close()  
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    create_file()
