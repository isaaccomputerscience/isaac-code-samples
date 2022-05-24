# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def convert_to_upper(my_string):
    ### Demonstrates how to convert a string to upper case ###
    upper_case_string = my_string.upper()
    return upper_case_string


def test():
    ### Test data ###
    name = input("Enter full name: ")
    converted_string = convert_to_upper(name)
    print(converted_string)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    test()
