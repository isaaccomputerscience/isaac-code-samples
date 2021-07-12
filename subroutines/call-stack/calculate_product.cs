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
    class CallStackExample
    {
        // Simple program to demonstrate the use of call stacks
        static void Main(string[] args){

            Console.WriteLine("Please enter a number");
            string num1_input = Console.ReadLine();
            int num1 = Convert.ToInt32(num1_input);
            Console.WriteLine("Please enter another number");
            string num2_input = Console.ReadLine();
            int num2 = Convert.ToInt32(num2_input);
            CalculateProduct(num1, num2);

        }

        // Calculates the product of two numbers
        static void CalculateProduct(int n1, int n2){

            int product = n1 * n2;
            Console.WriteLine(product);

        }
    }
}
