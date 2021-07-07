def greetings():
    """Demonstration of string concatenation"""
    first_name = input("Please enter your name ")
    print("Hello " + first_name)
    surname = input("Please enter your surname ")
    full_name = first_name + " " + surname
    print("Hello " + full_name)

if __name__ == "__main__":
    greetings()
