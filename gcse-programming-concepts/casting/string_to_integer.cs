/*
Note: This file is designed to be copied out and compiled on your machine. 
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file. 

To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Compile the program
4. Run the program
*/

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
            Console.WriteLine("Enter a number");
            string number = Console.ReadLine();
            int intNumber = int.Parse(number);
            int answer = intNumber * 2;
            Console.WriteLine(answer);

        }

    }
}