/*
Raspberry Pi Foundation
Developed to be used alongside Isaac Computer Science, part of the National Centre for Computing Education
Usage licensed under CC BY-SA 4

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

namespace IsaacCodeSamples
{
    
    class ProgrammingConstructs  // Condition controlled loop
    {
        
        // A guessing game, user guesses names until they get the right answer
        public static void Main() {            
            Console.WriteLine("Please enter your name ");
            string name = Console.ReadLine();
            while (name != "Fergus") {
                Console.WriteLine("Please enter your name");
                name = Console.ReadLine();
            }
            Console.WriteLine("You guessed my name!");
        }
        
        
    }
}
