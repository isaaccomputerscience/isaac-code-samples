using System;

namespace isaac_code_samples
{
    class SimpleSelection
    {
        void Main(string[] args){
            Console.WriteLine("Which animal has a long bendy trunk?");
            string animal = Console.ReadLine();
            if (animal == "Elephant"){
                Console.WriteLine("You are correct");
            }else{
                Console.WriteLine("You are incorrect");
            }

        }
    }
}