# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def main():
    print("How old are you?")
    user_response = input()
    age = int(user_response)
    months = age * 12
    print(f"Wow, you have been alive for around {months} months!")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()   

