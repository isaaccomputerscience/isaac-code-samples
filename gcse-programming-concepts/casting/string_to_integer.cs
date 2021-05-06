using System;

namespace string_to_integer
{
    class StrToInt
    {

        static void Main(string[] args){

            var strToFloat = new StrToInt();
            strToFloat.DoubleIt();

        }

        public void DoubleIt(){

            string number = Console.ReadLine();
            int intNumber = int.Parse(number);
            float answer = intNumber * 2;
            Console.WriteLine(answer);

        }

    }
}