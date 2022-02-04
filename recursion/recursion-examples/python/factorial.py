# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def factorial(n):
    """Recursively calculates and returns the value of n!"""
    if n == 1:
        return 1
    else:
        return  n * factorial(n-1)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    n = 5
    result = factorial(n)
    print(f"{n}! is {result}")
