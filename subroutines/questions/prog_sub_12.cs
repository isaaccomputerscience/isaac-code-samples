using System;

namespace isaac_code_samples
{
    class Program
    {
        static void Main(string[] args)
        {
            display_menu();
        }

        static void display_menu(){
            Console.WriteLine("1 - Weather");
            Console.WriteLine("2 - Time");
            Console.WriteLine("3 - Exit");
        }
    }
}
