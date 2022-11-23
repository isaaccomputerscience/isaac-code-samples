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
    class Pet {
        private string name;
        private string type;
        private string colour;
        private string mood;
        private Boolean sleeping;
        
        
        // Constructor
        public Pet(string givenName, string givenType, string givenColour) {
            name = givenName;
            type = givenType;
            colour = givenColour;
            string[] allMoods = { "playful", "hungry", "sleepy" };
            Random rnd = new Random();
            int index = rnd.Next(allMoods.Length);
            mood = allMoods[index];
            sleeping = false;
        }
        
        
        public string GetName() {
            return name;
        }
        
        
        public new string GetType() {
            return type;
        }
        
        
        public string GetColour() {
            return colour;
        }
        
        
        public string GetMood() {
            return mood;
        }
        
        
        public Boolean IsSleeping() {
            return sleeping;
        }
        
        
        public void Describe() {
            Console.WriteLine($"I am a {mood}, {colour} {type} called {name}");
        }
        
        
        public void SetName(string newName) {
            name = newName;
        }
        
        
        public void SetType(string newType) {
            type = newType;
        }
        
        
        public void SetColour(string newColour) {
            colour = newColour;
        }
        
        
        public void Play() {
            if (sleeping == true) {
                Console.WriteLine("Zzzzzzz. I am sleeping");
            } else if (mood == "hungry") {
                Console.WriteLine("I am too hungry to play");
            } else if (mood == "tired") {
                Console.WriteLine("I am too tired to play");
            } else {
                Console.WriteLine("This is fun, I love playing");            
                string[] allMoods = { "playful", "hungry", "sleepy" };
                Random rnd = new Random();
                int index = rnd.Next(allMoods.Length);
                mood = allMoods[index];
            }
        }
        
        
        public void Feed() {
            if (sleeping == true) {
                Console.WriteLine("Zzzzzzz. I am sleeping");
            }
            if (mood == "tired") {
                Console.WriteLine("I am too sleepy to eat anything now");
            } else if (mood == "playful") {
                Console.WriteLine("I am not hungry - I want to play");
            } else {
                Console.WriteLine("Yum - yum - that tastes great");
                mood = "playful";
            }
        }
        
        
        public void Sleep() {
            if (mood == "playful") {
                Console.WriteLine("I am too playful to sleep");
            } else if (mood == "hungry") {
                Console.WriteLine("I need something to eat before I can go to sleep");
            } else {
                Console.WriteLine("Zzzzzzzz");
                sleeping = true;
            }
        }
        
        
        public void Wake() {
            if (sleeping == false) {
                Console.WriteLine("I wasn't even asleep!");
            } else {
                Console.WriteLine("I am awake and ready to play!");
                sleeping = false;
                mood = "playful";
            }
        }
        
    }
}
