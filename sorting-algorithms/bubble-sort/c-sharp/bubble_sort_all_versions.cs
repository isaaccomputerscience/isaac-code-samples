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
            // Execute all three versions of the bubble sort algorithms
            Console.WriteLine("\n### Bubble sort version 1 (for loops) ###");
            BubbleSortVersion1(GetTestData());
            
            Console.WriteLine("\n### Bubble sort version 2 (while and for loops) ###");
            BubbleSortVersion2(GetTestData());
            
            Console.WriteLine("\n### Bubble sort version 3 (while and for loops improved) ###");
            BubbleSortVersion3(GetTestData());
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


        // An inefficient bubble sort that uses nested for loops
        public static void BubbleSortVersion1(int[] items)
        {
            int numItems = items.Length;
            int passNum; // Declared outside of the for loop for testing below

            for (passNum = 1; passNum < numItems; passNum++) {
                int index = 0; // Declared outside of the for loop for testing below
                for (index = 0; index < numItems - 1; index++) {
                    if (items[index] > items[index + 1]) {
                        int temp = items[index];
                        items[index] = items[index + 1];
                        items[index + 1] = temp;
                    }
                }
                // Testing
                Console.Write($"Pass {passNum}: ");
                Console.Write("[{0}]", string.Join(", ", items)); 
                Console.WriteLine($"  Comparisons: {index+1}");
            }
        }


        // A quite efficient bubble sort that stops if the items are sorted
        public static void BubbleSortVersion2(int[] items)
        {
            int numItems = items.Length;
            bool swapped = true;
            int passNum = 1; // Testing

            while (swapped == true) {
                swapped = false;
                int index = 0; // Declared outside of the for loop for testing below
                for (index = 0; index < numItems - 1; index++) {
                    if (items[index] > items[index + 1]) {
                        int temp = items[index];
                        items[index] = items[index + 1];
                        items[index + 1] = temp;
                        swapped = true;
                    }
                }
                // Testing
                Console.Write($"Pass {passNum}: ");
                Console.Write("[{0}]", string.Join(", ", items)); 
                Console.WriteLine($"  Comparisons: {index+1}");
                
                passNum = passNum + 1;
            }
        }


        // A more efficient bubble sort that reduces the number of comparisons per pass
        public static void BubbleSortVersion3(int[] items)
        {
            int numItems = items.Length;
            bool swapped = true;
            int passNum = 1;

            while (swapped == true) {
                swapped = false;
                int index = 0; // Declared outside of the for loop for testing below
                for (index = 0; index < numItems - passNum; index++) {
                    if (items[index] > items[index + 1]) {
                        int temp = items[index];
                        items[index] = items[index + 1];
                        items[index + 1] = temp;
                        swapped = true;
                    }
                }
                // Testing
                Console.Write($"Pass {passNum}: ");
                Console.Write("[{0}]", string.Join(", ", items)); 
                Console.WriteLine($"  Comparisons: {index+1}");
                
                passNum = passNum + 1;
            }
        }

        
    }
}