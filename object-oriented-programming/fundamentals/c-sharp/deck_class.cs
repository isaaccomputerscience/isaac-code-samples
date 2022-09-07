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
using card_class;

namespace IsaacCodeSamples
{
    class Deck
    {
        
        private string[] cards = new string[52]; // Declare an array of 52 elements
        private string[] suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        private string[] ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        private string[] values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        // Constructor method
        public static void Deck() {
            for (int i = 0; i = 4; i++) {
                for (int j = 0; j = 13; j++) {
                new card = Card(suits[i], ranks[j], values[j])
                this.cards.append(card);
                }
             }
             
        }

    }
    
    
    class Testing
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            myDeck = new Deck();  // Instantiate a new deck object
        }
    }
    
    
}
