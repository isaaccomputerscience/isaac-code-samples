# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def strip_whitespace():
    """Demonstrates stripping whitespace from the start and end of a string"""
    my_string = "     Isaac Computer Science  \n"
    stripped_string = my_string.strip()
    print(stripped_string)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    strip_whitespace()
