# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def main():
    """Create a list and output a value using an index value"""
    emotions = ["amazed", "delighted", "ecstatic", "enthusiastic", "lively"]

    print(emotions[2])  # Displays the third item in the list
    
    emotions.append("happy")  # Appends an item to the end of the list


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
