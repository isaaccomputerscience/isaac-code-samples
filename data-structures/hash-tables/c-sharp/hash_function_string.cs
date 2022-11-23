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

    class HashTables
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Generate a hash value from an integer hash key
            string key = "A5RD";
            int slots = 97;
            int value = HashString(key, slots);
            Console.WriteLine($"Hash value for {key} is {value}");
        }

        // Produce a hash value from a string
        public static int HashString(string hashKey, int numberOfSlots)
        {
            // Initialise total
            int total = 0;

            // Repeat for every character in the hash key
            for (int i = 0; i < hashKey.Length; i++) {
                // Add the character's ASCII value to the total
                int asciiCode = (int)hashKey[i];
                total = total + asciiCode;
            }

            // Generate the hash value using the modulo operator
            int hashValue = total % numberOfSlots;

            // Return the hash value
            return hashValue;
        }


    }
}