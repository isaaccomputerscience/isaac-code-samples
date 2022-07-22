# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

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
