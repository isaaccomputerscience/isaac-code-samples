/*
Note: This file is designed to be copied out and compiled on your machine. 
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file. 

To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Compile the program
4. Run the program
*/

using System;

namespace isaac_code_samples
{
    class BinarySearchRecursive
    {
        void Main(string[] args){
           test(); 
        }

        public static int BinarySearch(int[] items, int search_item, int first, int last){
            if (first > last){
                return -1;
            }else{
                int midpoint = (first + last) / 2;
                if (items[midpoint] == search_item){
                    return midpoint;
                }else if (search_item > items[midpoint]){
                    first = midpoint + 1;
                    return BinarySearch(items, search_item, first, last);
                }else{
                    last = midpoint - 1;
                    return BinarySearch(items, search_item, first, last);
                }
            }
        }

        private static void test(){
            int[] items = new int[]{5, 12, 24, 56, 68, 72, 81, 95};

            //Search for first item in array
            Console.WriteLine("Searching for first item in array...");
            int result = BinarySearch(items, 5, 0, items.Length - 1);
            Console.WriteLine("The search result was: " + result.ToString());

            //Search for last item in array
            Console.WriteLine("Searching for last item in array...");
            result = BinarySearch(items, 95, 0, items.Length - 1);
            Console.WriteLine("The search result was: " + result.ToString());

            //Search for an item that is not in the array
            Console.WriteLine("Searching for last item in array...");
            result = BinarySearch(items, 36, 0, items.Length - 1);
            Console.WriteLine("The search result was: " + result.ToString());
        }
    }
}
