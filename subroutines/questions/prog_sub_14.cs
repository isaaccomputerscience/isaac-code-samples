  
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
    class Program
    {
        static void Main(string[] args){
            find_y(5, 2, 3);
        }

        static int multiply(int a, int b){
            return a * b;
        }

        static int add(int a, int b){
            return a + b;
        }

        static void find_y(int x, int m, int c){
            Console.Write($"x={x} y=");
            Console.WriteLine(add(multiply(m, x), c));
        }
    }
}
