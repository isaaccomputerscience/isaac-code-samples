using System;

namespace isaac_code_samples
{
    class SumToNRecursion
    {
        static void Main(string[] args){
            int n = 6;
            int result = SumToN(n);
            Console.WriteLine(String.Format("The sum of 1 to {0} is: {1}", n.ToString(), result.ToString()));
        }

        public static int SumToN(int n){
            //returns the sum of all natural numbers from 1 to n inclusive
            if (n == 1){
                return 1;
            }else{
                return n + SumToN(n-1);
            }
        }
    }
}
