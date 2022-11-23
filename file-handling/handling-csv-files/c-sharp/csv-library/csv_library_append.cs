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
using System.Globalization;
using System.IO;
using CsvHelper;
using CsvHelper.Configuration;

namespace IsaacCodeSamples
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
            // Create a list of Movie objects for appending to the CSV file
            var movies = new List<Movie>() {
                new Movie {Title="The Batman", Year="2022", Duration="176", Genre="Action,Crime,Drama", Director="Matt Reeves", Rating="8.3", Revenue="350"},
                new Movie {Title="Joker", Year="2019", Duration="122", Genre="Crime,Drama,Thriller", Director="Todd Phillips", Rating="8.4", Revenue="335.5"}
            };            
            AppendRecord(movies);
        }

        // Append a record to a CSV file
        public static void AppendRecord(List<Movie> newRecords) {
            // Initialise the filename
            string filename = "movies_extra.csv";

            // Configure CsvHelper so it does not write the header record again
            var csvConfig = new CsvConfiguration(CultureInfo.CurrentCulture) {
                HasHeaderRecord = false
            };

            // Append to the CSV file using File, StreamWriter and CsvWriter
            using (var stream = File.Open(filename, FileMode.Append))
            using (var writer = new StreamWriter(stream))
            using (var csvWriter = new CsvWriter(writer, csvConfig)) {
                csvWriter.WriteRecords(newRecords);
            }
        }

        
    }
}