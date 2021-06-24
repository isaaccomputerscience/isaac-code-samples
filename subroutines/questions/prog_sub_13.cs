using System;

namespace isaac_code_samples
{
    class Program
    {
        static void Main(string[] args)
        {
            song();
        }

        static void badger(){
            Console.WriteLine("Badger");
        }

        static void mushroom(){
            Console.WriteLine("Mushroom");
        }

        static void song(){
            for(int i = 1; i <= 12; i++){
                badger();
            }
            mushroom();
            mushroom();
        }
    }
}
