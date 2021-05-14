using System;

namespace isaac_code_samples
{
    class BinarySearchRecursive
    {
        static void Main(string[] args){
           test(); 
        }

        public static int BinarySearch(int[] items, int search_item){
            // Binary search iterative version
            //Initialise variables
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

        private static void test(){
            int[] items = new int[]{5, 12, 24, 56, 68, 72, 81, 95};

            //Search for first item in array
            Console.WriteLine("Searching for first item in array...");
            int result = BinarySearch(items, 5);
            Console.WriteLine("The search result was: " + result.ToString());

            //Search for last item in array
            Console.WriteLine("Searching for last item in array...");
            result = BinarySearch(items, 95);
            Console.WriteLine("The search result was: " + result.ToString());

            //Search for an item that is not in the array
            Console.WriteLine("Searching for last item in array...");
            result = BinarySearch(items, 36);
            Console.WriteLine("The search result was: " + result.ToString());
        }
    }
}