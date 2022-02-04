# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def binary_search(items, search_item, first, last):
    """Binary search recursive version"""
    if first > last:
        return -1
    else:
        midpoint = (first + last) // 2
        if items[midpoint] == search_item:
            return midpoint
        elif search_item > items[midpoint]:
            first = midpoint + 1
            return binary_search(items, search_item, first, last)
        else:
            last = midpoint - 1 
            return binary_search(items, search_item, first, last)
            

def test():
    """Test script for binary search."""
    # Create a list containing some names
    items = ["Albie", "Byron", "Divya", "Hari", "Joanne", "Kim", "Wilbur", "Zoe"] 
    first = 0
    last = 7
    
    # Search for first item in the list
    print("Searching for first name in the list")
    result = binary_search(items, "Albie", first, last)
    print(f"Result of search was {result}")
    
    # Search for last item in the list
    print("Searching for last name in list")
    result = binary_search(items, "Zoe", first, last)
    print(f"Result of search was {result}")
    
    # Search for an item that is not in the list
    print("Searching for a name that is not in the list")
    result = binary_search(items, "Boris", first, last)
    print(f"Result of search was {result}")


# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':
    test()
