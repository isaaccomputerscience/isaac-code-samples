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
    class PrintBackwardsRecursive
    {
        static void Main(string[] args){
            PrintBackwards("I am a computer scientist");
        }

        // Prints a given string backwards
        public static void PrintBackwards(string phrase){
            if (phrase.Length == 1){
                Console.Write(phrase);
            } else {
                string new_phrase = phrase.Substring(1, phrase.Length - 1);
                PrintBackwards(new_phrase);
                Console.Write(phrase.Substring(0, 1));
            }
        }
    }
}