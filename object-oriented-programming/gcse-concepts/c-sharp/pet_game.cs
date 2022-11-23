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
    
    class Program
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            Console.WriteLine("Enter a name for your pet ");
            string petName = Console.ReadLine();
            Console.WriteLine($"What type of animal is {petName}? ");
            string petType = Console.ReadLine();
            Console.WriteLine($"What colour is {petName}? ");
            string petColour = Console.ReadLine();
            Pet myPet = new Pet(petName, petType, petColour); // Makes a pet object
            Boolean finished = false;
            while (finished == false)
            {
                ShowGameOptions();
                Console.WriteLine(" What do you want to do? ");
                string choice = Console.ReadLine();
                Console.WriteLine("\n");
                if (choice == "1")
                {
                    myPet.Feed();
                }
                else if (choice == "2")
                {
                    myPet.Play();
                }
                else if (choice == "3")
                {
                    myPet.Sleep();
                }
                else if (choice == "4")
                {
                    myPet.Wake();
                }
                else if (choice == "5")
                {
                    ChangePet(myPet);
                }
                else if (choice == "9")
                {
                    finished = true; // This will cause game to end
                    Console.WriteLine("Thanks for playing the pet game");
                }
                else
                {
                    Console.WriteLine("That is not a menu option");
                }
            }
        }
        
        
        // Display options for playing game
        public static void ShowGameOptions()
        {
            Console.WriteLine("\n");
            Console.WriteLine("  1. Feed your pet");
            Console.WriteLine("  2. Play with your pet");
            Console.WriteLine("  3. Put your pet to bed");
            Console.WriteLine("  4. Wake your pet up");
            Console.WriteLine("  5. Change pet");
            Console.WriteLine("  9. Finish the game");
        }
        
        
        // Allows pet to be changed
        public static void ChangePet(Pet myPet)
        {
            Console.WriteLine("\nDo you want to change the name of your pet(y/n)? ");
            string answer = Console.ReadLine();
            if (answer.ToLower() == "y")
            {
                Console.WriteLine("Enter a new name for your pet ");
                string newName = Console.ReadLine();
                myPet.SetName(newName);
            }
            Console.WriteLine("\nDo you want to change the type of pet you have(y/n)? ");
            answer = Console.ReadLine();
            if (answer.ToLower() == "y")
            {
                string petName = myPet.GetName();
                Console.WriteLine($"What type of animal is {petName}? ");
                string newType = Console.ReadLine();
                myPet.SetType(newType);
            }
            Console.WriteLine("\nDo you want to change the colour of your pet(y/n)? ");
            answer = Console.ReadLine();
            if (answer.ToLower() == "y")
            {
                string petName = myPet.GetName();
                Console.WriteLine($"What colour is {petName}? ");
                string newColour = Console.ReadLine();
                myPet.SetColour(newColour);
            }
            Console.WriteLine("\n");
            myPet.Describe();
        }    
    }
    
}
