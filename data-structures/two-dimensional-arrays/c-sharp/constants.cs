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

    class TwoDimensionalArrays
    {
        const int LEVEL1 = 0;
        const int LEVEL2 = 1;
        const int LEVEL3 = 2;

        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            string[,] spellingWords = new string[3, 3]; // Declare a two dimensional array

            spellingWords[0, 0] = "school";
            spellingWords[0, 1] = "pull";
            spellingWords[0, 2] = "where";
            spellingWords[1, 0] = "path";
            spellingWords[1, 1] = "floor";
            spellingWords[1, 2] = "sugar";
            spellingWords[2, 0] = "accident";
            spellingWords[2, 1] = "answer";
            spellingWords[2, 2] = "eight";

            for (int word = 0; word < 3; word++)
            {
                Console.WriteLine(spellingWords[LEVEL2, word]);
            }


        }
    }
}

