# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


# Use sys.maxsize to represent infinity
import sys


# Index values for g-score, f-score and previous node
G_SCORE = 0
F_SCORE = 1
PREVIOUS = 2


def display_graph(graph):
    """Display each node with it's neighbours and costs"""
    
    # Repeat for each node in the graph
    for node, neighbours in graph.items():
        print(f"Node: {node}")
        print("Neighbours:", end=" ")

        # Repeat for each neighbour node (n_node) in the neighbours list
        for n_node in neighbours:
            print(f"{n_node}:{neighbours[n_node]}", end = " ")
        print("\n")
        
        
def display_list(adjacency_list):
    """Display a list of nodes with their closest neighbour and scores"""

    print("   (g-score, f-score, previous)")

    # Repeat for each node in the given adjacency list
    for node, neighbours in adjacency_list.items():
        print(f"{node}: {neighbours}")
    print()


def display_shortest_path(visited, start_node, target_node):
    """Display the shortest path from start node to target node"""

    # Set the current node and the path as the target node
    current_node = target_node
    path = target_node

    # Repeat until the current node reaches the start node
    while current_node != start_node:
        # Add the previous node to the start of the path
        previous_node = visited[current_node][PREVIOUS]
        path = previous_node + path

        # Update the current node to be the previous node
        current_node = previous_node

    # Testing
    cost = visited[target_node][G_SCORE]
    print(f"The shortest path from {start_node} to {target_node} is:")
    print(f"Path: {path}")
    print(f"Cost: {cost}")


    
def get_heuristic(node):
    """Returns heuristic values for the graph as used on the Isaac CS platform"""

    if node == "A":
        estimated_distance_to_target = 10
    elif node == "B":
        estimated_distance_to_target = 15
    elif node == "C":
        estimated_distance_to_target = 5
    elif node == "D":
        estimated_distance_to_target = 5
    elif node == "E":
        estimated_distance_to_target = 10
    elif node == "F":
        estimated_distance_to_target = 0
    else:
        estimated_distance_to_target = 0
    
    return estimated_distance_to_target


def get_minimum(unvisited):
    """Returns the node with the lowest f-score"""

    # Set the lowest value to sys.maxsize for infinity
    lowest_value_node = sys.maxsize
    lowest_key = ""

    # Repeat for each node in the unvisited list
    for node in unvisited.items():
        # Get the f-score value
        f_score_value = node[1][F_SCORE]

        # Check if the f-score is less than the lowest value
        if f_score_value < lowest_value_node:
            # Update lowest value and lowest key
            lowest_value_node = f_score_value
            lowest_key = node[0]
            
    return lowest_key


def a_star(graph, start_node, target_node):
    """Apply the A* algorithm on a graph stored as a dictionary"""
    
    # Declare the visited and unvisited lists as dictionaries
    visited = {} 
    unvisited = {}

    # Add and initialise every node to the unvisited list
    for node in graph:
        # Initialise g-score and f-score to sys.maxsize (for infinity)
        # and the previous node to None
        unvisited[node] = [sys.maxsize, sys.maxsize, None]

    # Update the values for the start node in the unvisited list
    f_score_value = get_heuristic(start_node)
    unvisited[start_node] = [0, f_score_value, None]
    
    # Testing
    print("--- Initialised state of unvisited list ---")
    display_list(unvisited)

    # Repeat until there are no more nodes in the unvisited list
    finished = False
    while finished == False:
        # Check if there are no more nodes left to evaluate
        if len(unvisited) == 0:
            finished = True
        else:
            # Get the unvisited node with the lowest f-score
            current_node = get_minimum(unvisited)
            print(f"\nCurrent node >>> {current_node}") # Testing

            # Check if the current node is the target node
            if current_node == target_node:
                # Add the current node to the visited list
                finished = True
                visited[current_node] = unvisited[current_node]
            else:
                # Get the current node's list of neighbours
                neighbours = graph[current_node]

                # Repeat for each neighbour node in the neighbours list
                for node in neighbours:
                    # Check if the neighbour node has already been visited
                    if node not in visited:
                        # Calculate the new g-score
                        new_g_score = unvisited[current_node][G_SCORE] + neighbours[node]

                        # Check if the new g-score is less
                        if new_g_score < unvisited[node][G_SCORE]:
                            # Update g-score, f-score and previous node
                            unvisited[node][G_SCORE] = new_g_score
                            unvisited[node][F_SCORE] = new_g_score + get_heuristic(node)
                            unvisited[node][PREVIOUS] = current_node

                # Testing
                print("--- Unvisited list ---")
                display_list(unvisited)

                # Add the current node to the visited list
                visited[current_node] = unvisited[current_node]

                # Remove the current node from the unvisited list
                del unvisited[current_node]

                # Testing
                print(f"Moved {current_node} to visited list")
                print("--- Visited list ---")
                display_list(visited)

    # Testing
    print("--- Visited list ---")
    display_list(visited)

    # Return the final visited list
    return visited


def main():
    """Perform the A* algorithm on the test data"""

    # Use a dictionary to represent the graph as an adjacency list
    # and the g-score and f-score of each neighbour
    test_graph = {"A": {"B": 10, "C": 12, "D": 5},
             "B": {"A": 10, "E": 11},
             "C": {"A": 12, "D": 6, "E": 11, "F": 8},
             "D": {"A": 5, "C": 6, "F": 14},
             "E": {"B": 11, "C": 11},
             "F": {"C": 8, "D": 14}
             }
    
    print("### A* algorithm ###")
    print("\nDisplay graph: \n")
    display_graph(test_graph)

    # Perform the A* algorithm between nodes A and F
    visited_list = a_star(test_graph, "A", "F")

    # Display the shortest path using the visited list
    display_shortest_path(visited_list, "A", "F") 


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
