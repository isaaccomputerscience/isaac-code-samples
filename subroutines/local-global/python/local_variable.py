# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_local_and_global

def double(n):
    """Doubles a number and displays result"""
    amount = n * 2
    print(amount)

def triple(n):
    """Triples a number and displays result"""
    amount = n * 3
    print(amount)

def main():
    amount = 100
    print(amount)
    double(amount)
    triple(amount)
    print(amount)

if __name__ == '__main__':
    main() 
