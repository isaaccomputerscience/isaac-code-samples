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

namespace Recursion
{
    class RecursionExamples
    {
        // The Main method is the entry point for all C# programs
        static void Main(string[] args) {
            int x = 259;
            int y = 111;
            int answer = GCD(x, y);
            string output = $"The lowest common denominator of {x} and {y} is {answer}";
            Console.WriteLine(output);
        }
        

        // Euclidian algorithm to find greatest common denominator
        public static int GCD(int x, int y){
            if (y == 0) {
                return x;
            } else {
                return GCD(y, x % y);
            }
        }
        
        
    }
}
