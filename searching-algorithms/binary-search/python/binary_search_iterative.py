# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def binary_search(items, search_item):
    """An iterative binary search algorithm"""
  
    # Initialise the variables
    found = False
    found_index = -1
    first = 0
    last = len(items) - 1

    # Repeat while there are still items between first and last 
    # and the search item has not been found
    while first <= last and found == False:

        # Find the midpoint position (in the middle of the range)
        midpoint = (first + last) // 2

        # Compare the item at the midpoint to the search item
        if items[midpoint] == search_item:
            # If the item has been found, store the midpoint position
            found_index = midpoint
            found = True # Raise the flag to stop the loop

        # Check if the item at the midpoint is less than the search item    
        elif items[midpoint] < search_item:
            # Focus on the items after the midpoint
            first = midpoint + 1

        # Otherwise the item at the midpoint is greater than the search item  
        else:
            # Focus on the items before the midpoint
            last = midpoint - 1

    # Return the position of the search_item or -1 if not found
    return found_index


def main():
    """Perform a binary search on the test data"""
    test_items = [10,11,13,15,18,25,29]
    
    print("### Binary search (iterative) ###")
    print(test_items)

    # Search for a value and return the found index
    index = binary_search(test_items, 18)

    if index == -1:
        print("The item was not found in the list")
    else:
        print(f"The item was found at index {index}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
