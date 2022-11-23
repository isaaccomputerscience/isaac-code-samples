# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def show_password_length():
    """Prompts for a password and displays length"""
    password = input("Please enter a password ")
    print(len(password))


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    show_password_length()
