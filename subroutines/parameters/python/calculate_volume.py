# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_parameters 

def calculate_volume(height, width, depth):
    """Calculate the volume of a cuboid"""
    volume = height * width * depth
    return(volume)


def main():
    input_height = float(input("Enter height: "))
    input_width = float(input("Enter width: "))
    input_depth = float(input("Enter depth: "))
    volume = calculate_volume(input_height, input_width, input_depth)
    print(volume)


if __name__ == '__main__':
    main()
