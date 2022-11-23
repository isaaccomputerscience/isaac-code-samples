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

namespace MyApplication
{
    class Program
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            ReadCsv();
        }


        // Read and display the records from a CSV file
        public static void ReadCsv() {
            using (StreamReader reader = new StreamReader("movies.csv")) {
                string record;
                while ((record = reader.ReadLine()) != null) {
                    string[] movieData = record.Split(",");
                    string title = movieData[0];
                    string rating = movieData[4];
                    Console.WriteLine($"Movie name: {title}, Rating: {rating}");
                }
            } // The stream is now closed
        }

        
    }
}