/*
Isaac Computer Science
Usage licensed under the Open Government Licence v3.0
Note: This file is designed to be copied out and compiled on your machine.
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file.
To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Change the namespace to match your project (if neccesary)
4. Compile the program
5. Run the program
*/

using System;

namespace IsaacCodeSamples
{

    class BinarySearch  // Iterative version
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
           test(); 
        }
        

        // Binary search iterative version
        public static int BinarySearch(int[] items, int search_item){
            // Initialise variables
            int index = -1;
            bool found = false;
            int first = 0;
            int last = items.Length - 1;

            // Repeat while there are more items to check and the item has not yet been found.
            while(first <= last && found == false){
                int midpoint = (first + last) / 2;
                if (items[midpoint] == search_item){
                    index = midpoint;
                    found = true;
                }else if (items[midpoint] < search_item){
                    first = midpoint + 1;
                }else{
                    last = midpoint - 1;
                }
            }
            return index;
        }


        // Test function for binary search
        private static void test() {
            int[] items = new int[]{5, 12, 24, 56, 68, 72, 81, 95};

            // Search for first item in array
            Console.WriteLine("Searching for first item in array...");
            int result = BinarySearch(items, 5);
            Console.WriteLine("The search result was: " + result.ToString());

            // Search for last item in array
            Console.WriteLine("Searching for last item in array...");
            result = BinarySearch(items, 95);
            Console.WriteLine("The search result was: " + result.ToString());

            // Search for an item that is not in the array
            Console.WriteLine("Searching for last item in array...");
            result = BinarySearch(items, 36);
            Console.WriteLine("The search result was: " + result.ToString());
        }
        
        
    }
}
