# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_parameters 


def welcome_user(user):
    """Greets the user by name"""
    print("Greetings " + user)


def main():
    username = input("What is your name?")
    welcome_user(username)


if __name__ == '__main__':
    main()
