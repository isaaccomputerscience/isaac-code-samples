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
