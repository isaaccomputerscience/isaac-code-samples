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

namespace IsaacCodeSamples
{
    // Use a class to represent a player as a record
    class PlayerRecord
    {
        public int playerNumber;
        public string firstName;
        public string lastName;
        public DateTime dateOfBirth;
        public string position;
        public bool injured;
    }


    class DataStructures
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Declare an array to store 11 player records
            PlayerRecord[] firstTeam = new PlayerRecord[11];

            // Testing - create 4 players and add them to the array
            PlayerRecord player1 = CreatePlayer(1, "Maria", "Oarps", 
                3, 7, 1994, "Goalkeeper", false);
            firstTeam[0] = player1;
            
            PlayerRecord player2 = CreatePlayer(2, "Lucie", "Gold", 
                18, 10, 1991, "Defender", true);
            firstTeam[1] = player2;

            PlayerRecord player3 = CreatePlayer(3, "Raquel", "Weekly", 
                12, 6, 1992, "Defender", false);
            firstTeam[2] = player3;
            
            PlayerRecord player4 = CreatePlayer(4, "Kiera", "Welsh", 
                4, 8, 1998, "Midfielder", false);
            firstTeam[3]mon = player4;
            
            // Display information about each player
            DisplayPlayers(firstTeam);
        }


        // Create a new player record with the given data
        public static PlayerRecord CreatePlayer(int pId, string fName, 
            string lName, int day, int month, int year, string pos, bool inj)
        {
            // Create a new player record
            PlayerRecord player = new PlayerRecord();

            // Store the details of the player
            player.playerNumber = pId;
            player.firstName = fName;
            player.lastName = lName;
            player.dateOfBirth = new DateTime(year, month, day);
            player.position = pos;
            player.injured = inj;

            // Return the player record
            return player;
        }


        // Display some of the player details from each player record
        public static void DisplayPlayers(PlayerRecord[] playersArray)
        {
            Console.WriteLine("### Array of player records ###");

            // Repeat for each player in the players array of records
            foreach (PlayerRecord player in playersArray) {
                // Check if the player record exists
                if (player != null) {
                    // Display the player's number, name and position
                    Console.WriteLine($"\nNumber: {player.playerNumber}");
                    Console.WriteLine($"Name: {player.firstName} {player.lastName}");
                    Console.WriteLine($"Position: {player.position}");
                }
            }
        }

        
    }
}