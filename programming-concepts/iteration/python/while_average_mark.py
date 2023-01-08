# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def main():
    sum = 0
    num_values = 0

    user_input = input("Enter a mark or -1 to end: ")
    mark = int(user_input)

    while mark != -1:
        sum += mark  # sum = sum + mark
        num_values += 1
        user_input = input("Enter a mark or -1 to end: ")
        mark = int(user_input)

    average = sum / num_values
    print(f"The average mark was {average}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
