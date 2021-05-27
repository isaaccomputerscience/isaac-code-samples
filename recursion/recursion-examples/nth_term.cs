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

namespace isaac_code_samples
{
    class NthTermRecursive
    {
        void Main(string[] args){
            int n = 6;
            int increment = 3;
            int result = NthTerm(n, increment);
            Console.WriteLine(String.Format("Term {0} is {1}", n.ToString(), result.ToString()));
        }

        public static int NthTerm(int n, int increment){
            //returns the nth term of a numerical sequence
            if (n == 1){
                return 1;
            }else{
                return increment + NthTerm(n-1, increment);
            }
        }
    }
}