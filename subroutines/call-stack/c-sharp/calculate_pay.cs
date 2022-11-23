/*
Raspberry Pi Foundation
Developed to be used alongside Isaac Computer Science, part of the National Centre for Computing Education
Usage licensed under CC BY-SA 4
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
    class CallStack
    {

        // Simple program to demonstrate the use of call stacks
        public static void Main() {
            Console.WriteLine("Enter hours worked ");
            string hoursInput = Console.ReadLine();
            double hours = Convert.ToDouble(hoursInput);
            Console.WriteLine("Enter hourly rate ");
            string rateInput = Console.ReadLine();
            double rate = Convert.ToDouble(rateInput);
            double pay = CalculatePay(hours, rate);
            Console.WriteLine(pay);
        }


        // A simple pay calculation program
        public static double CalculatePay(double h, double r) {
            double pay = h * r;
            return pay;
        }


    }
}
