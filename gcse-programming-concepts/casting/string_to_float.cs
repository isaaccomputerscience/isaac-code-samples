using System;

namespace isaac_code_samples
{
    class Program
    {

        void Main(string[] args){

            var strToFloat = new Program();
            strToFloat.DoubleIt();

        }

        public void DoubleIt(){
            /// Asks the user for a number and doubles it
            string number = Console.ReadLine();
            float floatNumber = float.Parse(number);
            float answer = floatNumber * 2.0f;
            Console.WriteLine(answer);

        }

    }
}