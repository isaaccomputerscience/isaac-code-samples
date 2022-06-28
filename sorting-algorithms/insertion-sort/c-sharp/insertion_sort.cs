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
            // Perform an insertion sort on the test data
            //int[] testItems = new int[] {80, 64, 50, 43, 35, 21, 7, 3, 2}; // Least sorted
            //int[] testItems = new int[] {2, 3, 7, 35, 43, 21, 50, 64, 80}; // Nearly sorted
            //int[] testItems = new int[] {2, 3, 7, 21, 35, 43, 50, 64, 80}; // Sorted
            int[] testItems = new int[] {43, 21, 2, 50, 3, 80, 35, 7, 64}; // Random

            Console.WriteLine("\n### Insertion sort ###");
            Console.WriteLine("Original array");
            Console.WriteLine("[{0}]", string.Join(", ", testItems));

            int[] returnedItems = InsertionSort(testItems);

            Console.WriteLine("\nSorted array");
            Console.WriteLine("[{0}]", string.Join(", ", returnedItems));
        }


        // An insertion sort algorithm
        public static int[] InsertionSort(int[] items)
        {
            // Initialise the variables
            int numItems = items.Length;

            // Repeat for each item in the list, starting at the second item
            for (int index = 1; index < numItems; index++) {
                // Get the value of the next item to insert
                int itemToInsert = items[index];
                Console.WriteLine($"\nItem to insert: {itemToInsert}"); // Testing

                // Get the position of the previous item
                int previous = index - 1;

                // Repeat while there are previous items to check and the
                // value of the previous item is higher than the item to insert
                while (previous >= 0 && items[previous] > itemToInsert) {
                    // Testing
                    Console.Write("[{0}]", string.Join(", ", items));
                    Console.WriteLine($"  Previous position value: {items[previous]}");
                    
                    // Copy the previous item up one place
                    items[previous + 1] = items[previous];

                    // Get the position of the next previous item
                    previous = previous - 1;
                }
                
                // Testing
                Console.Write("[{0}]", string.Join(", ", items));
                Console.WriteLine($"  Correct position found: Index {previous+1}");

                // Copy the value of the item to insert into the correct position
                items[previous + 1] = itemToInsert;
                
                // Testing
                Console.Write("[{0}]", string.Join(", ", items));
                Console.WriteLine($"  Item inserted into index {previous+1}");
            }
            return items; // Testing
        }

        
    }
}