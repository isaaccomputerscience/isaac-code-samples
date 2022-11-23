# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def nth_term(n, increment):
    """Recursively calculates and returns the nth term of a sequence of integers"""
    if n == 1:
        return 1
    else:
        return increment + nth_term(n-1, increment)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    increment = 6
    n = 10
    result = nth_term(n, increment)
    print(f"The term is {result}")
