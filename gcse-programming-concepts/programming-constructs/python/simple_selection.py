def guess_the_animal():
    """Example of a simple selection statement"""
    animal = input("Which animal has a long bendy trunk? ")
    if animal == "elephant":
        print("You are correct")
    else:
        print("You are incorrect")

if __name__ == '__main__':
    guess_the_animal()
