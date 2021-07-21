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
    
    class StandardUses  // Binary search tree
    {
        
        // The Main method is the entry point for all C# programs
        public static void Main() {
            BST myBST = new BST();
            TestData(myBST);  // Create some test data
            Test(myBST);  // Run test script
        }
        

        // A recursive search of a binary search tree
        public static bool BSTSearch(Node node, string searchItem) {
            int compare = String.Compare(searchItem, node.data, StringComparison.OrdinalIgnoreCase);
            if (searchItem == node.data) {
                return true;
            } else if (compare > 0 && node.right != null) {
                    return BSTSearch(node.right, searchItem);
            } else if (compare < 0 && node.left != null) {
                return BSTSearch(node.left, searchItem);
            }
            return false;
        }
        

        // Inserts some data into tree
        public static void TestData(BST bst) {
            bst.Insert("fred");
            bst.Insert("elaine");
            bst.Insert("george");
            bst.Insert("harry");
        } 
        

        public static void Test(BST bst) {
            // Carries out some basic tests
            Node startNode = bst.GetRoot();
            if (BSTSearch(startNode, "aaron") != false) {
                Console.WriteLine("aaron - test failed");
            }
            if (BSTSearch(startNode, "harry") != true) {
                Console.WriteLine("harry - test failed");
            }
            if (BSTSearch(startNode, "zac") != false) {
                Console.WriteLine("zac - test failed");
            }
            Console.WriteLine("Test complete");
        }  
        
        
    }
}
