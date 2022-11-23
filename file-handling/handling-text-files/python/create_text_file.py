# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
     

def create_file():
    """Create an empty text file"""
    file_object = open("playlist.txt", mode = "w")
    file_object.close()  
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    create_file()
