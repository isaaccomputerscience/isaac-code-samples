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
            // Perform a bubble sort on the test data
            //int[] testItems = new int[] {80, 64, 50, 43, 35, 21, 7, 3, 2}; // Least sorted
            //int[] testItems = new int[] {2, 3, 7, 35, 43, 21, 50, 64, 80}; // Nearly sorted
            //int[] testItems = new int[] {2, 3, 7, 21, 35, 43, 50, 64, 80}; // Sorted
            int[] testItems = new int[] {43, 21, 2, 50, 3, 80, 35, 7, 64}; // Random

            Console.WriteLine("### Bubble sort version 1 (for loops) ###");
            Console.WriteLine("[{0}]", string.Join(", ", testItems));

            BubbleSortVersion1(testItems);
        }


        // An inefficient bubble sort that uses nested for loops
        public static void BubbleSortVersion1(int[] items)
        {
            // Initialise the variables
            int numItems = items.Length;

            // Pass through the array of items n-1 times
            for (int passNum = 1; passNum < numItems; passNum++) {
                // Perform a pass
                for (int index = 0; index < numItems - 1; index++) {
                    // Compare items to check if they are out of order
                    if (items[index] > items[index + 1]) {
                        // Swap the items
                        int temp = items[index];
                        items[index] = items[index + 1];
                        items[index + 1] = temp;
                    }
                }
                Console.WriteLine("[{0}]", string.Join(", ", items)); // Testing
            }
        }

        
    }
}