def gcd(x, y):
    """Euclidian algorithm to find greatest common denominator."""
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
    

if __name__ == '__main__':
    x = 259
    y = 111
    answer = gcd(x, y)
    print("The lowest common denominator of {} and {} is {}".format(x, y, answer))
