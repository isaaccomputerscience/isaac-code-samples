# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def main():
    """Create a list and output a value using an index value"""
    emotions = ["amazed", "delighted", "ecstatic", "enthusiastic", "lively"]

    print(emotions[2])  # Displays the third item in the list
    
    emotions.append("happy")  # Appends an item to the end of the list
    
    emotions.pop(1)  # Removes the second item from the list

    list_length = len(emotions)  # Get length of list
    for i in range(list_length):
        print(emotions[i])


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
