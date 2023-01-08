# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


# Use sys.maxsize to represent infinity
import sys


# Index values for cost and previous node
COST = 0
PREVIOUS = 1


def display_graph(graph: dict) -> None:
    """Display each node with it's neighbours and costs"""

    # Repeat for each node in the graph
    for node, neighbours in graph.items():
        print(f"Node: {node}")
        print("Neighbours:", end=" ")

        # Repeat for each neighbour node (n_node) in the neighbours list
        for n_node in neighbours:
            print(f"{n_node}:{neighbours[n_node]}", end=" ")
        print("\n")


def display_list(adjacency_list: dict) -> None:
    """Display a list of nodes with their closest neighbour and cost"""

    print("   (cost, previous)")

    # Repeat for each node in the given adjacency list
    for node, neighbours in adjacency_list.items():
        print(f"{node}: {neighbours}")
    print()


def display_shortest_paths(visited: dict, start_node: str) -> None:
    """Display the shortest path from the start node to other nodes"""

    print("\nShortest paths:")

    # Repeat for each node in the visited list
    for node, neighbour in visited.items():
        # Don't print the path for the start node
        if node != start_node:
            # Set the current node and the path to be the visited node
            current_node = node
            path = node

            # Repeat until the current node reaches the start node
            while current_node != start_node:
                # Add the previous node to the start of the path
                previous_node = visited[current_node][PREVIOUS]
                path = previous_node + path

                # Update the current node to be the previous node
                current_node = visited[current_node][PREVIOUS]

            # Testing
            print(f"Path for {node} with cost {visited[node][COST]}: ", end="")
            print(path)


def dijkstras_shortest_path(graph: dict, start_node: str) -> dict:
    """Apply Dijkstra's shortest path algorithm on a graph stored as a dictionary"""

    # Declare the visited and unvisited lists as dictionaries
    unvisited = {}
    visited = {}

    # Add every node to the unvisited list
    for node in graph:
        # Initialise the node's distance to sys.maxsize (for infinity)
        # and the previous node to None
        unvisited[node] = [sys.maxsize, None]

    # Set the cost of the start node to 0
    unvisited[start_node][COST] = 0

    # Testing
    print("--- Initialised state of unvisited list ---")
    display_list(unvisited)

    # Repeat until there are no more nodes in the unvisited list
    finished = False
    while not finished:
        # Check if there are no more nodes left to evaluate
        if len(unvisited) == 0:
            finished = True
        else:
            # Get the unvisited node with the lowest cost
            current_node = min(unvisited, key=unvisited.get)
            print(f"\nCurrent node >>> {current_node}")  # Testing

            # Get the current node's list of neighbours
            neighbours = graph[current_node]

            # Repeat for each neighbour node in the neighbours list
            for node in neighbours:
                # Check if the neighbour node has already been visited
                if node not in visited:
                    # Calculate the new cost
                    cost = unvisited[current_node][COST] + neighbours[node]

                    # Check if the new cost is less
                    if cost < unvisited[node][COST]:
                        # Update cost and previous node
                        unvisited[node][COST] = cost
                        unvisited[node][PREVIOUS] = current_node

                        # Testing
                        print(
                            f"Updated unvisited list with min distances from node {current_node}")
                        print("--- Unvisited list ---")
                        display_list(unvisited)

            # Add the current node to the visited list
            visited[current_node] = unvisited[current_node]

            # Remove the current node from the unvisited list
            del unvisited[current_node]

            # Testing
            print(f"Updated visited list with node {current_node}")
            print("--- Visited list ---")
            display_list(visited)

    # Return the final visited list
    return visited


def main():
    """Perform Dijkstra's shortest path algorithm on the test data"""

    # Use a dictionary to represent the graph as an adjacency list
    # and the cost of each neighbour
    test_graph = {"A": {"B": 8, "C": 5},
                  "C": {"A": 5, "D": 6, "E": 9},
                  "B": {"A": 8, "D": 1},
                  "D": {"C": 6, "B": 1, "E": 2},
                  "E": {"C": 9, "D": 2}
                  }

    print("### Dijkstra's shortest path algorithm ###")
    print("\nDisplay graph: \n")
    display_graph(test_graph)

    # Perform the shortest path algorithm on each node starting from node A
    visited_list = dijkstras_shortest_path(test_graph, "A")

    # Display the shortest paths from node A using the visited list
    display_shortest_paths(visited_list, "A")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
