# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_using_subroutines

def global_update_example():
    global number
    number = 10
    print(number)

number = 5
global_update_example()
print(number)
