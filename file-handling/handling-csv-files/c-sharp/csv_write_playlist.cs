/*
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
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using CsvHelper;

namespace IsaacCodeSamples
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
            WriteCSV();
        }


        // Write a list of objects to a CSV file
        public static void WriteCSV() {
            // Create a list of Track objects for writing to the CSV file
            var tracks = new List<Track>() {
                new Track {Artist = "Pharrell Williams", Song = "Happy", Duration = "03:55"},
                new Track {Artist = "Meat Loaf", Song = "Bat out of hell", Duration = "09:50"},
                new Track {Artist = "Adele", Song = "Easy on me", Duration = "03:44"},
                new Track {Artist = "Elton John & Dua Lipa", Song = "Cold heart", Duration = "03:22"}
            };

            // Write to the CSV file using StreamWriter and CsvWriter
            using (var writer = new StreamWriter("playlist.csv"))
            using (var csvWriter = new CsvWriter(writer, CultureInfo.CurrentCulture)) {
                csvWriter.WriteRecords(tracks);
            }
        }

        
    }
}