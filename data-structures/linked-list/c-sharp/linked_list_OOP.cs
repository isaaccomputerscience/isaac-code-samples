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
    // A class for a node in the linked list
    class Node
    {
        private string data;
        private Node next;

        // Constructor method
        public Node(string givenData)
        {
            data = givenData;
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
    }


    // A class for the linked list
    class LinkedList
    {
        private Node head; // Do not intialise yet as the linked list is empty

        public Node GetHead()
        {
            return head;
        }

        public void SetHead(Node newHead)
        {
            head = newHead;
        }

        // Insert a node to the front of the list
        public void InsertAtFront(string data)
        {
            // Create a new node
            Node newNode = new Node(data);

            // Check if the head node exists
            if (head == null) {
                SetHead(newNode);
            }
            else {
                // Update the pointers so the new node is the head
                newNode.SetNext(head);
                SetHead(newNode);
            }
        }


        // Insert a node into the correct position in an ordered list
        public void InsertInOrder(string data)
        {
            // Create a new node
            Node newNode = new Node(data);

            // Start at the head of the list
            Node current = GetHead();

            // Check if there are no nodes in the list
            if (current == null) {
                SetHead(newNode);
            }

            // Check if the new node data is before the head data
            else if (String.Compare(newNode.GetData(), current.GetData()) < 0) {
                // Set the new node as the head of the list
                newNode.SetNext(head);
                SetHead(newNode);
            }

            // Otherwise find where the new node should be positioned
            else {
                // Repeat until the point of insertion is found
                while (current.GetNext() != null 
                    && String.Compare(current.GetNext().GetData(), newNode.GetData()) < 0) {
                    // Get the next node
                    current = current.GetNext();
                }
                // Update the pointers of the new and current nodes
                newNode.SetNext(current.GetNext());
                current.SetNext(newNode);
            }
        }


        // Traverse the list and output the data from each node
        public void Traverse() 
        {
            // Set the current node as the head
            Node current = GetHead();

            // Repeat until there are no more linked nodes
            while (current != null) {
                Console.WriteLine(current.GetData());
                current = current.GetNext();
            }
        }


        // Delete a node. This assumes that the node does exist in the list
        public void Delete(string data)
        {
            // Start at the head of the list
            Node current = GetHead();

            // Check if the head node is to be deleted
            if (current.GetData() == data) {
                // Update the head pointer
                SetHead(current.GetNext());
            }
            else {
                // Repeat until the node has been found
                while (current.GetNext().GetData() != data) {
                    // Change the current node to be the next node
                    current = current.GetNext();
                }
                // Set the pointer to be the next node's pointer
                current.SetNext(current.GetNext().GetNext());
            }
        }


    }


    class DataStructures
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            Console.WriteLine("### Linked list (OOP) ###");

            // Instantiate an empty linked list object
            LinkedList myList = new LinkedList();

            // Insert test data into the linked list
            Console.WriteLine("\nInsert test data into the linked list in order:");
            InsertTestData(myList);
            myList.Traverse();

            // Testing - insert at front
            Console.WriteLine("\nInsert a node to the front of the list:");
            myList.InsertAtFront("Albus");
            myList.Traverse();

            // Testing - insert in order
            Console.WriteLine("\nInsert a node to the end of the list:");
            myList.InsertInOrder("Zeb");
            myList.Traverse();
            
            // Testing - delete a node
            Console.WriteLine("\nDelete a node from the list:");
            myList.Delete("Sabrina");
            myList.Traverse();
        }


        // Insert test data into the linked list
        public static void InsertTestData(LinkedList myList)
        {
                myList.InsertInOrder("Julie");
                myList.InsertInOrder("Rey");
                myList.InsertInOrder("Habib");
                myList.InsertInOrder("Sabrina");
                myList.InsertInOrder("Mina");
        }

        
    }
}