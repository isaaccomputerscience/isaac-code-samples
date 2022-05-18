# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_using_subroutines

def rle(text_string):
    """A simple version of RLE for text strings"""
    current_token = text_string[0]
    compressed = current_token
    counter = 0
    for i in range (len(text_string)):
        next_token = text_string[i]
        if next_token != current_token:
            compressed = compressed + str(counter) + next_token
            counter = 1
        else:
            counter = counter + 1
        current_token = next_token
    compressed = compressed + str(counter)
    return compressed


def run_tests():
    """sample test data"""
    # Normal data
    text = "aaaabbbccdddeee"
    print(text)
    print(rle(text))
    text = "Bobby"
    print(text)
    print(rle(text))
    # Boundary data
    text = "a"
    print(text)
    print(rle(text))
    text = "aaaaaa"
    print(text)
    print(rle(text))    
    text = "aaaae"
    print(text)
    print(rle(text))
    text = "aeeeee"
    print(text)
    print(rle(text))
    
    
# This code will run if this file is executed directly (i.e. not called by another program)
if __name__ == '__main__':
    run_tests()
