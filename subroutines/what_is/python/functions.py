# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_what_is_a_subroutine

def calculate_area_of_square(length):
    area = length * length
    return area

def main():
    length = 12
    result = calculate_area_of_square(length)
    print(result)

# This code will run if this file is executed directly (i.e. not called by another program)
if __name__ == "__main__":
    main()
