# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_proc_fun

import math

def calculate_area(length):
    """Calculates the area of a square of a given side length"""
    area = length * length
    return area

def get_hypotenuse(a, b):
    """Calculates the length of the hypotenuse of a right angled triangle"""
    hypotenuse = math.sqrt( calculate_area(a) + calculate_area(b) ) 
    return hypotenuse

def main():
    length1 = 3
    length2 = 4
    hyp = get_hypotenuse(length1, length2)
    print(hyp)

if __name__ == '__main__':
    main() 
