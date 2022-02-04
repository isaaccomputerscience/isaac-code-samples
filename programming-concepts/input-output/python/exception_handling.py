# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def main():
    print("Enter a number")
    try:
        user_input = input()
        number = int(user_input)
    except ValueError:
        print("You must enter a numeric value")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()  

