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

    class ProceduresFunctions
    {

            // The Main method is the entry point for all C# programs
            public static void Main() {
                double side1 = 3;
                double side2 = 4;
                double hypotenuse = GetHypotenuse(side1, side2);
                Console.WriteLine(hypotenuse);
            }

            // Calculates the length of the hypotenuse of a right angled triangle
            public static double GetHypotenuse(double a, double b) {
                double h = Math.Sqrt(CalculateArea(a) + CalculateArea(b));
                return h;
            }


            // Calculates the area of a square with sides of a given length
            public static double CalculateArea(double length) {
                double area = length * length;
                return area;
            }


        }
    }
