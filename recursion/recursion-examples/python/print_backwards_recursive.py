# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def print_backwards(phrase):
    """Prints a given word or phrase backwards"""
    if len(phrase) == 1:
        print(phrase, end = "")
    else:
        new_string = phrase[1:]
        print_backwards(new_phrase)
        print(phrase[0], end = "")

if __name__ == '__main__':
    print_backwards("I am a computer scientist")
