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
using System.Collections.Generic;

namespace IsaacCodeSamples
{
    class Dictionaries
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Intialise a new dictionary of students and results
            Dictionary<string, int> results = new Dictionary<string, int>() {
                {"Detra", 17},	
                {"Nova", 84},
                {"Charlie", 22},
                {"Hwa", 75},
                {"Roxann", 92},
                {"Elsa", 29}
            };

            // Display the score of Charlie
            int score = results["Charlie"];
            Console.WriteLine($"Charlie's score is {score}\n");

            // Insert a new key-value pair for Bob
            results["Bob"] = 78;
            Console.WriteLine($"Bob has been added with score {results["Bob"]}\n");

            // Update the score of Hwa
            results["Hwa"] = 71;
            Console.WriteLine($"Hwa's new score is {results["Hwa"]}\n");

            // Delete the key-value pair for Elsa
            results.Remove("Elsa");
            Console.WriteLine("Elsa has been deleted\n");

            // Repeat for each key-value pair in the dictionary
            foreach (KeyValuePair<string, int> kvp in results) {
                // Output the key-value pair of each item
                string key = kvp.Key;
                int value = kvp.Value;
                Console.WriteLine($"Key: {key}  Value: {value}");
            }
        }


    }
}