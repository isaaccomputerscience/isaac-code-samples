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
    // A class for a node in a linked list
    class Node
    {
        private string data;
        private Node next;

        // Constructor method
        public Node(string itemData)
        {
            data = itemData;
        }

        public string GetData()
        {
            return data;
        }

        public Node GetNext()
        {
            return next;
        }

        public void SetNext(Node newNext)
        {
            next = newNext;
        }

        // Testing
        public void OutputNode()
        {
            string nextData = "null";
            if (next != null)
                nextData = next.data;
            Console.WriteLine($"Data: {data}, next: {nextData}");
        }
    }


    // A stack implemented as a linked list
    class Stack
    {
        private Node top;

        // Check if the stack is empty
        public bool IsEmpty()
        {
            if (top == null)
                return true;
            else
                return false;
        }

        // Push a new item onto the stack
        public void Push(string data)
        {
            Node newNode = new Node(data);

            // Check if the stack is NOT empty
            if (!IsEmpty()) {
                // Point to the next element in the list
                newNode.SetNext(top);
            }
            
            // Set top to point to the new node
            top = newNode;
        }

        // Pop the item from the top of the stack
        public string Pop()
        {
            string poppedItem;

            if (IsEmpty()) {
                Console.WriteLine("\nStack is empty - nothing to pop");
                poppedItem = "";
            }
            else {
                // Get data and change pointer to next item
                poppedItem = top.GetData();
                top = top.GetNext();
            }

            return poppedItem;
        }

        // Peek the item at the top of the stack
        public string Peek()
        {
            string peekedItem;

            if (IsEmpty()) {
                Console.WriteLine("\nStack is empty - nothing to peek");
                peekedItem = "";
            }
            else {
                // Get data from the top of the stack
                peekedItem = top.GetData();
            }

            return peekedItem;
        }

        // Output the state of the stack
        public void OutputStack()
        {
            // Testing
            if (top != null) {
                Console.WriteLine("------ State of the stack ------");
                Node currentNode = top;
                currentNode.OutputNode();
                while (currentNode.GetNext() != null) {
                    currentNode = currentNode.GetNext();
                    currentNode.OutputNode();
                }
                Console.WriteLine();
            }
        }
    }


    class StacksExample
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            Console.WriteLine("### Stack (OOP) ###\n");

            // Initialise the stack
            Stack myStack = new Stack();

            // Insert test data onto the stack
            myStack.Push("Julie");
            myStack.OutputStack();
            
            myStack.Push("Rey");
            myStack.OutputStack();

            // Peek the top item of the stack
            string peekedItem = myStack.Peek();
            Console.WriteLine($"Peeked top of the stack: {peekedItem}");
            myStack.OutputStack();
            
            // Insert more test data onto the stack
            myStack.Push("Habib");
            myStack.OutputStack();
            
            myStack.Push("Sabrina");
            myStack.OutputStack();

            // Pop the top item from the stack
            string poppedItem = myStack.Pop();
            Console.WriteLine($"Popped {poppedItem}");
            myStack.OutputStack();
            
            // Insert more test data onto the stack
            myStack.Push("Mina");
            myStack.OutputStack();
            
            myStack.Push("Eirini");
            myStack.OutputStack();
        }

    }
}