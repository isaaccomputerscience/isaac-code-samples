/*
Raspberry Pi Foundation
Developed to be used alongside Isaac Computer Science, part of the National Centre for Computing Education
Usage licensed under CC BY-SA 4

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

    class Selection
    {
        // The Main method is the entry point for all C# programs
        public static void Main() {
            RentCheck();
        }
        

        // Example of nested selection to check user can rent a flat
        public static void RentCheck() {
            Console.WriteLine("Enter your age: ");
            string inputAge = Console.ReadLine();
            int age = Int32.Parse(inputAge);
        
            if (age >= 21) {
                Console.WriteLine("Enter your salary: ");
                string inputSalary = Console.ReadLine();
                int salary = Int32.Parse(inputSalary);
                
                if (salary > 15000) {
                    Console.WriteLine("You can rent the flat");
                }
                else {
                    Console.WriteLine("You don't earn enough to rent the flat");
                }
            }
            else if (age >= 18 && age < 21) {
                Console.WriteLine("Do you have a guarantor (yes/no): ");
                string guarantor = Console.ReadLine();

                if (guarantor == "yes") {
                    Console.WriteLine("We will need to contact your guarantor");
                }
                else {
                    Console.WriteLine("I am sorry but you need a guarantor");
                }
            }
            else {
                Console.WriteLine("I am sorry but you can't rent the flat");
            }
        }

    }
}
