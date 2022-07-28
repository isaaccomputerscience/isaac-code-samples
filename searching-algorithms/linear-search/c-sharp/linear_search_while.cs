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
            // Perform a linear search on the test data
            int[] testItems = new int[] {11, 25, 10, 29, 15, 13, 18};

            Console.WriteLine("### Linear search version 2 (while loop) ###");
            Console.WriteLine("[{0}]", string.Join(", ", testItems));

            // Search for a value and return the found index
            int index = LinearSearchVersion2(testItems, 15);

            if (index == -1) {
                Console.WriteLine("The item was not found in the array");
            }
            else {
                Console.WriteLine($"The item was found at index {index}");
            }
        }


        // A linear search algorithm that stops iterating if the item is found
        public static int LinearSearchVersion2(int[] items, int searchItem) 
        {
            // Initialise the variables
            int found_index = -1;
            int current = 0;
            bool found = false;

            // Repeat while the end of the array has not been reached
            // and the search item has not been found
            while (found == false && current < items.Length) {

                // Compare the item at the current index to the search item
                if (items[current] == searchItem) {
                    // If the item has been found, store the current index 
                    found_index = current;
                    found = true; // Raise the flag to stop the loop
                }
                current = current + 1; // Go to the next index in the array
            }
            // Return the index of the searchItem or -1 if not found
            return found_index;
        }
   
        
    }
}