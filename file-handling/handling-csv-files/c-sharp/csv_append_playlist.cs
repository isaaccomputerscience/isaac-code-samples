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
using CsvHelper.Configuration;

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
            AppendCSV();
        }


        // Append a record to a CSV file
        public static void AppendCSV() {
            // Configure CsvHelper so it does not write the header record
            var csvConfig = new CsvConfiguration(CultureInfo.CurrentCulture) {
                HasHeaderRecord = false
            };

            // Create a list of Track objects for writing to the CSV file
            var tracks = new List<Track>() {
                new Track {Artist = "Carolina Gaitán", Song = "We don't talk about Bruno", Duration = "03:36"}
            };

            // Append to the CSV file using File, StreamWriter and CsvWriter
            using (var stream = File.Open("playlist.csv", FileMode.Append))
            using (var writer = new StreamWriter(stream))
            using (var csvWriter = new CsvWriter(writer, csvConfig)) {
                csvWriter.WriteRecords(tracks);
            }
        }

        
    }
}