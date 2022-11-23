# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_what_is_a_subroutine

import random  #imports the random library

def main():
    num = random.randint(1, 100)
    print(num)

# This code will run if this file is executed directly (i.e. not called by another program)
if __name__ == "__main__":
    main()
