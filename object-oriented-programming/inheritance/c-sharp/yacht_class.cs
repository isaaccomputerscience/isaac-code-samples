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


namespace IsaacCodeSamples
{


    class Yacht : Boat  // Inherits from Boat
    {

        private int masts;

        // Constructor method
        public Yacht(int givenMasts) : base(string givenName, float givenLength, int givenCapacity, int givenBerths, float givenUnitCost) {
            masts = givenMasts;
        }
        
    }


    class Testing
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
             myBoat = Yacht("Mary Sue", 15.7, 300, 6, 54.5, 2)
        }
        
    }
    
}
