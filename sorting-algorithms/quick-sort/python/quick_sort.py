# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def quick_sort(items, start, end):
    """"A recursive quick sort algorithm"""
    
    # Base case for recursion:
    # The recursion will stop when the partition contains a single item
    if start >= end:
        return

    # Otherwise recursively call the function
    else:
        pivot_value = items[start] # Set to first item in the partition
        low_mark = start + 1 # Set to second position in the partition
        high_mark = end # Set to last position in the partition
        finished = False
        
        print(f"{items} Pivot value: {pivot_value}  Low mark: {low_mark}  High mark: {high_mark}")
        
        # Repeat until low and high values have been swapped as needed
        while finished == False:
            
            # Move the left pivot
            while low_mark <= high_mark and items[low_mark] <= pivot_value:
                low_mark = low_mark + 1 # Increment low_mark
                
             # Move the right pivot                               
            while items[high_mark] >= pivot_value and high_mark >= low_mark:
                high_mark = high_mark - 1 # Decrement high_mark

            # Check that the low mark doesn't overlap with the high mark
            if low_mark < high_mark:
                # Swap the values at low_mark and high_mark
                temp = items[low_mark]
                items[low_mark] = items[high_mark]
                items[high_mark] = temp
                print(f"{items} Swapped the values {items[high_mark]} and {items[low_mark]}") # Testing
                
            # Otherwise end the loop
            else:
                finished = True
            
        # Swap the pivot value and the value at high_mark
        temp = items[start]
        items[start] = items[high_mark]
        items[high_mark] = temp
        print(f"{items} Swapped the pivot value {pivot_value} and {items[start]}\n") # Testing

   
        # Recursive call on the left partition
        quick_sort(items, start, high_mark - 1)

        # Recursive call on the right partition
        quick_sort(items, high_mark + 1, end)
    return items


def main():
    """Perform a quick sort on the test data"""
    #test_items = [80,64,50,43,35,21,7,3,2] # Least sorted
    #test_items = [2,3,7,35,43,21,50,64,80] # Nearly sorted
    #test_items = [2,3,7,21,35,43,50,64,80] # Sorted
    test_items = [43,21,2,50,3,80,35,7,64] # Random
    
    print("### Quick sort (recursive) ###")
    print(f"\nOriginal items {test_items} \n")

    # Assign the returned sorted array
    sorted_items = quick_sort(test_items, 0, len(test_items)-1)

    print(f"Sorted items {sorted_items}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
