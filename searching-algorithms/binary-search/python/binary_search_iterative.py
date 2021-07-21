# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def binary_search(items, search_item):
    """Returns index or -1 if not found"""
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


def run_test():
    """Test script for binary search"""
    # Ordered list of names
    items = ["Albie", "Byron", "Divya", "Hari", "Joanne", "Kim", "Wilbur", "Zoe"] 
    
    # Search for first item in list.
    print("Searching for name at start of list")
    result = binary_search(items, "Albie")
    print(f"Result of search was {result}")
    
    # Search for last item in list.
    print("Searching for name at end of list")
    result = binary_search(items, "Zoe")
    print(f"Result of search was {result}")
    
    # Search for an item not in list.
    print("Searching for name that is not in list")
    result = binary_search(items, "Boris")
    print(f"Result of search was {result}")
    

if __name__ == "__main__":
    run_test()
