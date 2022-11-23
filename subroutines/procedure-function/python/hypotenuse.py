# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_proc_fun

import math

def calculate_area(length):
    """Calculates the area of a square of a given side length"""
    area = length * length
    return area

def get_hypotenuse(a, b):
    """Calculates the length of the hypotenuse of a right angled triangle"""
    h = math.sqrt( calculate_area(a) + calculate_area(b) ) 
    return h

def main():
    side1 = 3
    side2 = 4
    hypotenuse = get_hypotenuse(side1, side2)
    print(hypotenuse)

if __name__ == '__main__':
    main() 
