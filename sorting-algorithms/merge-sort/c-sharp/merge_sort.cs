/*
Raspberry Pi Foundation
Developed to be used alongside Isaac Computer Science, part of the National Centre for Computing Education
Usage licensed under CC BY-SA 4

Note: This file is designed to be copied out and compiled on your machine.
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file.
To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Change the namespace to match your project (if necessary)
4. Compile the program
5. Run the program
*/

using System;

namespace IsaacCodeSamples
{
    class SortingAlgorithms
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Perform a merge sort on the test data
            //int[] testItems = new int[] {80, 64, 50, 43, 35, 21, 7, 3, 2}; // Least sorted
            //int[] testItems = new int[] {2, 3, 7, 35, 43, 21, 50, 64, 80}; // Nearly sorted
            //int[] testItems = new int[] {2, 3, 7, 21, 35, 43, 50, 64, 80}; // Sorted
            int[] testItems = new int[] {43, 21, 2, 50, 3, 80, 35, 7, 64}; // Random

            Console.WriteLine("### Merge sort (recursive) ###");
            Console.Write("Original items ");
            Console.WriteLine("[{0}]", string.Join(", ", testItems));
            
            int[] sortedItems = MergeSort(testItems); // Assign the returned sorted array

            Console.Write("Sorted items ");
            Console.WriteLine("[{0}]", string.Join(", ", sortedItems));
        }


        // A recursive merge sort algorithm
        public static int[] MergeSort(int[] items)
        {
            int[] leftHalf; // Stores items in the left half of the items array
            int[] rightHalf; // Stores items in the right half of the items array
            int[] mergedItems = new int[items.Length]; // Stores the merged items in each recursive call

            Console.Write("Splitting ");
            Console.WriteLine("[{0}]", string.Join(", ", items));

            // Base case for recursion:
            // The recursion will stop when the array has been divided into single items
            if (items.Length <= 1)
                return items;
            else {
                int midpoint = (items.Length - 1) / 2; // Calculate the midpoint index
                int leftSize = midpoint + 1; // Size of the left half array
                int rightSize; // Size of the right half array

                // Check if the total number of items is even
                if (items.Length % 2 == 0)
                    rightSize = midpoint + 1; // Left and right arrays are equal in size
                else
                    rightSize = midpoint; // Right array will have one less item than left array

                leftHalf = new int[leftSize]; // Create left half array
                rightHalf = new int[rightSize]; // Create right half array

                // Populate left half array with the items up to and including the midpoint
                for (int i = 0; i < leftSize; i++)
                    leftHalf[i] = items[i];

                // Populate right half array with the items after the midpoint
                int indexItems = midpoint + 1;
                for (int i = 0; i < rightSize; i++) {
                    rightHalf[i] = items[indexItems];
                    indexItems++;
                }

                leftHalf = MergeSort(leftHalf); // Recursive call on left half
                rightHalf = MergeSort(rightHalf); // Recursive call on right half

                Console.Write("Items before merge "); // Testing
                Console.WriteLine("[{0}]", string.Join(", ", items));

                mergedItems = Merge(leftHalf, rightHalf); // Call function to merge both halves

                Console.Write("Merged items "); // Testing
                Console.WriteLine("[{0}]", string.Join(", ", mergedItems));
                Console.WriteLine();

                return mergedItems;
            }
        }
  
        // Merges the items in left and right into a new ordered list called merged
        public static int[] Merge(int[] left, int[] right)
        {
            int mergedSize = left.Length + right.Length; // Size of the new array
            int[] merged = new int[mergedSize]; // New array for merging the items
            
            int indexLeft = 0; // left current position
            int indexRight = 0; // right current position
            int indexMerged = 0; // merged current position

            // While there are still items to merge
            while (indexLeft < left.Length && indexRight < right.Length) {
                // Find the lowest of the two items being compared and add it to the new array 
                if (left[indexLeft] < right[indexRight]) {
                    merged[indexMerged] = left[indexLeft];
                    indexLeft++;
                    indexMerged++;
                }
                else {
                    merged[indexMerged] = right[indexRight];
                    indexRight++;
                    indexMerged++;
                }
            }

            // Add to the merged array any remaining data from left array
            while (indexLeft < left.Length) {
                merged[indexMerged] = left[indexLeft];
                indexLeft++;
                indexMerged++;
            }

            // Add to the merged array any remaining data from right array
            while (indexRight < right.Length) {
                merged[indexMerged] = right[indexRight];
                indexRight++;
                indexMerged++;
            }

            return merged;
        }

        
    }
}