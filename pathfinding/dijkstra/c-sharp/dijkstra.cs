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
using System.Collections.Generic;
using System.Linq;

namespace IsaacCodeSamples
{
    class Pathfinding
    {
        // Index values for cost and previous node
        public const int Cost = 0;
        public const int Previous = 1;

        // The Main method is the entry point for all C# programs
        public static void Main()
        { 
            // Use a dictionary to represent the graph as an adjacency list
            // and the cost of each neighbour
            var testGraph = new Dictionary<string, Dictionary<string, int>>
            {
                {"A", new Dictionary<string, int> { {"B", 8}, {"C", 5} } },
                {"C", new Dictionary<string, int> { {"A", 5}, {"D", 6}, {"E", 9} } },
                {"B", new Dictionary<string, int> { {"A", 8}, {"D", 1} } },
                {"D", new Dictionary<string, int> { {"C", 6}, {"B", 1}, {"E", 2} } },
                {"E", new Dictionary<string, int> { {"C", 9}, {"D", 2} } }
            };

            Console.WriteLine("### Dijkstra's shortest path algorithm ###");
            Console.WriteLine("\nDisplay graph: \n");
            DisplayGraph(testGraph);

            // Perform the shortest path algorithm on each node starting from node A
            var visitedList = DijkstrasShortestPath(testGraph, "A");

            // Display the shortest paths from node A using the visited list
            DisplayShortestPaths(visitedList, "A");
        }

        // Display each node with it's neighbours and costs
        public static void DisplayGraph(Dictionary<string, Dictionary<string, int>> graph)
        {
            // Repeat for each node in the graph
            foreach (KeyValuePair<string, Dictionary<string, int>> kvp in graph) {
                string node = kvp.Key;
                Dictionary<string, int> neighbours = kvp.Value;

                Console.WriteLine($"Node: {kvp.Key}");
                Console.Write("Neighbours: ");
                
                // Repeat for each neighbour node in the neighbours list
                foreach (KeyValuePair<string, int> n_node in neighbours) {
                    Console.Write($"{n_node.Key}:{n_node.Value} ");
                }
                Console.WriteLine("\n");
            }
        }

        // Display a list of nodes with their closest neighbour and cost
        public static void DisplayList(Dictionary<string, List<object>> adjacencyList)
        {
            Console.WriteLine("   (cost, previous)");

            // Repeat for each node in the given adjacency list
            foreach (KeyValuePair<string, List<object>> kvp in adjacencyList) {
                string node = kvp.Key;
                List<object> neighbours = kvp.Value;
                
                // If the neighbour node (nNode) does not exist then set the string to "null"
                string nNode = neighbours[Previous] == null ? "null" : (string)neighbours[Previous];
                
                Console.WriteLine($"{node}: {neighbours[Cost]}, {nNode}");
            }
            Console.WriteLine();
        }

        // Display the shortest path from the start node to other nodes
        public static void DisplayShortestPaths(Dictionary<string, List<object>> visited, 
            string startNode)
        {
            Console.WriteLine("\nShortest paths:");

            // Repeat for each node in the visited list
            foreach (KeyValuePair<string, List<object>> kvp in visited) {
                // Don't print the path for the start node
                if (kvp.Key != startNode) {
                    // Set the current node and the path as the key node
                    string currentNode = kvp.Key;
                    string path = kvp.Key;

                    // Repeat until the current node reaches the start node
                    while (currentNode != startNode) {
                        // Add the previous node to the start of the path
                        string previousNode = (string)visited[currentNode][Previous];
                        path = previousNode + path;
                        
                        // Update the current node to be the previous node
                        currentNode = previousNode;
                    }

                    // Testing
                    Console.Write($"Path for {kvp.Key} with cost {visited[kvp.Key][Cost]}: ");
                    Console.WriteLine(path);
                }

            }
        }

        // Apply Dijkstra's shortest path algorithm on a graph stored as a dictionary
        public static Dictionary<string, List<object>> DijkstrasShortestPath(
            Dictionary<string, Dictionary<string, int>> graph, string startNode)
        {
            // Declare the visited and unvisited lists as dictionaries
            Dictionary<string, List<object>> unvisited = new Dictionary<string, List<object>>();
            Dictionary<string, List<object>> visited = new Dictionary<string, List<object>>();

            // Add and initialise every node to the unvisited list
            foreach (KeyValuePair<string, Dictionary<string, int>> kvp in graph) {
                // Get the node
                string node = kvp.Key;

                // Initialise the node's distance to Int32.MaxValue (for infinity)
                // and the previous node to null
                unvisited[node] = new List<object>() {Int32.MaxValue, null};
            }

            // Set the cost of the start node to 0
            unvisited[startNode][Cost] = 0;
            
            // Testing
            Console.WriteLine("--- Initialised state of unvisited list ---");
            DisplayList(unvisited);

            // Repeat until there are no more nodes in the unvisited list
            bool finished = false;
            while (finished == false) {
                // Check if there are no more nodes left to evaluate
                if (unvisited.Count == 0)
                    finished = true;
                else {
                    // Get the unvisited node with the lowest cost
                    int min = unvisited.Min(item => (int)item.Value[Cost]);
                    string currentNode = unvisited.Where(pair => pair.Value.Contains(min)).FirstOrDefault().Key;
                    Console.WriteLine($"\nCurrent node >>> {currentNode}"); // Testing

                    // Get the current node's list of neighbours
                    Dictionary<string, int> neighbours = graph[currentNode];

                    // Repeat for each node in the neighbours list
                    foreach (KeyValuePair<string, int> kvp in neighbours) {
                        // Get the neighbour node
                        string node = kvp.Key;

                        // Check if the neighbour node has already been visited
                        if (visited.ContainsKey(node) == false) {
                            // Calculate the new cost
                            int cost = (int)unvisited[currentNode][Cost] + neighbours[node];

                            // Check if the new cost is less
                            if (cost < (int)unvisited[node][Cost]) {
                                // Update cost and previous node
                                unvisited[node][Cost] = cost;
                                unvisited[node][Previous] = currentNode;

                                // Testing
                                Console.WriteLine($"Updated unvisited list with min distances from node {currentNode}");
                                Console.WriteLine("--- Unvisited list ---");
                                DisplayList(unvisited);
                            }
                        }
                    }
                    // Add the current node to the visited list
                    visited[currentNode] = unvisited[currentNode];

                    // Remove the current node from the unvisited list
                    unvisited.Remove(currentNode);

                    // Testing
                    Console.WriteLine($"Updated visited list with node {currentNode}");
                    Console.WriteLine("--- Visited list ---");
                    DisplayList(visited);
                }
            }
            // Return the final visited list
            return visited;
        }

        
    }
}