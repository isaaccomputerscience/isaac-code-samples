/*
Isaac Computer Science
Usage licensed under the Open Government Licence v3.0

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

    class Variables
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            Console.WriteLine("Enter a week of the year: ");
            string userInput = Console.ReadLine();
            int week = Int32.Parse(userInput);

            if (week > 0 && week <= 52) {
                Console.WriteLine($"You have chosen week {week}");
            }
            else {
                Console.WriteLine("A week must be between 1-52");
            }
        }
        

    }
}