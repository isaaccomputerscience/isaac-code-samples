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
    class Player
    {

        private string name;
        private int score;

        // Constructor method
        public Player(string givenName) {
            name = givenName;
            score = 0;
        }
        
        public getName() {
            return name;
        }
        
        public getScore() {
            return score;
        }
        
        public setScore(int newScore) {
            score = newScore;
        }
        
    }
    
    
    class Testing
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Instantiate a new player object
            Player player1 = new Player("Leona");
            Console.WriteLine($"The player's name is: {player1.GetName()}");
            Console.WriteLine($"The player's score is: {player1.GetScore()}");
            player1.setScore(20);
            Console.WriteLine($"The player's score is now: {player1.GetScore()}");
        }
    }
    
    
}
