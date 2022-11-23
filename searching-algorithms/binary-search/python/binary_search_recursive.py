# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def binary_search_recursive(items, search_item, first, last):
    """A recursive binary search algorithm"""

    # Base case for recursion: The recursion will stop when the
    # index of the first item is greater than the index of last
    if first > last:
        return -1 # Return -1 if the search item is not found

    # Recursively call the function
    else:
        # Find the midpoint position (in the middle of the range)
        midpoint = (first + last) // 2
        
        # Compare the item at the midpoint to the search item
        if items[midpoint] == search_item:
            # If the item has been found, return the midpoint position
            return midpoint
     
        # Check if the item at the midpoint is less than the search item 
        elif items[midpoint] < search_item:
            # Focus on the items after the midpoint
            first = midpoint + 1
            return binary_search_recursive(items, search_item, first, last)

        # Otherwise the item at the midpoint is greater than the search item
        else:
            # Focus on the items before the midpoint
            last = midpoint - 1 
            return binary_search_recursive(items, search_item, first, last)


def main():
    """Perform a binary search on the test data"""
    test_items = [10,11,13,15,18,25,29]

    first_index = 0
    last_index = len(test_items) - 1
    
    print("### Binary search (recursive) ###")
    print(test_items)

    # Search for a value and return the found index
    index = binary_search_recursive(test_items, 18, first_index, last_index)

    if index == -1:
        print("The item was not found in the list")
    else:
        print(f"The item was found at index {index}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
