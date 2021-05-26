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
    '''test script for binary search'''
    # Create a list containing some names
    items = ['Albie', 'Byron', 'Divya', 'Hari', 'Joanne', 'Kim', 'Wilbur', 'Zoe'] 
    
    # Search for first item in the list
    print ('Searching for first name in the list')
    result = binary_search(items, 'Albie')
    print ('Result of search was {}'.format(result))
    
    # Search for last item in the list
    print ('Searching for the last name in the list')
    result = binary_search(items, 'Zoe')
    print ('Result of search was {}'.format(result))
    
    # Search for an item that is not in the list
    print ('Searching for a name that is not in the list')
    result = binary_search(items, 'Boris')
    print ('Result of search was {}'.format(result))

if __name__ == '__main__':
    test()
