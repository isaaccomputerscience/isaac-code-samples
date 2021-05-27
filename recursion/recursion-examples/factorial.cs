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
    class FactorialRecursive
    {
        static void Main(string[] args){
            int n = 5;
            int result = Factorial(n);
            Console.WriteLine(String.Format("{0}! is {1}", n.ToString(), result.ToString()));
        }

        public static int Factorial(int n){
            //returns the value of n!
            if (n == 1){
                return 1;
            }else{
                return n * Factorial(n-1);
            }
        }
    }
}