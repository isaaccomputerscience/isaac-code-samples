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

    class CompressionTechniques
    {

        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Test data - normal data
            string text = "aaaabbbccdddeee";
            Console.WriteLine(text);
            Console.WriteLine(RLE(text));

            text = "Bobby";
            Console.WriteLine(text);
            Console.WriteLine(RLE(text));

            // Test data - boundary data
            text = "a";
            Console.WriteLine(text);
            Console.WriteLine(RLE(text));

            text = "aaaaaa";
            Console.WriteLine(text);
            Console.WriteLine(RLE(text));

            text = "aaaae";
            Console.WriteLine(text);
            Console.WriteLine(RLE(text));

            text = "aeeeee";
            Console.WriteLine(text);
            Console.WriteLine(RLE(text));
        }

        // A simple version of Run Length Encoding for text strings
        public static string RLE(string textString)
        {
            char currentToken = textString[0];
            string compressed = currentToken.ToString();
            int counter = 1;

            for (int i = 1; i < textString.Length; i++) {
                char nextToken = textString[i];
                if (nextToken != currentToken) {
                    compressed = compressed + counter.ToString() + nextToken;
                    counter = 1;
                }
                else {
                    counter = counter + 1;
                }
                currentToken = nextToken;
            }
            compressed = compressed + counter.ToString();
            return compressed;
        }
    }

}