# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def main():
    print("What is your name?")
    name = input()
    print(f"Hello {name}")

"""
Lines 6 and 7 can be combined into a single line of code:
name = input("What is your name?")
"""

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main() 