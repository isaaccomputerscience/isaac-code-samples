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
            Console.WriteLine("Enter the title of the film: ");
            string title = Console.ReadLine();
            Console.WriteLine("Enter the year the film was made: ");
            string year = Console.ReadLine();
            Console.WriteLine("Enter the length of the film in minutes: ");
            string duration = Console.ReadLine();
            Console.WriteLine("Enter the name of the film director: ");
            string director = Console.ReadLine();
            Console.WriteLine("Enter the average film rating: ");
            string rating = Console.ReadLine();
            Console.WriteLine("Enter the takings in US$ millions: ");
            string takings = Console.ReadLine();
            AppendMovieOptimised(title, year, duration, director, rating, takings);
        }


        // Optimised version to append a new record to the CSV file
        public static void AppendMovieOptimised(string title, string year, string duration, string director, string rating, string takings) {
            string newMovie = title + "," + year + "," + duration + "," + director + "," + rating + "," + takings;
            using (StreamWriter writer = new StreamWriter("movies.csv", true)) {
                writer.WriteLine(newMovie);
            }
        }

        
    }
}