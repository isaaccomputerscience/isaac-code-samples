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


namespace Subroutines
{
    class DefineAndCall
    {
        // The Main method is the entry point for all C# programs
        public static void Main(string[] args) {
            Console.Write("What is your name? ");
            string name = Console.ReadLine();
            RunQuiz();
            Console.WriteLine("End of the quiz");
        }
        

        // Simulates a quiz
        public static void RunQuiz() {
            Console.WriteLine("What is the capital city of Botswana?");
            string answer = Console.ReadLine();
        }


    }
}
