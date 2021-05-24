def nth_term(n):
    ''' returns the nth term of a numerical sequence'''
    if n == 1:
        return 1
    else:
        return 3 + nth_term(n-1)


if __name__ =='__main__':
    n = 6
    result = nth_term(n)
    print ('Term {} is {}'.format(n, result))
