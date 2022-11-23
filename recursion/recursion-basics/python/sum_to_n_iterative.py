# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def sum_to_n_iterative(n):
    """Calculates and returns the sum of all natural numbers from 1 to n inclusive"""
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ =='__main__':
    n = 6
    result = sum_to_n_iterative(n)
    print(f"The sum of 1 to {n} is: {result}")
