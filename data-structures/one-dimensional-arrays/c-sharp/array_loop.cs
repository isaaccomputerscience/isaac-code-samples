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

    class OneDimensionalArrays
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            string[] emotions = new string[6]; // Declare an array of 6 elements

            emotions[0] = "amazed";  // Assign a value into a position of the array
            emotions[1] = "delighted";
            emotions[2] = "ecstatic";
            emotions[3] = "enthusiastic";
            emotions[4] = "lively";

            Console.WriteLine(emotions[2]);  // Displays the third element of the array

            emotions[5] = "happy";  // Adds a new item to the array

            emotions[1] = "";  // Deletes the item in the second element of the array

            for (int i = 0; i < 6; i++)
            {
                Console.WriteLine(emotions[i]);
            }

        }
    }

}
