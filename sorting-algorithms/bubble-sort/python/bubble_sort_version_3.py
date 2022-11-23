# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def bubble_sort_version_3(items):
    """A more efficient bubble sort that reduces the number of comparisons per pass"""
    # Initialise the variables
    num_items = len(items)
    swapped = True
    pass_num = 1

    # Repeat while one or more swaps have been made
    while swapped == True:
        swapped = False
        # Perform a pass, reducing the number of comparisons each time
        for index in range(0, num_items - pass_num):
            # Compare items to check if they are out of order
            if items[index] > items[index + 1]:
                # Swap the items
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
                swapped = True
        pass_num = pass_num + 1
        print(items) # Testing


def main():
    """Perform a bubble sort on the test data"""
    #test_items = [80,64,50,43,35,21,7,3,2] # Least sorted
    #test_items = [2,3,7,35,43,21,50,64,80] # Nearly sorted
    #test_items = [2,3,7,21,35,43,50,64,80] # Sorted
    test_items = [43,21,2,50,3,80,35,7,64] # Random
    
    print("### Bubble sort version 3 (while and for loops improved) ###")
    print(test_items)
    
    bubble_sort_version_3(test_items)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
