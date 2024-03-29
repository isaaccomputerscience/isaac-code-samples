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
using System.IO;

namespace IsaacCodeSamples
{
    class PlayingCard
    {
        private string suit;
        private string rank;
        private int value;

        // Constructor method
        public PlayingCard(string givenSuit, string givenRank, int givenValue) {
            suit = givenSuit;
            rank = givenRank;
            value = givenValue;
        }

        public string GetSuit() {
            return suit;
        }

        public string GetRank() {
            return rank;
        }

        public int GetValue() {
            return value;
        }

    }

    
    class Testing
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            // Instantiate a new card object
            PlayingCard myCard = new PlayingCard("clubs", "2", 2);
            Console.WriteLine($"Suit is: {myCard.GetSuit()}");
            Console.WriteLine($"Rank is: {myCard.GetRank()}");
            Console.WriteLine($"Value is: {myCard.GetValue()}");
        }
        
    }

}
