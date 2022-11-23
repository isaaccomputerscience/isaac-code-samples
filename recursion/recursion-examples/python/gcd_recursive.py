# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def gcd(x, y):
    """Euclidian algorithm to find and return the greatest common denominator of two numbers"""
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    x = 259
    y = 111
    answer = gcd(x, y)
    print(f"The lowest common denominator of {x} and {y} is {answer}")
