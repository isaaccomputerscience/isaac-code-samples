# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def bubble_sort_version_1(items):
    """An inefficient bubble sort that uses nested for loops"""
    # Initialise the variables
    num_items = len(items)

    # Pass through the array of items n-1 times
    for pass_num in range(1, num_items):
        # Perform a pass
        for index in range(0, num_items - 1):
            # Compare items to check if they are out of order
            if items[index] > items[index + 1]:
                # Swap the items
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
        print(items) # Testing


def main():
    """Perform a bubble sort on the test data"""
    #test_items = [80,64,50,43,35,21,7,3,2] # Least sorted
    #test_items = [2,3,7,35,43,21,50,64,80] # Nearly sorted
    #test_items = [2,3,7,21,35,43,50,64,80] # Sorted
    test_items = [43,21,2,50,3,80,35,7,64] # Random
    
    print("### Bubble sort version 1 (for loops) ###")
    print(test_items)
    
    bubble_sort_version_1(test_items)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
