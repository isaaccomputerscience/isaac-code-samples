# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_parameters 


def welcome_user(user):
    print("Greetings " + user)


def main():
    username = input("What is your name?")
    welcome_user(username)


if __name__ == '__main__':
    main()