# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def print_backwards(phrase):
    """Prints a given word or phrase backwards"""
    if len(phrase) == 1:
        print(phrase, end = "")
    else:
        new_phrase = phrase[1:]
        print_backwards(new_phrase)
        print(phrase[0], end = "")


# This code will run if this file is executed directly
# (i.e. not called by another program) 
if __name__ == '__main__':
    print_backwards("I am a computer scientist")
