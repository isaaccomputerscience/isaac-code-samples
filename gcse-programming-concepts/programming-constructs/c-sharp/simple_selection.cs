using System;

namespace IsaacCodeSamples
{

    class ProgrammingConstructs  // Simple selection
    {
       
        public static void Main() {
            Console.WriteLine("Which animal has a long bendy trunk?");
            string animal = Console.ReadLine();
            if (animal == "Elephant") {
                Console.WriteLine("You are correct");
            } else {
                Console.WriteLine("You are incorrect");
            }
        }
        
        
    }
}
