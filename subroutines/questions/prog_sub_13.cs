  
/*
Note: This file is designed to be copied out and compiled on your machine. 
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file. 
To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Compile the program
4. Run the program
*/

using System;

namespace isaac_code_samples
{
    class Program
    {
        static void Main(string[] args)
        {
            song();
        }

        static void badger(){
            Console.WriteLine("Badger");
        }

        static void mushroom(){
            Console.WriteLine("Mushroom");
        }

        static void song(){
            for(int i = 1; i <= 12; i++){
                badger();
            }
            mushroom();
            mushroom();
        }
    }
}
