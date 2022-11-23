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

    class Iteration
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            int sum = 0;
            int numValues = 0;

            Console.WriteLine("Enter a mark or -1 to end ");
            string userInput = Console.ReadLine();
            int mark = Int32.Parse(userInput);

            while (mark != -1) {
                sum = sum + mark;
                numValues = numValues + 1;

                Console.WriteLine("Enter a mark or -1 to end ");
                userInput = Console.ReadLine();
                mark = Int32.Parse(userInput);
            }

            double average = (double)sum / (double)numValues;
            Console.WriteLine($"The average mark was {average}");
        }
        

    }
}
