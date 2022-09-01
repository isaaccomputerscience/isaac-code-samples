# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def breadth_first_search(graph, start_node, target_node):
    """A breadth-first search performed on a graph"""

    # Initialise the variables
    queue = [start_node]
    discovered = [start_node]
    neighbours = []
    found = False

    # Repeat while there are items in the queue
    # and the target node has not been found 
    while len(queue) != 0 and found == False:
        
        # Set the current node to the first item in the queue
        current_node = queue[0]

        # Remove the current node from the start of the queue
        queue = queue[1:]

        # Get the current node's list of neighbours
        neighbours = graph[current_node]

        # Testing
        print(f"\nQueue: {queue}")
        print(f"Discovered: {discovered}")
        print(f"Neighbours: {neighbours}")

        # Repeat for each node in the neighbours list
        for node in neighbours:
            # Check if the node has not already been discovered
            if node not in discovered:
                # Check if the target node has been found
                if node == target_node:
                    found = True
                # Otherwise append the node to the queue and discovered lists
                else:
                    queue.append(node)
                    discovered.append(node)

                    # Testing
                    print(f"\nQueue: {queue}")
                    print(f"Discovered: {discovered}")
                    print(f"Neighbours: {neighbours}")
                    
    return found




def main():
    """Create a graph and search for an item"""

    # Represent a graph using a dictionary with lists as values
    test_graph = {
        "1": ["2", "9"],
        "2": ["1"],
        "3": ["4", "5", "6", "9"],
        "4": ["3"],
        "5": ["3", "8"],
        "6": ["3", "7"],
        "7": ["6", "8", "9"],
        "8": ["5", "7"],
        "9": ["1", "3", "7"]
        }

    print("### Graph traversal - breadth-first search (BFS) ###")

    # Search for a value and return if it has been found
    item_to_find = "4"
    start = "1"
    found = breadth_first_search(test_graph, start, item_to_find)

    # Output the search result
    print(f"\nThe target node is {item_to_find}")
    
    if found == True:
        print(f"{item_to_find} was found in the graph")
    else:
        print(f"{item_to_find} does not exist in the graph")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
