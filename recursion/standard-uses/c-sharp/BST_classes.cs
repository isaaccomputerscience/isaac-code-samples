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
    
    // Node in a binary search tree (BST)
    class Node
    {
        
        public string data;
        public Node left;
        public Node right;
        
        // Constructor
        public Node(string new_data) {
            data = new_data;
        }
        
    }

    // Binary search tree
    class BST
    {
        public Node root;

        public Node GetRoot() {
            return root;
        }
        

        // Insert a new node
        public void Insert(string data) {            
            Node newNode = new Node(data);
            if (root == null) {
                root = newNode;
            } else {
                bool placed = false;
                Node current = root;
                while (placed == false) {
                    if (current.data[0] > data[0]) {  // Go left
                        if (current.left == null) {
                            current.left = newNode;
                            placed = true;
                        } else {
                            current = current.left;
                        }
                    } else {  // Go right
                        if (current.right == null) {
                            current.right = newNode;
                            placed = true;
                        } else {
                            current = current.right;
                        }
                    }
                }
            }
        }
        
        
    }
}
