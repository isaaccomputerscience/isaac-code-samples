# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_proc_fun


def calculate_area(length):
    """Calculates the area of a square of a given side length"""
    area = length * length
    return area

def main():
    length = 12
    result = calculate_area(length)
    print(result)

if __name__ == '__main__':
    main() 
