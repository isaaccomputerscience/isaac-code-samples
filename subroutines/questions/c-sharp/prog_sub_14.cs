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
    
    class SubQuestion14
    {
        
        static void Main() {
            find_y(5, 2, 3);
        }
        

        static int multiply(int a, int b) {
            return a * b;
        }
        

        static int add(int a, int b) {
            return a + b;
        }
        

        static void find_y(int x, int m, int c) {
            Console.Write($"x={x} y=");
            Console.WriteLine(add(multiply(m, x), c));
        }
        
        
    }
}
