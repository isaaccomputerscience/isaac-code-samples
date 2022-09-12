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
using System.Collections.Generic;

namespace IsaacCodeSamples
{
    class Graph
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Use a dictionary to represent the graph as an adjacency list.
            // Each key is a node in the graph.
            // Each value is a list of the node's neighbours
            var testGraph = new Dictionary<string, List<string>>() {
                {"1", new List<string>() {"2", "9"} },
                {"2", new List<string>() {"1"} },
                {"3", new List<string>() {"4", "5", "6", "9"} },
                {"4", new List<string>() {"3"} },
                {"5", new List<string>() {"3", "8"} },
                {"6", new List<string>() {"3", "7"} },
                {"7", new List<string>() {"6", "8"} },
                {"8", new List<string>() {"5", "7"} },
                {"9", new List<string>() {"1", "3", "7"} }
            };

            Console.WriteLine("### Depth-first search (DFS) - Graph implementation ###");

            // Search for a value and return true if it has been found
            string itemToFind = "4";
            string start = "1";
            bool found = DepthFirstSearch(testGraph, start, itemToFind);

            // Output the search result
            Console.WriteLine($"\nThe target node is {itemToFind}");
            if (found == true) {
                Console.WriteLine($"{itemToFind} was found in the graph");
            }
            else {
                Console.WriteLine($"{itemToFind} was NOT found in the graph");
            }
        }

        // A depth-first search performed on a graph stored as a dictionary
        public static bool DepthFirstSearch(Dictionary<string, List<string>> graph, 
            string startNode, string targetNode)
        {
            // Initialisation
            List<string> stack = new List<string>() {startNode};
            List<string> discovered = new List<string>() {startNode};
            List<string> neighbours = new List<string>();
            bool found = false;

            // Repeat while there are items in the stack
            // and the target node has not been found 
            while (stack.Count != 0 && found == false) {

                // Set the current node to the top item in the stack
                string currentNode = stack[stack.Count - 1];

                // Remove the current node from the top of the stack
                stack.RemoveAt(stack.Count - 1);

                // Get the current node's list of neighbours
                neighbours = graph[currentNode];

                // Testing
                Console.Write("\nStack: ");
                Console.WriteLine("[{0}]", string.Join(", ", stack));
                Console.Write("Discovered: ");
                Console.WriteLine("[{0}]", string.Join(", ", discovered));
                Console.Write("Neighbours: ");
                Console.WriteLine("[{0}]", string.Join(", ", neighbours));

                // Repeat for each node in the neighbours list
                foreach (string node in neighbours) {
                    // Check if the node has not already been discovered
                    if (discovered.Contains(node) == false) {
                        // Check if the target node has been found
                        if (node == targetNode) {
                            found = true;
                        }
                        else {
                            // Push the node onto the stack 
                            // and add it to the discovered list
                            stack.Add(node);
                            discovered.Add(node);

                            // Testing
                            Console.Write("\nStack: ");
                            Console.WriteLine("[{0}]", string.Join(", ", stack));
                            Console.Write("Discovered: ");
                            Console.WriteLine("[{0}]", string.Join(", ", discovered));
                            Console.Write("Neighbours: ");
                            Console.WriteLine("[{0}]", string.Join(", ", neighbours));
                        }
                    }
                }
            }
            return found;
        }

        
    }
}