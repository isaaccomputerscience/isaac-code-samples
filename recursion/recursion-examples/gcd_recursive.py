def gcd(x, y):
    ''' Euclidian algorithm to find greatest common denominator '''
    if y == 0:
        return x
    else:
        return gcd (y, x % y)
    

if __name__ == '__main__':
    print (gcd (259, 111))
