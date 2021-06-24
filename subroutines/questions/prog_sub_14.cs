using System;

namespace isaac_code_samples
{
    class Program
    {
        static void Main(string[] args){
            find_y(5, 2, 3);
        }

        static int multiply(int a, int b){
            return a * b;
        }

        static int add(int a, int b){
            return a + b;
        }

        static void find_y(int x, int m, int c){
            Console.Write($"x={x} y=");
            Console.WriteLine(add(multiply(m, x), c));
        }
    }
}
