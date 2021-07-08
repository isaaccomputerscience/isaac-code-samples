def double_it():
    """prompts user for number and doubles it"""
    number = input("Please enter a number ")
    int_number = int(number)
    answer = int_number * 2
    print(answer)

if __name__ == '__main__':
    double_it()
