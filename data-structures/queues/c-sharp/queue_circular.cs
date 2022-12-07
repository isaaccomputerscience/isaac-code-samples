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
    class Queues
    {
        public const int MaxSize = 4;

        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            Console.WriteLine("### Circular queue ###");

            // Initialise the queue and pointers
            string[] queue = new string[MaxSize];
            int front = -1;
            int rear = -1;

            // Tuples are used to store multiple return values
            Tuple<int, int> enqueuedValues; // front, rear
            Tuple<string, int, int> dequeuedValues; // item, front, rear

            // Insert test data into the queue
            enqueuedValues = Enqueue(queue, front, rear, "Julie");
            front = enqueuedValues.Item1;
            rear = enqueuedValues.Item2;
            OutputQueue(queue, front, rear);
            
            enqueuedValues = Enqueue(queue, front, rear, "Rey");
            front = enqueuedValues.Item1;
            rear = enqueuedValues.Item2;
            OutputQueue(queue, front, rear);
            
            enqueuedValues = Enqueue(queue, front, rear, "Habib");
            front = enqueuedValues.Item1;
            rear = enqueuedValues.Item2;
            OutputQueue(queue, front, rear);
            
            enqueuedValues = Enqueue(queue, front, rear, "Sabrina");
            front = enqueuedValues.Item1;
            rear = enqueuedValues.Item2;
            OutputQueue(queue, front, rear);

            // Trying to enqueue - should say queue is full
            enqueuedValues = Enqueue(queue, front, rear, "Mina");
            front = enqueuedValues.Item1;
            rear = enqueuedValues.Item2;
            OutputQueue(queue, front, rear);

            // Dequeue some of the items
            dequeuedValues = Dequeue(queue, front, rear);
            front = dequeuedValues.Item2;
            rear = dequeuedValues.Item3;
            Console.WriteLine($"\nDequeued {dequeuedValues.Item1}");
            OutputQueue(queue, front, rear);

            dequeuedValues = Dequeue(queue, front, rear);
            front = dequeuedValues.Item2;
            rear = dequeuedValues.Item3;
            Console.WriteLine($"\nDequeued {dequeuedValues.Item1}");
            OutputQueue(queue, front, rear);

            // Insert data into the empty slots in the queue
            enqueuedValues = Enqueue(queue, front, rear, "Eirini");
            front = enqueuedValues.Item1;
            rear = enqueuedValues.Item2;
            OutputQueue(queue, front, rear);

            enqueuedValues = Enqueue(queue, front, rear, "Diane");
            front = enqueuedValues.Item1;
            rear = enqueuedValues.Item2;
            OutputQueue(queue, front, rear);

            // Trying to enqueue - should say queue is full
            enqueuedValues = Enqueue(queue, front, rear, "Fergus");
            front = enqueuedValues.Item1;
            rear = enqueuedValues.Item2;
            OutputQueue(queue, front, rear);
        }

        // Check if the queue is empty
        public static bool IsEmpty(int front)
        {
            if (front == -1)
                return true;
            else
                return false;
        }

        // Check if the queue is full
        public static bool IsFull(int front, int rear)
        {
            if ((rear + 1) % MaxSize == front)
                return true;
            else
                return false; 
        }

        // Enqueue an item
        public static Tuple<int, int> Enqueue(string[] queue, int front, int rear, string data)
        {
            if (IsFull(front, rear) == true)
                Console.WriteLine($"\nQueue is full - {data} not added");
            else {
                rear = (rear + 1) % MaxSize;
                queue[rear] = data;
                if (front == -1) // First item to be queued
                    front = 0;
            }
            return Tuple.Create(front, rear);
        }

        // Dequeue an item
        public static Tuple<string, int, int> Dequeue(string[] queue, int front, int rear)
        {
            string dequeuedItem;

            if (IsEmpty(front) == true) {
                Console.WriteLine("\nQueue is empty - nothing to dequeue");
                dequeuedItem = "";
            }
            else {
                dequeuedItem = queue[front];
                queue[front] = ""; // Testing
                // Check if the queue is empty
                if (front == rear) {
                    front = -1;
                    rear = -1;
                }    
                else
                    front = (front + 1) % MaxSize;
            }

            return Tuple.Create(dequeuedItem, front, rear);
        }

        // Output the state of the queue
        public static void OutputQueue(string[] queue, int front, int rear)
        {
            // Testing
            Console.Write("\nQueue: ");
            Console.WriteLine("[{0}]", string.Join(", ", queue));
            Console.WriteLine($"Front: {front}");
            Console.WriteLine($"Rear: {rear}");
        }

    }
}