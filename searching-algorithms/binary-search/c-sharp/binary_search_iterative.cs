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
    class SearchingAlgorithms
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Perform a binary search on the test data
            int[] testItems = new int[] {10, 11, 13, 15, 18, 25, 29};

            Console.WriteLine("### Binary search (iterative) ###");
            Console.WriteLine("[{0}]", string.Join(", ", testItems));

            // Search for a value and return the found index
            int index = BinarySearch(testItems, 15);

            if (index == -1) {
                Console.WriteLine("The item was not found in the list");
            }
            else {
                Console.WriteLine($"The item was found at index {index}");
            }
        }


        // An iterative binary search algorithm
        public static int BinarySearch(int[] items, int searchItem)
        {
            // Initialise the variables
            bool found = false;
            int foundIndex = -1;
            int first = 0;
            int last = items.Length - 1;
            int midpoint = 0;

            // Repeat while there are still items between first and last 
            // and the search item has not been found
            while (first <= last && found == false) {
                // Find the midpoint position (in the middle of the range)
                midpoint = (first + last) / 2;

                // Compare the item at the midpoint to the search item
                if (items[midpoint] == searchItem) {
                    // If the item has been found, store the midpoint position
                    foundIndex = midpoint;
                    found = true; // Raise the flag to stop the loop
                }
                // Check if the item at the midpoint is less than the search item
                else if (items[midpoint] < searchItem) {
                    // Focus on the items after the midpoint
                    first = midpoint + 1;
                }
                // Otherwise the item at the midpoint is greater than the search item
                else {
                    // Focus on the items before the midpoint
                    last = midpoint - 1;
                }
            } 
            // Return the position of the searchItem or -1 if not found
            return foundIndex;
        }
        

    }
}