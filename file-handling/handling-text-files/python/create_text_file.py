# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def create_file():
    """Create an empty text file"""
    filename = "playlist.txt"
    file_object = open(filename, mode = "w")
    file_object.close()  
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    create_file()
