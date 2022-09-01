# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


import sys

# Index values for cost and previous
COST = 0
PREVIOUS = 1

def display_graph(graph):
    """Display each node with it's neighbours and costs"""
    
    # Repeat for each node in the graph
    for key, value in graph.items():
        print(f"Node: {key}")
        print("Neighbours:", end=" ")

        # Repeat for each neighbour of the node
        for neighbour in value:
            print(f"{neighbour}:{value[neighbour]}", end = " ")
        print("\n")
        
        
def display_list(list_as_dictionary):
    """Display a list of nodes with their closest neighbour and cost"""

    # Repeat for each node in the given dictionary
    for key, value in list_as_dictionary.items():
        print(f"{key}:  {value}")
    print()


def display_shortest_paths(visited, start_node):
    """Display the shortest path from the start node to other nodes"""
    
    print("\nShortest paths:")

    # Repeat for each node in the visited dictionary
    for key, value in visited.items():
        # Don't print the path for the start node
        if key != start_node:
            # Set the current node and the path as the key node
            current_node = key
            path = key

            # Repeat until the current node reaches the start node
            while current_node != start_node:
                # Add the previous node to the start of the path
                previous_node = visited[current_node][PREVIOUS]
                path = previous_node + path
                
                # Update the current node to be the previous node
                current_node = visited[current_node][PREVIOUS]
                
            # Testing
            print(f"Path for {key} with cost {visited[key][COST]}: ", end="")
            print(path)


def dijkstras_shortest_path(graph, start_node):
    """Apply Dijkstra's shortest path algorithm"""

    # Declare the visited and unvisited dictionaries
    unvisited = {}
    visited = {}

    # Add every node to the unvisited dictionary
    for key in graph:
        # Set distance to sys.maxsize for infinity and previous to None
        unvisited[key] = [sys.maxsize, None]
        
    # Set the cost of the start node to 0
    unvisited[start_node][COST] = 0
    
    print("--- Initialised state of unvisited list ---")
    display_list(unvisited)
   
    # Repeat until there are no more nodes in the unvisited dictionary
    finished = False
    while finished == False:
        # Check if there are no more nodes left to evaluate
        if len(unvisited) == 0:
            finished = True
        else:
            # Get the unvisited node with the lowest cost
            current_node = min(unvisited, key = unvisited.get)
            print(f"\nCurrent node >>> {current_node}") # Testing

            # Get the current node's dictionary of neighbours
            neighbours = graph[current_node]

            # Repeat for each node in the neighbours dictionary
            for node in neighbours:
                # Check if the node has already been visited
                if node not in visited:
                    # Calculate the new cost
                    cost = unvisited[current_node][COST] + neighbours[node]

                    # Check if the new cost is less
                    if cost < unvisited[node][COST]:
                        # Update cost and previous node
                        unvisited[node][COST] = cost
                        unvisited[node][PREVIOUS] = current_node

                        # Testing
                        print(f"Updated unvisited list with min distances from node {current_node}")
                        print("--- Unvisited list ---")
                        display_list(unvisited)

            # Add the current node to the visited dictionary
            visited[current_node] = unvisited[current_node]

            # Remove the current node from the unvisited dictionary
            del unvisited[current_node]

            # Testing
            print(f"Updated visited list with node {current_node}")
            print("--- Visited list ---")
            display_list(visited)

    return visited


def main():
    """Perform Dijkstra's shortest path algorithm on the test data"""

    # Use a dictionary to represent the nodes of a graph
    # and the cost of each neighbour
    test_graph = {"A": {"B":8, "C":5},
             "C": {"A":5, "D":6, "E":9},
             "B": {"A":8, "D":1},
             "D": {"C":6, "B":1, "E":2},
             "E": {"C":9, "D":2}
             }
    
    print("### Dijkstra's shortest path algorithm ###")
    print("\nDisplay graph: \n")
    display_graph(test_graph)

    # Perform the shortest path algorithm on each node starting from node A
    visited_dictionary = dijkstras_shortest_path(test_graph, "A")

    # Display the shortest paths from node A using the visited dictionary
    display_shortest_paths(visited_dictionary, "A")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
