# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_parameters 

def calculate_volume(height, width, depth):
    volume = height * width * depth
    print(volume)


def main():
    input_height = int(input("Enter height: "))
    input_width = int(input("Enter width: "))
    input_depth = int(input("Enter depth: "))
    calculate_volume(input_height, input_width, input_depth)


if __name__ == '__main__':
    main()
