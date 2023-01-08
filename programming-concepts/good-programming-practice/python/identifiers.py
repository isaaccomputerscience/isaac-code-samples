# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


# First example
def conv(a):
    b = a / 9.81 * 3.711
    return b
# These identifiers do not help the programmer understand what is happening in the program


# Second example
GRAVITY_ON_EARTH = 9.81
GRAVITY_ON_MARS = 3.711


# This function takes a float as its parameter, and returns a float
def calculate_weight_on_mars(weight_on_earth: float) -> float:
    weight_on_mars = (weight_on_earth / GRAVITY_ON_EARTH) * GRAVITY_ON_MARS
    return weight_on_mars
# These identifiers clearly show the meaning and purpose of the data they hold.


def main():
    """
    Execute both subroutines and output the results
    """

    weight = 35.7
    print(conv(weight))
    print(calculate_weight_on_mars(weight))
    # It is possible to specify parameters for clarity: calculate_weight_on_mars(weight_on_earth=weight)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
