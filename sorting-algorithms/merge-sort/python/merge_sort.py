# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def merge_sort(items):
    """"A recursive merge sort algorithm"""
    print("Splitting", items)

    # Base case for recursion:
    # The recursion will stop when the list has been divided into single items
    if len(items) <= 1:
        return items
    else:
        midpoint = (len(items)-1) // 2 # Calculate the midpoint index
        left_half = items[0:midpoint+1] # Create left half list
        right_half = items[midpoint+1:len(items)] # Create right half list

        left_half = merge_sort(left_half) # Recursive call on left half
        right_half = merge_sort(right_half) # Recursive call on right half
        
        print(f"Items before merge {items}") # Testing

        # Call procedure to merge both halves
        merged_items = merge(left_half, right_half) # Call function to merge both halves

        print(f"Merged items {merged_items} \n") # Testing

        return merged_items


def merge(left, right):
    """Merges the items in left and right into a new ordered list called merged"""
    merged = [] # New list for merging the items
    index_left = 0 # left current position
    index_right = 0 # right current position

    # While there are still items to merge
    while index_left < len(left) and index_right < len(right):

        # Find the lowest of the two items being compared 
        # and add it to the new list
        if left[index_left] < right[index_right]:
            merged.append(left[index_left])
            index_left += 1
        else:
            merged.append(right[index_right])
            index_right += 1

    # Add to the merged list any remaining data from left list
    while index_left < len(left):
        merged.append(left[index_left])
        index_left += 1

    # Add to the merged list any remaining data from right list
    while index_right < len(right):
        merged.append(right[index_right])
        index_right += 1

    return merged


def main():
    """Perform a merge sort on the test data"""
    #test_items = [80,64,50,43,35,21,7,3,2] # Least sorted
    #test_items = [2,3,7,35,43,21,50,64,80] # Nearly sorted
    #test_items = [2,3,7,21,35,43,50,64,80] # Sorted
    test_items = [43,21,2,50,3,80,35,7,64] # Random
    
    print("### Merge sort (recursive) ###")
    print(f"Original items {test_items} \n")

    sorted_items = merge_sort(test_items) # Assign the returned sorted array

    print(f"Sorted items {sorted_items}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
