def double_it():
    """Prompts user for a number and doubles it"""
    number = input("Please enter a number ")
    float_number = float(number)
    answer = float_number * 2
    print(f"The answer is {answer}")
    print(f"{answer:.2f}")

if __name__ == '__main__':
    double_it()
