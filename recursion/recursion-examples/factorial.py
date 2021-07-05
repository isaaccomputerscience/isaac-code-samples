def factorial (n):
    """Recursively calculates and returns the value of n!"""
    if n == 1:
        return 1
    else:
        return  n * factorial(n-1)


if __name__ == '__main__':
    n = 5
    result = factorial (n)
    print("{}! is {}".format(n, result))
