/*
Raspberry Pi Foundation
Developed to be used alongside Isaac Computer Science, part of the National Centre for Computing Education
Usage licensed under CC BY-SA 4
Note: This file is designed to be copied out and compiled on your machine.
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file.
To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Change the namespace to match your project (if neccesary)
4. Compile the program
5. Run the program
*/

using System;

namespace IsaacCodeSamples
{
    class LocalGlobal
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            int amount = 100;
            Console.WriteLine(amount);
            Triple(amount);
            Quadruple(amount);
            Console.WriteLine(amount);
        }


        // Triple number and display result
        public static void Triple(int n) { 
            int amount = n * 3;
            Console.WriteLine(amount);
        }


        // Quadruple number and display result
        public static void Quadruple(int n) {
            int amount = n * 4;
            Console.WriteLine(amount);
        }


    }
}
