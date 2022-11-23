# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def main():
    print("Please enter your name: ")
    name = input()

    while name != "Bob":
        print("Try again Bob")
        print("Please enter your name: ")
        name = input()

    print("Hi Bob")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
