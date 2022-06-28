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

        # Get the position of the previous item
        previous = index - 1

        # Repeat while there are previous items to check and the
        # value of the previous item is higher than the item to insert
        while previous >= 0 and items[previous] > item_to_insert:
            print(f"{items}  Previous position value: {items[previous]}") # Testing
            
            # Copy the previous item up one place
            items[previous + 1] = items[previous]

            # Get the position of the next previous item
            previous = previous - 1
            
        print(f"{items}  Correct position found: Index {previous+1}") # Testing

        # Copy the value of the item to insert into the correct position
        items[previous + 1] = item_to_insert
        
        print(f"{items}  Item inserted into index {previous+1}") # Testing


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
