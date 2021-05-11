def binary_search (items, search_item, first, last):
    '''Binary search - recursive version'''
    if first > last:
        return -1
    else:
        midpoint = (first + last) // 2
        if items[midpoint] == search_item:
            return midpoint
        elif search_item > items[midpoint]:
            first = midpoint + 1
            return binary_search (items, search_item, first, last)
        else:
            last = midpoint - 1 
            return binary_search (items, search_item, first, last)

def test():
    '''test script for binary search'''
    # Create a list containing numbers 0 to 7
    items = [] 
    for i in range(8):
        items.append(i)
    # Search for first item in the list
    print ('Searching for first item in the list')
    result = binary_search(items, 0, 0, 7)
    if result != 0:
        print ('test failed')
    else:
        print ('test passed')
    # Search for last item in the list
        print ('Searching for last item in the list')
    result = binary_search(items, 7, 0, 7)
    if result != 7:
        print ('test failed')
    else:
        print ('test passed')
    # Search an item that is not in the list
    print ('Searching for item that is not in the list')
    result = binary_search(items, 12, 0, 7)
    if result != -1:
        print ('test failed')
    else:
        print ('test passed')

if __name__ == '__main__':
    test()
