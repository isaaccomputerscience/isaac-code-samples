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
            SelectHighEarners();
        }


        // Select and display high earning movies over $200 million
        public static void SelectHighEarners() {
            int highEarners = 0;
            using (StreamReader reader = new StreamReader("movies.csv")) {
                string record;
                while ((record = reader.ReadLine()) != null) {
                    string[] movieData = record.Split(",");
                    decimal revenue =  decimal.Parse(movieData[5]);

                    // Check if the movie revenue was over $200 million
                    if (revenue > 200) {
                        string title = movieData[0];
                        Console.WriteLine($"Movie name: {title}, Revenue: ${revenue} million");
                        highEarners = highEarners + 1;
                    }
                }
            } // The stream is now closed
            Console.WriteLine($"There were {highEarners} high earning movies.");
        }

        
    }
}