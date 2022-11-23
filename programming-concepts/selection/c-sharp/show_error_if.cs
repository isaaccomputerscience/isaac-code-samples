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


        // Example of an if/else if statement to match the error code
        public static void ShowError() {
            Console.WriteLine("Enter the error code: ");
            string errorCode = Console.ReadLine();

            if (errorCode == "400") {
                Console.WriteLine("Bad request");
            }
            else if (errorCode == "401") {
                Console.WriteLine("Unauthorised request");
            }
            else if (errorCode == "403") {
                Console.WriteLine("Forbidden request");
            }
            else if (errorCode == "404") {
                Console.WriteLine("Page not found");
            }
            else if (errorCode == "408") {
                Console.WriteLine("Timeout error");
            }
            else {
                Console.WriteLine("Unknown error");
            }
        }
        

    }
}
