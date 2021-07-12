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

            Console.WriteLine("Enter hours worked ");
            string hours_input = Console.ReadLine();
            int hours_float = Convert.ToInt32(num1_input);
            Console.WriteLine("Enter hourly rate ");
            string rate_float = Console.ReadLine();
            int num2 = Convert.ToInt32(num2_input);
            int pay = CalculatePay(hours_float, rate_float);
            Console.WriteLine(pay);

        }

        // A simple pay calculation program
        static float CalculatePay(float h, float r){

            float pay = h * r;
            return pay;

        }
    }
}

