# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def main():
    score = None

    print("Would you like to start a new game?")
    response = input()

    if response == "YES":
        score = 0

    print(score)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
