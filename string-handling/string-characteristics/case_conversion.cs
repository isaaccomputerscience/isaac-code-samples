/*
Isaac Computer Science
Usage licensed under the Open Government Licence v3.0

Note: This file is designed to be copied out and compiled on your machine. 
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file. 
To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Compile the program
4. Run the program
*/

using System;

namespace StringHandling
{

    class StringCharacteristics
    {

        // The Main method is the entry point for all C# programs
        public static void Main(string[] args) {
            string letter = "B";
            char lowerCase = ConvertToLower(letter);
            Console.WriteLine(lowerCase);
        }


        // Demonstrates how to use ASCII codes to convert letter case
        public static char ConvertToLower(string letter) {
            int letterCode = (int)letter[0];  // Get code for character extraced from string
            int newLetterCode = letterCode + 32;
            char lowerCase = Convert.ToChar(newLetterCode);  // Converts new code to a character
            return lowerCase;
        }


    }
}

