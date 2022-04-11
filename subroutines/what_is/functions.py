# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_what_is_a_subroutine

def calculate_area_of_square(length):
    area = length * length
    return area

def main():
    length = 12
    result = calculate_area_of_square(length)
    print(result)
    
if __name__ == "main":
    main()
