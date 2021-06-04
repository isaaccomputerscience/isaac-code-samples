def palindrome(word):
    """Returns True if word is a palindrome"""
    length = len(word)
    if length == 0 or length == 1:
        return True
    elif word[0] == word[length - 1]:
        new_word = word[1 : length - 1]
        return palindrome(new_word)
    else:
        return False


if __name__ == '__main__':
    test_word = 'kayak'
    is_palindrome = palindrome(test_word)
    print ("{}: {}".format(test_word, is_palindrome))
