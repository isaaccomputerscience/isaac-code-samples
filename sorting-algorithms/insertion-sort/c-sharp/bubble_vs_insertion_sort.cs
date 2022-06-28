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
            // Compare a bubble sort with an insertion sort algorithm
            Console.WriteLine("\n### Bubble sort (while and for loops improved) ###");
            BubbleSort(GetTestData());
            
            Console.WriteLine("\n### Insertion sort ###");
            InsertionSort(GetTestData());
        }


        // Returns the test data for the algorithm
        public static int[] GetTestData()
        {
            //int[] testItems = new int[] {80, 64, 50, 43, 35, 21, 7, 3, 2}; // Least sorted
            //int[] testItems = new int[] {2, 3, 7, 35, 43, 21, 50, 64, 80}; // Nearly sorted
            //int[] testItems = new int[] {2, 3, 7, 21, 35, 43, 50, 64, 80}; // Sorted
            int[] testItems = new int[] {43, 21, 2, 50, 3, 80, 35, 7, 64}; // Random
            
            Console.Write($"Data: ");
            Console.WriteLine("[{0}]", string.Join(", ", testItems));

            return testItems;
        }


        // A bubble sort algorithm (while and for loops improved)
        public static void BubbleSort(int[] items)
        {
            // Initialise the variables
            int numItems = items.Length;
            bool swapped = true;
            int passNum = 1;
            int totalComparisons = 0; // Testing

            // Repeat while one or more swaps have been made
            while (swapped == true) {
                swapped = false;
                int index = 0; // Declared outside of the for loop for testing below
                // Perform a pass, reducing the number of comparisons each time
                for (index = 0; index < numItems - passNum; index++) {
                    // Compare items to check if they are out of order
                    if (items[index] > items[index + 1]) {
                        // Swap the items
                        int temp = items[index];
                        items[index] = items[index + 1];
                        items[index + 1] = temp;
                        swapped = true;
                    }
                    totalComparisons = totalComparisons + 1; // Testing
                }
                
                // Testing
                Console.Write($"Pass {passNum}: ");
                Console.Write("[{0}]", string.Join(", ", items)); 
                Console.WriteLine($"  Comparisons: {index}");

                passNum = passNum + 1;
            }
            Console.WriteLine($"Total comparisons: {totalComparisons}"); // Testing
        }


        // An insertion sort algorithm
        public static void InsertionSort(int[] items)
        {
            // Initialise the variables
            int numItems = items.Length;
            int totalComparisons = 0; // Testing

            // Repeat for each item in the list, starting at the second item
            for (int index = 1; index < numItems; index++) {
                // Get the value of the next item to insert
                int itemToInsert = items[index];

                // Get the position of the previous item
                int previous = index - 1;

                // Testing
                int comparisons = 1;
                totalComparisons = totalComparisons + 1;

                // Repeat while there are previous items to check and the
                // value of the previous item is higher than the item to insert
                while (previous >= 0 && items[previous] > itemToInsert) {
                    // Copy the previous item up one place
                    items[previous + 1] = items[previous];

                    // Get the position of the next previous item
                    previous = previous - 1;
                    // Testing
                    comparisons = comparisons + 1;
                    totalComparisons = totalComparisons + 1; // Testing
                }

                // Copy the value of the item to insert into the correct position
                items[previous + 1] = itemToInsert;
                
                // Testing
                Console.Write($"Pass {index}: ");
                Console.Write("[{0}]", string.Join(", ", items));
                Console.WriteLine($"  Comparisons: {comparisons}");
            }
            Console.WriteLine($"Total comparisons: {totalComparisons}"); // Testing
        }

        
    }
}