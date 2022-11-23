# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def main():
    """Demonstrates finding a letter within a string"""
    subject = "Computer Science"
    letter_sought = "m"
    show_position(subject, letter_sought)
    position = subject.find(letter_sought)
    print(f"{letter_sought} found at: {position}")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
