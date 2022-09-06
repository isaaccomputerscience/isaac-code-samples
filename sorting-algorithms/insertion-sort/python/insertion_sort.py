# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def insertion_sort(items):
    """"An insertion sort algorithm"""
    # Initialise the variables
    num_items = len(items)

    # Repeat for each item in the list, starting at the second item
    for index in range(1, num_items):
        # Get the value of the next item to insert
        item_to_insert = items[index] 
        print(f"\nItem to insert: {item_to_insert}") # Testing

        # Get the current position of the last sorted item
        position = index - 1

        # Repeat while there are still items in the list to check
        # and the current sorted item is greater than the item to insert
        while position >= 0 and items[position] > item_to_insert:
            print(f"{items}  Current item: {items[position]} (index {position})") # Testing
            
            # Copy the value of the sorted item up one place
            items[position + 1] = items[position]

            # Get the position of the next sorted item
            position = position - 1
            
        print(f"{items}  Correct position found at index {position+1}") # Testing

        # Copy the value of the item to insert into the correct position
        items[position + 1] = item_to_insert
        
        print(f"{items}  Item inserted into index {position+1}") # Testing


def main():
    """Perform an insertion sort on the test data"""
    #test_items = [80,64,50,43,35,21,7,3,2] # Least sorted
    #test_items = [2,3,7,35,43,21,50,64,80] # Nearly sorted
    #test_items = [2,3,7,21,35,43,50,64,80] # Sorted
    test_items = [43,21,2,50,3,80,35,7,64] # Random
    
    print("\n### Insertion sort ###")
    print("Original list")
    print(test_items)

    insertion_sort(test_items)

    print("\nSorted list")
    print(test_items)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
