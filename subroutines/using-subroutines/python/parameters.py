# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_using_subroutines

def calculate_two_numbers(number1, number2):
    answer = number1 + number2
    return answer

def main():
    answer = calculate_two_numbers(5, 10)
    print(answer)
    
    
# This code will run if this file is executed directly (i.e. not called by another program)
if __name__ == '__main__':
    main()
