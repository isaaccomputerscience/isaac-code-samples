# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def palindrome(word):
    """Recursively determines whether a word is a palindrome. Returns a Boolean."""
    length = len(word)
    if length == 0 or length == 1:
        # Empty strings and single letters are palindromes!
        return True
    elif word[0] == word[-1]:
        new_word = word[1: -1]
        print(new_word)
        return palindrome(new_word)
    else:
        return False


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    test_word = 'kayak'
    is_palindrome = palindrome(test_word)
    print(f"{test_word}: {is_palindrome}")
