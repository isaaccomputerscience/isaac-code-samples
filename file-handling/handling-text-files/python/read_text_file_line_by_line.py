# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def read_line_by_line():
    """Read and display a file line by line"""
    file_object = open("bridge.txt", mode="r")
    for rhyme_line in file_object:
        print(rhyme_line)
    file_object.close() 
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    read_line_by_line()
