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
    class NullStrings
    {
        static void Main(string[] args)
        {
            DemonstrateNulls();
        }
        

        // Demonstrates the difference between a null and a space 
        public static void DemonstrateNulls()
        {
            string nullString = "";
            Console.WriteLine(nullString.Length);
            string stringWithSpace = " ";
            Console.WriteLine(stringWithSpace.Length);
            if (nullString == stringWithSpace) {
                Console.WriteLine("We are the same");
            }
            else
            {
                Console.WriteLine("We are different");
            }
        }

    }
}
