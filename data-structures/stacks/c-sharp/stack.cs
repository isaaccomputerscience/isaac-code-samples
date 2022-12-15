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
    class Stacks
    {
        public const int MaxSize = 4;

        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            Console.WriteLine("### Stack ###");

            // Initialise the stack and pointers
            string[] stack = new string[MaxSize];
            int top = -1;

            // Insert test data into the stack
            top = Push(stack, top, "Julie");
            OutputStack(stack, top);
            
            top = Push(stack, top, "Rey");
            OutputStack(stack, top);
            
            top = Push(stack, top, "Habib");
            OutputStack(stack, top);
            
            top = Push(stack, top, "Sabrina");
            OutputStack(stack, top);

            // Trying to push - should say stack is full
            top = Push(stack, top, "Mina");
            OutputStack(stack, top);

            // Peek the top item of the stack
            string peekedItem = Peek(stack, top);
            Console.Write($"\nPeeked top of the stack {peekedItem}");
            OutputStack(stack, top);

            // Pop all of the items
            foreach (string item in stack) {
                // Tuple is used to store multiple return values
                Tuple<string, int> poppedValues; // item, top

                poppedValues = Pop(stack, top);
                top = poppedValues.Item2;
                Console.Write($"\nPopped {poppedValues.Item1}");
                OutputStack(stack, top);
            }

            // Try to pop - should say stack is empty
            Tuple<string, int> finalPoppedValues; // item, top
            finalPoppedValues = Pop(stack, top);
            top = finalPoppedValues.Item2;
        }

        // Check if the stack is empty
        public static bool IsEmpty(int top)
        {
            if (top == -1)
                return true;
            else
                return false;
        }

        // Check if the stack is full
        public static bool IsFull(int top)
        {
            if (top == MaxSize - 1)
                return true;
            else
                return false; 
        }

        // Push data onto the top of the stack
        public static int Push(string[] stack, int top, string data)
        {
            if (IsFull(top) == true)
                Console.WriteLine($"\nStack is full - {data} not added");
            else {
                top = top + 1;
                stack[top] = data;
            }
            return top;
        }

        // Return a copy of the item from the top of stack without removing it
        public static string Peek(string[] stack, int top)
        {
            string peekedItem;

            if (IsEmpty(top) == true) {
                Console.WriteLine("\nStack is empty - nothing to peek");
                peekedItem = "";
            }
            else {
                peekedItem = stack[top];
            }

            return peekedItem;
        }

        // Return the item from the top of stack and remove it from the stack
        public static Tuple<string, int> Pop(string[] stack, int top)
        {
            string poppedItem;

            if (IsEmpty(top) == true) {
                Console.WriteLine("\nStack is empty - nothing to pop");
                poppedItem = "";
            }
            else {
                poppedItem = stack[top];
                stack[top] = ""; // Testing
                top = top - 1;
            }

            return Tuple.Create(poppedItem, top);
        }

        // Output the state of the stack
        public static void OutputStack(string[] stack, int top)
        {
            // Testing
            Console.WriteLine("\n------ State of the stack (first item is the top) ------");

            for (int i = MaxSize - 1; i >= 0; i--) {
                string item = stack[i];
                if (string.IsNullOrEmpty(item)) {
                    item = "null";
                }
                Console.WriteLine($"{item}");
            }

            Console.WriteLine($"Top pointer: {top}");
        }

    }
}