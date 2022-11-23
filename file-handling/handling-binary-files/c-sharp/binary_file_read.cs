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
using System.Collections.Generic;
using System.IO;

namespace MyApplication
{
    class Program
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            ReadBinaryFile();
        }


        // Read data from a binary file
        public static void ReadBinaryFile() {
            // Declare an empty dictionary for adding the data to
            Dictionary<string, double> player_stats = new Dictionary<string, double>();

            string filename = "treasure.game";

            // Read from a file using File and BinaryReader
            using (var stream = File.Open(filename, FileMode.Open))
            using (var binaryReader = new BinaryReader(stream)) { 
                // Read each key and value pair from the file
                while (binaryReader.BaseStream.Position != binaryReader.BaseStream.Length) {
                    var key = binaryReader.ReadString();
                    var value = binaryReader.ReadDouble();

                    player_stats.Add(key, value);
                }
            }

            // Testing the dictionary has been populated from the binary file
            Console.WriteLine("Output dictionary read from binary file");
            foreach(var kvp in player_stats)
                Console.WriteLine("Key: {0}, Value: {1}", kvp.Key, kvp.Value);
        }

        
    }
}