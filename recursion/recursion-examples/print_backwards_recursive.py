def print_backwards (string):
    ''' Prints a given string backwards '''
    if len (string) == 1:
        print (string , end = '')
    else:
        new_string = string[1:]
        print_backwards (new_string)
        print (string[0], end = '')

if __name__ == '__main__':
    print_backwards ('I am a computer scientist')
