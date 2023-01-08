# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def bubble_sort_version_1(items):
    """An inefficient bubble sort that uses nested for loops"""
    num_items = len(items)
    
    for pass_num in range(1, num_items): # pseudocode: num_items - 1
        for index in range(0, num_items - 1): # pseudocode: num_items - 2
            if items[index] > items[index + 1]:
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
        print(f"Pass {pass_num}: {items}   Comparisons: {index+1}") # Testing


def bubble_sort_version_2(items):
    """A quite efficient bubble sort that stops if the items are sorted"""
    num_items = len(items)
    swapped = True
    pass_num = 1 # Testing
    
    while swapped:
        swapped = False
        for index in range(0, num_items - 1): # pseudocode: num_items - 2
            if items[index] > items[index + 1]:
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
                swapped = True
        print(f"Pass {pass_num}: {items}   Comparisons: {index+1}") # Testing
        pass_num = pass_num + 1 # Testing


def bubble_sort_version_3(items):
    """A more efficient bubble sort that reduces the number of comparisons per pass"""
    num_items = len(items)
    swapped = True
    pass_num = 1
    
    while swapped:
        swapped = False # Assume sorted
        for index in range(0, num_items - pass_num): # pseudocode: num_items - 1 - pass_num
            if items[index] > items[index + 1]:
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp
                swapped = True
        print(f"Pass {pass_num}: {items}   Comparisons: {index+1}") # Testing
        pass_num = pass_num + 1


def get_test_data():
    """Returns the test data for the algorithm"""
    #test_items = [80,64,50,43,35,21,7,3,2] # Least sorted
    #test_items = [2,3,7,35,43,21,50,64,80] # Nearly sorted
    #test_items = [2,3,7,21,35,43,50,64,80] # Sorted
    test_items = [43,21,2,50,3,80,35,7,64] # Random

    print(f"Data: {test_items}")
    
    return test_items


def main():
    """Execute all three versions of the bubble sort algorithms"""
    print("\n### Bubble sort version 1 (for loops) ###")
    bubble_sort_version_1(get_test_data())
    
    print("\n### Bubble sort version 2 (while and for loops) ###")
    bubble_sort_version_2(get_test_data())
    
    print("\n### Bubble sort version 3 (while and for loops improved) ###")
    bubble_sort_version_3(get_test_data())


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
