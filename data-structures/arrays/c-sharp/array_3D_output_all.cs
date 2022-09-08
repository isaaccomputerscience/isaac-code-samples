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
    class DataStructures
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Create a three-dimensional array
            string[,,] myArray = Create3DArray();

            // Output every element in the array
            Console.WriteLine("### Output each element in the 3D array ###");
            OutputEachElement(myArray);
        }

        public static string[,,] Create3DArray()
        {
            // Declare and initialise a three-dimensional array
            string[,,] spellingWords = new string[2, 3, 5] { 
                { 
                    { "me", "do", "her", "it", "him" }, 
                    { "put", "ask", "says", "red", "any" }, 
                    { "they", "where", "friend", "fast", "class" }
                },
                { 
                    { "door", "find", "most", "bath", "eye" }, 
                    { "every", "great", "climb", "prove", "behind" }, 
                    { "clothes", "again", "improve", "should", "parents" } 
                } 
            };

            /*
            // Declare an array of 2 x 3 x 5 elements
            string[,,] spellingWords = new string[2, 3, 5];

            // Assign words into different positions in the array
            spellingWords[0, 0, 4] = "him";
            spellingWords[0, 2, 1] = "where";
            spellingWords[1, 1, 0] = "every";
            spellingWords[1, 2, 4] = "parents";
            */

            // Return the array
            return spellingWords;
        }


        // Output every element in a three-dimensional array
        public static void OutputEachElement(string[,,] givenArray)
        {
            // Repeat for each year
            for (int year = 0; year < givenArray.GetLength(0); year++)
            {
                // Repeat for each level
                for (int level = 0; level < givenArray.GetLength(1); level++)
                {
                    // Output each word for the current year and level
                    for (int word = 0; word < givenArray.GetLength(2); word++)
                    {
                        Console.WriteLine(givenArray[year, level, word]);
                    }
                }
            }
        }

        
    }
}
