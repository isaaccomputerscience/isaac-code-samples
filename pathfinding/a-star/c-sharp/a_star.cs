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
using System.Linq;

namespace IsaacCodeSamples
{
    class Pathfinding
    {
        // Index values for g-score, f-score and previous
        public const int GScore = 0;
        public const int FScore = 1;
        public const int Previous = 2;

        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            // Use a dictionary to represent the graph as an adjacency list
            // and the g-score and f-score of each neighbour
            var testGraph = new Dictionary<string, Dictionary<string, int>>
            {
                {"A", new Dictionary<string, int> { {"B", 10}, {"C", 12}, {"D", 5} } },
                {"B", new Dictionary<string, int> { {"A", 10}, {"E", 11} } },
                {"C", new Dictionary<string, int> { {"A", 12}, {"D", 6}, {"E", 11}, {"F", 8} } },
                {"D", new Dictionary<string, int> { {"A", 5}, {"C", 6}, {"F", 14} } },
                {"E", new Dictionary<string, int> { {"B", 11}, {"C", 11} } },
                {"F", new Dictionary<string, int> { {"C", 8}, {"D", 14} } }
            };

            Console.WriteLine("### A* algorithm ###");
            Console.WriteLine("\nDisplay graph: \n");
            DisplayGraph(testGraph);

            // Perform the A* algorithm between nodes A and F
            var visitedList = AStar(testGraph, "A", "F");

            // Display the shortest path using the visited list
            DisplayShortestPath(visitedList, "A", "F");
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

        // Display a list of nodes with their closest neighbour and scores
        public static void DisplayList(Dictionary<string, List<object>> adjacencyList)
        {
            Console.WriteLine("   (g-score, f-score, previous)");

            // Repeat for each node in the given adjacency list
            foreach (KeyValuePair<string, List<object>> kvp in adjacencyList) {
                string node = kvp.Key;
                List<object> neighbours = kvp.Value;

                // If the neighbour node (nNode) does not exist then set the string to "null"
                string nNode = neighbours[Previous] == null ? "null" : (string)neighbours[Previous];
                
                Console.WriteLine($"{node}: {neighbours[GScore]}, {neighbours[FScore]}, {nNode}");
            }
            Console.WriteLine();
        }

        // Display the shortest path from start node to target node
        public static void DisplayShortestPath(Dictionary<string, List<object>> visited, 
            string startNode, string targetNode)
        {
            // Set the current node and the path as the key node
            string currentNode = targetNode;
            string path = targetNode;

            // Repeat until the current node reaches the start node
            while (currentNode != startNode) {
                // Add the previous node to the start of the path
                string previousNode = (string)visited[currentNode][Previous];
                path = previousNode + path;
                
                // Update the current node to be the previous node
                currentNode = previousNode;
            }

            // Testing
            int cost = (int)visited[targetNode][GScore];
            Console.WriteLine($"The shortest path from {startNode} to {targetNode} is:");
            Console.WriteLine($"Path: {path}");
            Console.WriteLine($"Cost: {cost}");
        }

        // Returns heuristic values for the graph as used on the Isaac CS platform
        public static int GetHeuristic(string node)
        {
            int estimatedDistanceToTarget;

            if (node == "A") {
                estimatedDistanceToTarget = 10;
            }
            else if (node == "B") {
                estimatedDistanceToTarget = 15;
            }
            else if (node == "C") {
                estimatedDistanceToTarget = 5;
            }
            else if (node == "D") {
                estimatedDistanceToTarget = 5;
            }
            else if (node == "E") {
                estimatedDistanceToTarget = 10;
            }
            else if (node == "F") {
                estimatedDistanceToTarget = 0;
            }
            else {
                estimatedDistanceToTarget = 0;
            }
            
            return estimatedDistanceToTarget;
        }

        // Returns the node with the lowest f-score
        public static string GetMinimum(Dictionary<string, List<object>> unvisited)
        {
            // Set the lowest value to Int32.MaxValue for infinity
            int lowestValueNode = Int32.MaxValue;
            string lowestKey = "";

            // Repeat for each node in the unvisited list
            foreach (KeyValuePair<string, List<object>> kvp in unvisited) {
                List<object> node = kvp.Value;

                // Get the f-score value
                int fScoreValue = (int)node[FScore];

                // Check if the f-score is less than the lowest value
                if (fScoreValue < lowestValueNode) {
                    // Update lowest value and lowest key
                    lowestValueNode = fScoreValue;
                    lowestKey = kvp.Key;
                }
            }
            return lowestKey;
        }

        // Apply the A* algorithm
        public static Dictionary<string, List<object>> AStar(
            Dictionary<string, Dictionary<string, int>> graph, string startNode, string targetNode)
        {
            // Declare the visited and unvisited lists as dictionaries
            Dictionary<string, List<object>> unvisited = new Dictionary<string, List<object>>();
            Dictionary<string, List<object>> visited = new Dictionary<string, List<object>>();

            // Add and initialise every node to the unvisited list
            foreach (KeyValuePair<string, Dictionary<string, int>> kvp in graph) {
                // Get the node
                string node = kvp.Key;

                // Initialise g-score and f-score to Int32.MaxValue (for infinity)
                //  and the previous node to null
                unvisited[node] = new List<object>() {Int32.MaxValue, Int32.MaxValue, null};
            }

            // Update the values for the start node in the unvisited list
            int fScoreValue = GetHeuristic(startNode);
            unvisited[startNode] = new List<object>() {0, fScoreValue, null};
            
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
                    // Get the unvisited node with the lowest f-score
                    string currentNode = GetMinimum(unvisited);
                    Console.WriteLine($"\nCurrent node >>> {currentNode}"); // Testing

                    // Check if the current node is the target node
                    if (currentNode == targetNode) {
                        // Add the current node to the visited list
                        finished = true;
                        visited[currentNode] = unvisited[currentNode];
                    }
                    else {
                        // Get the current node's list of neighbours
                        Dictionary<string, int> neighbours = graph[currentNode];

                        // Repeat for each neighbour node in the neighbours list
                        foreach (KeyValuePair<string, int> kvp in neighbours) {
                            // Get the neighbour node
                            string node = kvp.Key;

                            // Check if the neighbour node has already been visited
                            if (visited.ContainsKey(node) == false) {
                                // Calculate the new g-score
                                int newGScore = (int)unvisited[currentNode][GScore] + neighbours[node];

                                // Check if the new g-score is less
                                if (newGScore < (int)unvisited[node][GScore]) {
                                    // Update g-score, f-score and previous node
                                    unvisited[node][GScore] = newGScore;
                                    unvisited[node][FScore] = newGScore + GetHeuristic(node);
                                    unvisited[node][Previous] = currentNode;
                                }
                            }
                        }
                        // Testing
                        Console.WriteLine("--- Unvisited list ---");
                        DisplayList(unvisited);

                        // Add the current node to the visited list
                        visited[currentNode] = unvisited[currentNode];

                        // Remove the current node from the unvisited list
                        unvisited.Remove(currentNode);

                        // Testing
                        Console.WriteLine($"Moved {currentNode} to visited list");
                        Console.WriteLine("--- Visited list ---");
                        DisplayList(visited);
                    }
                }
            }
            // Testing
            Console.WriteLine("--- Visited list ---");
            DisplayList(visited);

            // Return the final visited list
            return visited;
        }

        
    }
}