/*
Isaac Computer Science
Usage licensed under the Open Government Licence v3.0

Note: This file is designed to be copied out and compiled on your machine.
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file.
To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Change the namespace to match your project (if necessary)
4. Compile the program
5. Run the program
*/

using System;

namespace IsaacCodeSamples
{

    class StringValidation
    {

        // The Main method is the entry point for all C# programs
        public static void Main() {
            Test();
        }

        // Test data
        public static void Test() {
            // normal data
            string password = "elephant1234";
            bool result = CheckPassword(password);
            Console.WriteLine($"{password} is valid: {result}");

            // boundary data
            password = "elephant";  // 8 characters exactly
            result = CheckPassword(password);
            Console.WriteLine($"{password} is valid: {result}");

            // password is too short
            password = "1234";
            result = CheckPassword(password);
            Console.WriteLine($"{password} is valid: {result}");
        }


        // Checks password length
        public static bool CheckPassword(string password) {
            bool isValid = true;
            if (password.Length < 8) {
                isValid = false;
            }
            return isValid;
        }
        

    }
}
