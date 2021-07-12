def loop_until_correct():
    """An example of a condition controlled loop."""
    name = input("Please enter your name ")
    while name != "Fergus":
       name = input("Please enter your name ")
    print("You guessed my name!")

if __name__ == '__main__':
    loop_until_correct()
