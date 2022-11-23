# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def bubble_sort_version_2(items):
    """A quite efficient bubble sort that stops if the items are sorted"""
    # Initialise the variables
    num_items = len(items)
    swapped = True

    # Repeat while one or more swaps have been made
    while swapped == True:
        swapped = False
        # Perform a pass
        for index in range(0, num_items - 1):
            # Compare items to check if they are out of order
            if items[index] > items[index + 1]:
                # Swap the items
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
                swapped = True
        print(items) # Testing


def main():
    """Perform a bubble sort on the test data"""
    #test_items = [80,64,50,43,35,21,7,3,2] # Least sorted
    #test_items = [2,3,7,35,43,21,50,64,80] # Nearly sorted
    #test_items = [2,3,7,21,35,43,50,64,80] # Sorted
    test_items = [43,21,2,50,3,80,35,7,64] # Random
    
    print("### Bubble sort version 2 (while and for loops) ###")
    print(test_items)
    
    bubble_sort_version_2(test_items)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
