# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def main():
    sum = 0
    num_values = 0

    user_input = input("Enter a mark or -1 to end ")
    mark = int(user_input)

    while mark != -1:
        sum = sum + mark
        num_values = num_values + 1
        user_input = input("Enter a mark or -1 to end ")
        mark = int(user_input)

    average = sum / num_values
    print(f"The average mark was {average}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
