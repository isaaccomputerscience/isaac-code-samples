/*
Isaac Computer Science
Usage licensed under the Open Government Licence v3.0

Note: This file is designed to be copied out and compiled on your machine.
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file.
To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Change the namespace to match your project (if neccesary)
4. Compile the program
5. Run the program
*/

using System;

namespace IsaacCodeSamples 
    
{
    class StandardUses  // Binary tree traversal
    {
        
        // The Main method is the entry point for all C# programs
        public static void Main() {
            BST myTree = new BST();
            TestData(myTree);  // Create some test data
            Node start = myTree.GetRoot();  // Get start node
            TraverseInOrder(start); 
        }
        

        // Inserts some data into the tree
        public static void TestData(BST bst) {
            bst.Insert("Zac");
            bst.Insert("Lucy");
            bst.Insert("Anil");
            bst.Insert("Boris");
        }

        
        // In order binary search traversal
        public static void TraverseInOrder(Node node) {    
            if (node != null) {
                TraverseInOrder(node.left);
                Console.WriteLine(node.data);
                TraverseInOrder(node.right);
            }
        }
        
        
    }
}
