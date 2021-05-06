using System;

namespace string_to_integer
{
    class StrToInt
    {

        void Main(string[] args){

            var strToFloat = new StrToInt();
            strToFloat.DoubleIt();

        }

        public void DoubleIt(){
            /// Asks the user for a number and doubles it
            string number = Console.ReadLine();
            int intNumber = int.Parse(number);
            float answer = intNumber * 2;
            Console.WriteLine(answer);

        }

    }
}