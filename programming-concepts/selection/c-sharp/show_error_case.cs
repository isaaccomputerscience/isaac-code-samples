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
            ShowError();
        }


        // Example of a switch/case statement to match the error code
        public static void ShowError() {
            Console.WriteLine("Enter the error code: ");
            string errorCode = Console.ReadLine();

            switch (errorCode) {
                case "400":
                    Console.WriteLine("Bad request");
                    break;
                case "401":
                    Console.WriteLine("Unauthorised request");
                    break;
                case "403":
                    Console.WriteLine("Forbidden request");
                    break;
                case "404":
                    Console.WriteLine("Page not found");
                    break;
                case "408":
                    Console.WriteLine("Timeout error");
                    break;
                default:
                    Console.WriteLine("Unknown error");
                    break;
            }
        }
        

    }
}
