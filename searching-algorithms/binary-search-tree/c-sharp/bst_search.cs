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
    // A node in a binary search tree
    class Node
    {
        public int data;
        public Node left;
        public Node right;

        // Constructor method
        public Node(int data)
        {
            this.data = data;
        }
    }

    // A class for constructing a binary search tree (BST)
    class BST
    {
        private Node root; // Do not intialise the root yet as the tree is empty

        // Return the root node
        public Node GetRoot()
        {
            return root;
        }


        // Insert a new node
        public void Insert(int item)
        {
            // Create a new node
            Node newNode = new Node(item);

            // Check if the root node exists
            if (root == null) {
                // Set the root to be the new node
                root = newNode;
            }
            // Find the correct place to insert the new node
            else {
                Node current = root;
                bool placed = false;

                // Repeat while the data has not been inserted
                while (placed == false) {
                    // Check if the new item is greater than the current node data
                    if (item > current.data) {
                        // Check if the current node does not have a right child node
                        if (current.right == null) {
                            // Insert the new node to the right of the current node
                            current.right = newNode;
                            placed = true;
                        }
                        // Otherwise repeat with the current right node
                        else {
                            current = current.right;
                        }
                    }

                    // Otherwise the new item is less than or equal to the current node
                    else {
                        // Check if the current node does not have a left child node
                        if (current.left == null) {
                            // Insert the new node to the left of the current node
                            current.left = newNode;
                            placed = true;
                        }
                        // Otherwise repeat with the current left node
                        else {
                            current = current.left;
                        }
                    }
                }
            }
        }


        // Recursively searches for an item in a binary search tree
        public bool Search(Node node, int searchItem)
        {
            // Base case for recursion:
            // The recursion will stop if the search item has been found
            if (searchItem == node.data) {
                return true;
            }

            // Check if the search item is greater than the node data
            // and there is another node to the right to check
            else if (searchItem > node.data && node.right != null) {
                return Search(node.right, searchItem);
            }

            // Check if the search item is less than the node data
            // and there is another node to the left to check
            else if (searchItem < node.data && node.left != null) {
                return Search(node.left, searchItem);
            }

            // Base case for recursion:
            // Otherwise the search item does not exist
            else {
                return false;
            }
        }


    }

    class SearchingAlgorithms
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Instantiate a new tree object
            BST bst = new BST();

            // Insert test data into the binary search tree
            InsertTestData(bst);

            // Get the root node
            Node root = bst.GetRoot();

            // Testing
            Console.WriteLine("### Output the tree structure ###");
            Console.WriteLine("The root is the left-most value and the children are to the right\n");
            OutputTree(root);

            // Search for a value and return if it has been found
            int itemToFind = 6;
            bool found = bst.Search(root, itemToFind);

            // Output the search result
            Console.WriteLine($"\nThe search item is {itemToFind}");
            if (found == true) {
                Console.WriteLine($"{itemToFind} was found in the binary search tree");
            }
            else {
                Console.WriteLine($"{itemToFind} does not exist in the binary search tree");
            }
        }


        // Insert test data into the binary search tree
        public static void InsertTestData(BST bst)
        {
            bst.Insert(8);  // This will be the root node
            bst.Insert(3);
            bst.Insert(6);
            bst.Insert(10);
            bst.Insert(1);
            bst.Insert(5);
            bst.Insert(18);
            bst.Insert(7);
            bst.Insert(12);
        }


        // Output the tree with the root to the left and children to the right
        public static void OutputTree(Node node, int level = 0)
        {
            if (node != null) {
                OutputTree(node.right, level + 1);
                
                string spaces = new String(' ', 4 * level); // String of spaces
                Console.WriteLine($"{spaces}-> {node.data}");

                OutputTree(node.left, level + 1);
            }
        }

        
    }
}
