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
            AppendMovie();
        }


        // Append a new record to the CSV file
        public static void AppendMovie() {
            string newMovie = "CODA,2021,111,Sian Heder,8.1,1.5";
            using (StreamWriter writer = new StreamWriter("movies.csv", true)) {
                writer.WriteLine(newMovie);
            }
        }

        
    }
}