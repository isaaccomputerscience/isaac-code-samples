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
            // Perform a bubble sort on the test data
            //int[] testItems = new int[] {80, 64, 50, 43, 35, 21, 7, 3, 2}; // Least sorted
            //int[] testItems = new int[] {2, 3, 7, 35, 43, 21, 50, 64, 80}; // Nearly sorted
            //int[] testItems = new int[] {2, 3, 7, 21, 35, 43, 50, 64, 80}; // Sorted
            int[] testItems = new int[] {43, 21, 2, 50, 3, 80, 35, 7, 64}; // Random

            Console.WriteLine("### Bubble sort version 2 (while and for loops) ###");
            Console.WriteLine("[{0}]", string.Join(", ", testItems));

            BubbleSortVersion2(testItems);
        }


        // A quite efficient bubble sort that stops if the items are sorted
        public static void BubbleSortVersion2(int[] items)
        {
            // Initialise the variables
            int numItems = items.Length;
            bool swapped = true;

            // Repeat while one or more swaps have been made
            while (swapped == true) {
                swapped = false;
                // Perform a pass
                for (int index = 0; index < numItems - 1; index++) {
                    // Compare items to check if they are out of order
                    if (items[index] > items[index + 1]) {
                        // Swap the items
                        int temp = items[index];
                        items[index] = items[index + 1];
                        items[index + 1] = temp;
                        swapped = true;
                    }
                }
                Console.WriteLine("[{0}]", string.Join(", ", items)); // Testing
            }
        }

        
    }
}