# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def bubble_sort(items):
    """A bubble sort algorithm (while and for loops improved)"""
    # Initialise the variables
    num_items = len(items)
    swapped = True
    pass_num = 1
    total_comparisons = 0 # Testing

    # Repeat while one or more swaps have been made
    while swapped == True:
        swapped = False
        # Perform a pass, reducing the number of comparisons each time
        for index in range(0, num_items - pass_num):
            # Compare items to check if they are out of order
            if items[index] > items[index + 1]:
                # Swap the items
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
                swapped = True
            total_comparisons = total_comparisons + 1 # Testing
        print(f"Pass {pass_num}: {items}   Comparisons: {index+1}") # Testing
        pass_num = pass_num + 1

    print(f"Total comparisons: {total_comparisons}") # Testing


def insertion_sort(items):
    """"An insertion sort algorithm"""
    # Initialise the variables
    num_items = len(items)
    total_comparisons = 0 # Testing

    # Repeat for each item in the list, starting at the second item
    for index in range(1, num_items):
        # Get the value of the next item to insert
        item_to_insert = items[index] 

        # Get the current position of the last sorted item
        position = index - 1

        # Testing
        comparisons = 1
        total_comparisons = total_comparisons + 1

        # Repeat while there are still items in the list to check
        # and the current sorted item is greater than the item to insert
        while position >= 0 and items[position] > item_to_insert:
            # Copy the value of the sorted item up one place
            items[position + 1] = items[position]

            # Get the position of the next sorted item
            position = position - 1

            # Testing
            comparisons = comparisons + 1
            total_comparisons = total_comparisons + 1
            
        # Copy the value of the item to insert into the correct position
        items[position + 1] = item_to_insert
        
        print(f"Pass {index}: {items}   Comparisons: {comparisons}") # Testing

    print(f"Total comparisons: {total_comparisons}") # Testing


def get_test_data():
    """Returns the test data for the algorithm"""
    #test_items = [80,64,50,43,35,21,7,3,2] # Least sorted
    #test_items = [2,3,7,35,43,21,50,64,80] # Nearly sorted
    #test_items = [2,3,7,21,35,43,50,64,80] # Sorted
    test_items = [43,21,2,50,3,80,35,7,64] # Random

    print(f"Data: {test_items}")
    
    return test_items


def main():
    """Compare a bubble sort with an insertion sort algorithm"""    
    print("\n### Bubble sort (while and for loops improved) ###")
    bubble_sort(get_test_data())
    
    print("\n### Insertion sort ###")
    insertion_sort(get_test_data())



# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
