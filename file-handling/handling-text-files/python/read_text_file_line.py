# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def read_line_of_file():
    """Read and display a single line of the file"""
    file_object = open("bridge.txt", mode="r")
    rhyme_line = file_object.readline()
    file_object.close()
    print(rhyme_line) 
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    read_line_of_file()
