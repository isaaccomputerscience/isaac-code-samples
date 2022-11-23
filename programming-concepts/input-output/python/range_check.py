# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def main():
    user_input = input("Enter a week of the year: ")
    week = int(user_input)

    if week > 0 and week <= 52:
        print(f"You have chosen week {week}")
    else:
        print("A week must be between 1-52")

    
# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
