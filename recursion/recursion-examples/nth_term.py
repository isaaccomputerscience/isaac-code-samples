# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def nth_term(n, increment):
    """Recursively calculates and returns the nth term of a sequence of integers"""
    if n == 1:
        return 1
    else:
        return increment + nth_term(n-1, increment)

if __name__ == '__main__':
    increment = 6
    n = 10
    result = nth_term(n, increment)
    print(f"The term is {result}")
