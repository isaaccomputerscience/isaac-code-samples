# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def check_in_string():
    """Demonstrates checking if a substring occurs within a string"""
    my_string = "Hello World!"
    is_in_string = "World" in my_string
    print(is_in_string)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    check_in_string()
