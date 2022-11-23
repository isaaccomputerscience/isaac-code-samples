# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def main():
    valid_booking = False
    booking = input("Enter your booking reference: ")

    if len(booking) == 8:
        valid_booking = True


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
