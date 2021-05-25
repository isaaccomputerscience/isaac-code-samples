def nth_term(n, increment):
    ''' Returns the nth term of a sequence of integers'''
    if n == 1:
        return 1
    else:
        return increment + nth_term(n-1, increment)

if __name__ == '__main__':
    increment = 6
    n = 10
    print (nth_term (n, increment))
