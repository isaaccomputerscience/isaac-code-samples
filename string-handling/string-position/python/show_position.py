# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def show_position(my_string, letter_sought):
    """Demonstrates finding a letter within a string"""
    position = my_string.find(letter_sought)
    print(f"{letter_sought} found at: {position}")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    subject = "Computer Science"
    letter = "m"
    show_position(subject, letter)
