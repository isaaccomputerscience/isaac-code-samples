# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def main():
    numbers_to_guess = [1,4,8,3,10]

    print("Guess my numbers, each number is between 1 and 10")

    for number in numbers_to_guess:
        user_input = input("Enter a number to guess: ")
        guess = int(user_input)

        while guess != number:
            # If the user does not guess the number correctly, request another guess
            user_input = input("Enter a number to guess: ")
            guess = int(user_input)

        print("Well done, next number to guess")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
