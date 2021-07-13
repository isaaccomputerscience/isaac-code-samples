using System;

namespace isaac_code_samples
{
    class WhileLoop
    {
        void Main(string[] args){
            /// A name guessing game, user inputs guesses until they get the right answer
            Console.WriteLine("Please enter your name");
            string name = Console.ReadLine();
            while (name != "Fergus"){
                Console.WriteLine("Please enter your name");
                name = Console.ReadLine();
            }
            Console.WriteLine("You guessed my name!");

        }
    }
}