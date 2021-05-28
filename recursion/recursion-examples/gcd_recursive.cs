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
    class GCDRecursive
    {
        static void Main(string[] args){
            int x = 259; 
            int y = 111;            
            int result = GCD(x, y);
            Console.WriteLine(result);
        }

        public static int GCD(int x, int y){
            // Euclidian algorithm to find greatest common denominator
            if (y == 0){
                return x;
            }else{
                return gcd (y, x % y);
            }
        }
    }
}
