# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def main():
    print("What hour is it?")
    user_input = input()
    hour = int(user_input)

    if hour < 12:
        print("Good morning")
    elif hour < 18:
        print("Good afternoon")
    elif hour < 22:
        print("Good evening")
    else:
        print("Good night")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
