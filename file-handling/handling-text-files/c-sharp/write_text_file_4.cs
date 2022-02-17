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
using System.IO;

namespace MyApplication
{
    class Program
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            string track1 = "Happy, Pharrell Williams, 3:55";
            WriteToFile(track1);
            string track2 = "Reach, S Club 7, 4:02";
            WriteToFile(track2);
        }


        // Method for writing data to a new line in a text file
        public static void WriteToFile(string data) {
            string filename = "playlist.txt";

            using (StreamWriter sw = new StreamWriter(filename, true)) {
                sw.WriteLine(data);
            } // The stream is now closed
        }

        
    }
}