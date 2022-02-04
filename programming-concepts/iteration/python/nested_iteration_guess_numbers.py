# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def main():
    numbers_to_guess = [1,4,8,3,10]

    print("Guess my numbers, each number is between 1 and 10")

    for number in numbers_to_guess:
        user_input = input("Enter a number to guess: ")
        guess = int(user_input)

        while guess != number:
            user_input = input("Enter a number to guess: ")
            guess = int(user_input)

        print("Well done, next number to guess")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
