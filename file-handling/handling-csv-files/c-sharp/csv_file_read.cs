﻿/*
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
using System.Globalization;
using System.IO;
using CsvHelper;

namespace MyApplication
{
    // The Track class holds information about a track
    class Track
    {
        public string Artist { get; set; }
        public string Song { get; set; }
        public string Duration { get; set; }
    }

    
    class Program
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            ReadCSV();
        }

        
        // Read all the records from a CSV file
        public static void ReadCSV() {
            string filename = "playlist.txt";

            // Read the CSV file using StreamReader and CsvReader
            using (var reader = new StreamReader(filename))
            using (var csvReader = new CsvReader(reader, CultureInfo.CurrentCulture)) {
                // Get all the records and store them as a list of Track objects
                var records = csvReader.GetRecords<Track>();
                
                // Loop through the list of Track objects
                foreach (var track in records) {
                    Console.WriteLine($"{track.Artist } {track.Song} {track.Duration}");
                }
            }
        }

        
    }
}