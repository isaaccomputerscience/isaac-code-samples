def binary_search (items, search_item, first, last):
    """Binary search - recursive version."""
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
    print ("Searching for first name in the list")
    result = binary_search(items, "Albie", first, last)
    print ('Result of search was {}'.format(result))
    
    # Search for last item in the list
    print ('Searching for the last name in the list')
    result = binary_search(items, "Zoe", first, last)
    print ('Result of search was {}'.format(result))
    
    # Search for an item that is not in the list
    print ('Searching for a name that is not in the list')
    result = binary_search(items, "Boris", first, last)
    print ('Result of search was {}'.format(result))

if __name__ == '__main__':
    test()
