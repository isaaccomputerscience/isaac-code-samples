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
using System.Globalization;
using System.IO;
using CsvHelper;

namespace MyApplication
{
    // The Movie class holds information about a movie
    class Movie
    {
        public string Title { get; set; }
        public string Year { get; set; }
        public string Duration { get; set; }
        public string Genre { get; set; }
        public string Director { get; set; }
        public string Rating { get; set; }
        public string Revenue { get; set; }
    }

    
    class Program
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {  
            Console.WriteLine("Enter a genre of movie to find:");
            string genreChosen = Console.ReadLine();

            int total = MoviesByGenre(genreChosen);
            Console.WriteLine($"There were {total} movies containing the genre {genreChosen}");
        }

        // Read all the records from a CSV file
        public static int MoviesByGenre(string genre) {
            // Initialise the filename and count
            string filename = "movies_extra.csv";
            int count = 0;

            // Capitalise the first letter of each word in genre
            TextInfo textInfo = CultureInfo.CurrentCulture.TextInfo;
            genre = textInfo.ToTitleCase(genre);

            // Read the CSV file using StreamReader and CsvReader
            using (var reader = new StreamReader(filename))
            using (var csvReader = new CsvReader(reader, CultureInfo.CurrentCulture)) {
                // Get all the records and store them as a list of Movie objects
                var records = csvReader.GetRecords<Movie>();
                
                // Loop through the list of Movie objects
                foreach (var movie in records) {
                    // Check if the genre is in the genre field
                    if (movie.Genre.Contains(genre)) {
                        Console.WriteLine($"Data: {movie.Title}, {movie.Year}, {movie.Duration}, {movie.Genre}, {movie.Director}, {movie.Rating}, {movie.Revenue}");
                        count = count + 1;
                    }
                }
            }
            return count;
        }

        
    }
}