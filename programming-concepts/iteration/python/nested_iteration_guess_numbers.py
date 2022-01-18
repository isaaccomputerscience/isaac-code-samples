
numbers_to_guess = [1,4,8,3,10]

print("Guess my numbers, each number is between 1 and 10")

for number in numbers_to_guess:
    user_input = input("Enter a number to guess: ")
    guess = int(user_input)

    while guess != number:
        user_input = input("Enter a number to guess: ")
        guess = int(user_input)

    print("Well done, next number to guess")
