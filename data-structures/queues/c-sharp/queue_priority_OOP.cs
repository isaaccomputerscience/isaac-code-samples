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
    private int priority;
    private Node next;

    // Constructor method
    public Node(string itemData, int itemPriority)
    {
        data = itemData;
        priority = itemPriority;
    }

    public string GetData()
    {
        return data;
    }

    public int GetPriority()
    {
        return priority;
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
            Console.WriteLine($"Data: {data}, priority: {priority}, next: {nextData}");
        }
    }


    // A priority queue stored as a linked list
    class PriorityQueue
    {
        private Node front;
        private Node rear;

        public Node GetFront()
        {
            return front;
        }

        public void SetFront(Node newFront)
        {
            front = newFront;
        }

        public Node GetRear()
        {
            return rear;
        }

        public void SetRear(Node newRear)
        {
            rear = newRear;
        }

        // Check if the queue is empty
        public bool IsEmpty()
        {
            if (front == null)
                return true;
            else
                return false;
        }

        // Enqueue an item based on the priority
        public void Enqueue(string data, int itemPriority)
        {
            Node newNode = new Node(data, itemPriority);

            // Check if the queue is empty
            if (IsEmpty()) {
                front = newNode;
                rear = newNode;
            }
            else {
                // Check if new node should be the new front of queue
                if (newNode.GetPriority() > front.GetPriority()) {
                    // Change the current head pointer
                    newNode.SetNext(front);
                    front = newNode;
                }
                // Check if new node should be added to the end of the queue
                else if (newNode.GetPriority() <= rear.GetPriority()) {
                    rear.SetNext(newNode);
                    rear = newNode;
                }
                else {
                    // Find the insertion point
                    Node current = front;
                    Node previous = null;
                    while (current.GetPriority() >= newNode.GetPriority()) {
                        previous = current;
                        current = current.GetNext();
                    }
                    newNode.SetNext(current);
                    previous.SetNext(newNode);
                }
            }
        }

        // Dequeue an item
        public string Dequeue()
        {
            string dequeuedItem;

            if (IsEmpty()) {
                Console.WriteLine("\nQueue is empty - nothing to dequeue");
                dequeuedItem = "";
            }
            else {
                // Get data and change pointer to next item
                dequeuedItem = front.GetData();
                front = front.GetNext();
            }

            return dequeuedItem;
        }

        // Output the state of the queue
        public void OutputQueue()
        {
            // Testing
            if (front != null) {
                Console.WriteLine("------ State of the queue ------");
                Console.Write("Head ");
                Node currentNode = front;
                currentNode.OutputNode();
                while (currentNode.GetNext() != null) {
                    currentNode = currentNode.GetNext();
                    currentNode.OutputNode();
                }
                Console.WriteLine();
            }
        }
    }


    class Queues
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            Console.WriteLine("### Priority queue (OOP) ###\n");

            // Initialise the queue
            PriorityQueue myQueue = new PriorityQueue();

            // Insert test data into the queue
            TestEnqueue(myQueue);
            
            // Remove test data from the queue
            TestDequeue(myQueue);
        }

        public static void TestEnqueue(PriorityQueue myQueue)
        {
            Console.WriteLine("Adding A with priority 3");
            myQueue.Enqueue("A", 3);
            myQueue.OutputQueue();
            
            Console.WriteLine("Adding B with priority 2 - should be behind A");
            myQueue.Enqueue("B", 2);
            myQueue.OutputQueue();
            
            Console.WriteLine("Adding C with priority 3 - should be in front of B");
            myQueue.Enqueue("C", 3);
            myQueue.OutputQueue();
            
            Console.WriteLine("Adding D with priority 3 - should be after C");
            myQueue.Enqueue("D", 3);
            myQueue.OutputQueue();
            
            Console.WriteLine("Adding E with priority 3 - should be after D");
            myQueue.Enqueue("E", 3);
            myQueue.OutputQueue();
            
            Console.WriteLine("Adding F with priority 1 - should be after B");
            myQueue.Enqueue("F", 1);
            myQueue.OutputQueue();
            
            Console.WriteLine("Adding G with priority 4 - should be head of queue");
            myQueue.Enqueue("G", 4);
            myQueue.OutputQueue();
            
            Console.WriteLine("Adding H with priority 5 - should be head of queue");
            myQueue.Enqueue("H", 5);
            myQueue.OutputQueue();
            
            Console.WriteLine("Adding I with priority 5 - should be after H");
            myQueue.Enqueue("I", 5);
            myQueue.OutputQueue();
        }

        public static void TestDequeue(PriorityQueue myQueue)
        {
            Console.WriteLine("\n------ Dequeuing 10 items ------\n");

            for (int i = 0; i < 10; i++)
            {
                myQueue.Dequeue();
                myQueue.OutputQueue();
            }
        }

    }
}