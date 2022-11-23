# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def change_character():
    """Demonstrates finding a letter within a string"""
    welcome = "Hello Wirld"
    temp = welcome[:7] + 'o' + welcome[8:]
    welcome = temp
    print(welcome)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    change_character()
