# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def sum_to(given_number):
    """Calculates the sum of all integers from 1 to the given number"""

    total = 0
    for i in range(1, given_number + 1):
        total = total + i
        
    return total


def main():
    """Test the sum_to function"""

    num = 5
    result = sum_to(num)
    print(f"The sum of all integers from 1 to {num} is {result}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
