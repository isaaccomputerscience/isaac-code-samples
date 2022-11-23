# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def check_empty_string(my_string):
    """Checks if a string is empty"""
    empty = False
    length_my_string = len(my_string)

    if length_my_string == 0:
        empty = True

    return empty


def main():
    user_input = input("Enter a string to check if it is empty: ")
    is_empty = check_empty_string(user_input)

    if is_empty == True:
        print("Yes, the string is empty!")
    else:
        print("No, the string is not empty!")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
