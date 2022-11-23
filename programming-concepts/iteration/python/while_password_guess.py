# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def main():
    password = "1234"
    password_guess = ""

    while password_guess != password:
        print("Please enter your password: ")
        password_guess = input()


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
