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

    class Selection
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            Console.WriteLine("What hour is it?");
            string user_input = Console.ReadLine();
            int hour = Int32.Parse(user_input);

            if (hour < 12)
                Console.WriteLine("Good morning");
            else if (hour < 18)
                Console.WriteLine("Good afternoon");
            else if (hour < 22)
                Console.WriteLine("Good evening"); 
            else
                Console.WriteLine("Good night");
        }
        

    }
}
