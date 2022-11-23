/*
Raspberry Pi Foundation
Developed to be used alongside Isaac Computer Science, part of the National Centre for Computing Education
Usage licensed under CC BY-SA 4

Note: This file is designed to be copied out and compiled on your machine.
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file.
To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Change the namespace to match your project (if necessary)
4. Compile the program
5. Run the program
*/

using System;

namespace IsaacCodeSamples
{
    class Complexity
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {   
            // Test the SumTo method
            int num = 5;
            int result = SumTo(num);
            Console.WriteLine($"The sum of all integers from 1 to {num} is {result}");
        }


        // Calculates the sum of all integers from 1 to the given number
        public static int SumTo(int givenNumber) 
        {
            int total = 0;
            for (int i = 1; i <= givenNumber; i++) {
                total = total + i;
            }

            return total;
        }

        
    }
}
