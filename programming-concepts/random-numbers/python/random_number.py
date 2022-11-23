# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

from random import randint

def main():
    random_number = randint(1,100)
    print(random_number)

    
# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()