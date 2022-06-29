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

    class StringValidation
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            Console.WriteLine("Enter a string to check if it is empty:");
            string userInput = Console.ReadLine();
            bool isEmpty = CheckEmptyString(userInput);
            
            if (isEmpty == true) {
                Console.WriteLine("Yes, the string is empty!");
            }
            else {
                Console.WriteLine("No, the string is not empty!");
            }
        }


        // Checks if a string is empty
        public static bool CheckEmptyString(string myString)
        {
            bool empty = false;

            if (String.IsNullOrEmpty(myString)) {
                empty = true;
            }

            return empty;
        }


    }
}
