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
using System.IO;

namespace IsaacCodeSamples
{
    class Program
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            AppendToFile();
        }


        // Example of appending to a text file
        public static void AppendToFile() {
            using (StreamWriter writer = new StreamWriter("twinkle.txt", true)) {
                writer.WriteLine("");
                writer.WriteLine("When the blazing sun is gone");
                writer.WriteLine("When he nothing shines upon,");
                writer.WriteLine("Then you show your little light,");
                writer.WriteLine("Twinkle, twinkle, all the night.");
            } // The stream is now closed
        }

        
    }
}