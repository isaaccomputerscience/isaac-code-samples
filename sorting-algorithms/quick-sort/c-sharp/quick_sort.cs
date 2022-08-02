/*
Isaac Computer Science
Usage licensed under the Open Government Licence v3.0

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
            // Perform a quick sort on the test data
            //int[] testItems = new int[] {80, 64, 50, 43, 35, 21, 7, 3, 2}; // Least sorted
            //int[] testItems = new int[] {2, 3, 7, 35, 43, 21, 50, 64, 80}; // Nearly sorted
            //int[] testItems = new int[] {2, 3, 7, 21, 35, 43, 50, 64, 80}; // Sorted
            int[] testItems = new int[] {43, 21, 2, 50, 3, 80, 35, 7, 64}; // Random

            Console.WriteLine("### Quick sort (recursive) ###");
            Console.Write("\nOriginal items ");
            Console.WriteLine("[{0}]", string.Join(", ", testItems));
            Console.WriteLine();
            
            // Assign the returned sorted array
            int[] sortedItems = QuickSort(testItems, 0, testItems.Length - 1);

            Console.Write("Sorted items ");
            Console.WriteLine("[{0}]", string.Join(", ", sortedItems));
        }


        // A recursive quick sort algorithm
        public static int[] QuickSort(int[] items, int start, int end)
        {
            // Base case for recursion:
            // The recursion will stop when the partition contains a single item
            if (start >= end)
                return new int[0];
                
            // Otherwise recursively call the function
            else {
                int pivotValue = items[start]; // Set to first item in the partition
                int lowMark = start + 1; // Set to second position in the partition
                int highMark = end; // Set to last position in the partition
                int temp;
                bool finished = false;
                
                Console.Write("[{0}]", string.Join(", ", items)); // Testing
                Console.WriteLine($" Pivot value: {pivotValue}  Low mark: {lowMark}  High mark: {highMark}");

                // Repeat until low and high values have been swapped as needed
                while (finished == false) {
                    // Move the left pivot
                    while (lowMark <= highMark && items[lowMark] <= pivotValue) {
                        lowMark = lowMark + 1; // Increment lowMark
                    }
                        
                    // Move the right pivot                               
                    while (items[highMark] >= pivotValue && highMark >= lowMark) {
                        highMark = highMark - 1; // Decrement highMark
                    }

                    // Check that the low mark doesn't overlap with the high mark
                    if (lowMark < highMark) {
                        // Swap the values at lowMark and highMark
                        temp = items[lowMark];
                        items[lowMark] = items[highMark];
                        items[highMark] = temp;
                        
                        Console.Write("[{0}]", string.Join(", ", items)); // Testing
                        Console.WriteLine($" Swapped the values {items[highMark]} and {items[lowMark]}");
                    }

                    // Otherwise end the loop
                    else {
                        finished = true;
                    }
                }
            
                // Swap the pivot value and the value at highMark
                temp = items[start];
                items[start] = items[highMark];
                items[highMark] = temp;
                
                Console.Write("[{0}]", string.Join(", ", items)); // Testing
                Console.WriteLine($" Swapped the pivot value {pivotValue} and {items[start]}\n");
        
                // Recursive call on the left partition
                QuickSort(items, start, highMark - 1);

                // Recursive call on the right partition
                QuickSort(items, highMark + 1, end);

                return items;
            }
        }

        
    }
}