# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def append_to_file():
    """Example of appending to a text file"""
    file_object = open("twinkle.txt", mode="a")
    file_object.write("\n") 
    file_object.write("When the blazing sun is gone\n")
    file_object.write("When he nothing shines upon,\n")
    file_object.write("Then you show your little light,\n")
    file_object.write("Twinkle, twinkle, all the night.\n")
    file_object.close()

    
# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    append_to_file()
