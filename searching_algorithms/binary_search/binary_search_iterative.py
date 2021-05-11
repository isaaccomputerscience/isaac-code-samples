def binary_search (items, search_item):
    '''ICS iterative version'''
    index = -1
    found = False
    first = 0
    last = len(items) - 1
        
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if items[midpoint] == search_item:
            index = midpoint
            found = True  
        elif items[midpoint] < search_item: 
            first = midpoint + 1 
        else: 
            last = midpoint - 1       
    return index

def test():
    '''test script for binary serach'''
    # Create a list containing numbers 0 to 7
    items = [] 
    for i in range(8):
        items.append(i)
    # Search for first item in the list
    print ('Searching for first item in the list')
    result = binary_search(items, 0)
    if result != 0:
        print ('test failed')
    else:
        print ('test passed')
    # Search for last item in the list
        print ('Searching for last item in the list')
    result = binary_search(items, 7)
    if result != 7:
        print ('test failed')
    else:
        print ('test passed')
    # Search an item that is not in the list
    print ('Searching for item that is not in the list')
    result = binary_search(items, 12)
    if result != -1:
        print ('test failed')
    else:
        print ('test passed')

if __name__ == '__main__':
    test()
