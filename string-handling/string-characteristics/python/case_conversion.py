# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def convert_to_lower(letter):
    """Demonstrates how to use ASCII codes to convert letter case"""
    letter_code = ord(letter)
    new_letter_code = letter_code + 32
    lower_case = chr(new_letter_code)
    return lower_case


def test():
    """Test data"""
    letter = "B"
    lower_case = convert_to_lower(letter)
    print(lower_case)       


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    test()
