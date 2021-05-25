def palindrome(string):
    ''' Returns True if string is a palindrome '''
    print (string)
    length = len (string)
    if length == 0 or length == 1:
        return True
    elif string[0] == string[length - 1]:
        new_string = string[1 : length - 1]
        return palindrome (new_string)
    else:
        return False


if __name__ == '__main__':
    test_word = 'kayak'
    is_palindrome = palindrome (test_word)
    print ('{}: {}'.format(test_word, is_palindrome))
