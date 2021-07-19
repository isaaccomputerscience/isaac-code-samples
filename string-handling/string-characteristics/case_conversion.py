# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def convert_to_lower(letter):
    """Demonstrates how to extract a file extension"""
    letter_code = ord(letter)
    new_letter_code = letter_code + 32
    lower_case = chr(new_letter_code)
    return lower_case


def test():
    """Test data"""
    letter = "B"
    lower_case = convert_to_lower(letter)
    print(lower_case)       
    

if __name__ == '__main__':
    test()
