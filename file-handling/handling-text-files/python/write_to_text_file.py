# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
     

def write_to_file():
    """Example of writing to a text file"""
    file_object = open("twinkle.txt", mode="w")  
    file_object.write("Twinkle, twinkle, little star,\n")
    file_object.write("How I wonder what you are!\n")
    file_object.write("Up above the world so high,\n")
    file_object.write("Like a diamond in the sky.\n")
    file_object.close()

    
# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    write_to_file()
