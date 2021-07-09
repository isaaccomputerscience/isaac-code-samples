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
    class Cases
    {
        static void Main(string[] args){
            ConvertToLower();
        }

        //Demonstrates conversion to lower case
        static void ConvertToLower(){
            Console.Write("Enter an uppercase letter ");
            string letter = Console.ReadLine();
            int letterCode = (int)letter[0];  // Converts first letter to ASCII code
            int newLetterCode = letterCode + 32;
            char lowerCase = Convert.ToChar(newLetterCode);  // Converts new code to a letter
           Console.WriteLine(lowerCase);
        }

    }
}
