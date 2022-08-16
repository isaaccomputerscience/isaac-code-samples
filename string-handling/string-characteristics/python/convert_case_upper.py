# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def convert_to_upper():
    """Demonstrates how to convert a string to upper case"""
    user_name = input("Enter your full name: ")
    upper_case_name = user_name.upper()
    print(upper_case_name)

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    convert_to_upper()
