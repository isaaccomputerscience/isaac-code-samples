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

namespace Recursion
{
    class BinaryTreeTraversal
    {
        // The Main method is the entry point for all C# programs
        static void Main(string[] args) {
            BST myTree = new BST();
            TestData(myTree);  // Create some test data
            Node start = myTree.GetRoot();  // Get start node
            TraverseInOrder(start); 
        }
        

        // Inserts some data into the tree
        static void TestData(BST bst) {
            bst.Insert("Zac");
            bst.Insert("Lucy");
            bst.Insert("Anil");
            bst.Insert("Boris");
        }

        
        // In order binary search traversal
        static void TraverseInOrder(Node node) {    
            if (node != null) {
                TraverseInOrder(node.left);
                Console.WriteLine(node.data);
                TraverseInOrder(node.right);
            }
        }
        
        
    }
}
