# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def show_substrings():
    """Demonstrates extracting substrings"""
    my_string = "Computer Science"
    # Display characters 7 to 9
    print(my_string[7:10])
    
    # Display characters from start of string up to index position 4 
    print(my_string[:5])
    
    # Display characters from index position 6 to end of string
    print(my_string[6:])
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    show_substrings()
