/*
Note: This file is designed to be copied out and compiled on your machine. 
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file. 

To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Compile the program
4. Run the program
*/

using System;

namespace isaac_code_samples
{
    class Node
    {
        // Node in a Binary search tree
        public string data;
        public Node left;
        public Node right;

        public Node(string new_data){
            data = new_data;
        }
    }

    class BST
    {
        public Node root;

        public Node GetRoot(){
            return root;
        }

        public void Insert(string data){
            // Insert a new node
            Node newNode = new Node(data);
            if (root == null){
                root = newNode;
            }else {
                bool placed = false;
                Node current = root;
                while (placed == false){
                    if (current.data[0] > data[0]){ // Go left
                        if (current.left == null){
                            current.left = newNode;
                            placed = true;
                        }else {
                            current = current.left;
                        }
                    }else { //Go right
                        if (current.right == null){
                            current.right = newNode;
                            placed = true;
                        }else {
                            current = current.right;
                        }
                    }
                }
            }
        }
    }
}
