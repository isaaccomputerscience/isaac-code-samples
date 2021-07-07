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
    class StringLength
    {
        static void Main(string[] args)
        {
            ShowPasswordLength();
         }

        // Prompts for a password and displays length
        public static void ShowPasswordLength()
        {
            Console.Write("Please enter a password ");
            string password = Console.ReadLine();
            Console.WriteLine(password.Length);
        }
    }
}
