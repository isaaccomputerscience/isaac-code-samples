# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


class Node:
    """A node in a binary search tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """A class for constructing a binary search tree (BST)"""
    
    def __init__(self):
        """Constructor method"""
        self.root = None  # Initialise to None as the tree is empty
    
    def get_root(self):
        """Return the root node"""
        return self.root

    def insert(self, item):
        """Insert a new node"""

        # Create a new node
        new_node = Node(item)

        # Check if the root node exists
        if self.root is None:
            # Set the root to be the new node
            self.root = new_node

        # Find the correct place to insert the new node
        else:
            current = self.root
            placed = False

            # Repeat while the data has not been inserted            
            while placed == False:
                
                # Check if the new item is greater than the current node data
                if item > current.data:
                    # Check if the current node does not have a right child node
                    if current.right is None:
                        # Insert the new node to the right of the current node
                        current.right = new_node
                        placed = True
                    # Otherwise repeat with the current right node
                    else:
                        current = current.right

                # Otherwise the new item is less than or equal to the current node
                else:
                    # Check if the current node does not have a left child node
                    if current.left is None:
                        # Insert the new node to the left of the current node
                        current.left = new_node
                        placed = True
                    # Otherwise repeat with the current left node
                    else:
                        current = current.left
                        
    
    def search(self, node, search_item):
        """Recursively searches for an item in a binary search tree"""

        # Base case for recursion:
        # The recursion will stop if the search item has been found
        if search_item == node.data:
            return True

        # Check if the search item is greater than the node data
        # and there is another node to the right to check
        elif search_item > node.data and node.right is not None:
            return self.search(node.right, search_item)

        # Check if the search item is less than the node data
        # and there is another node to the left to check
        elif search_item < node.data and node.left is not None:
            return self.search(node.left, search_item)

        # Base case for recursion:
        # Otherwise the search item does not exist
        else:
            return False
            

def insert_test_data(bst):
    """"Insert test data into the binary search tree"""
    bst.insert(8)  # This will be the root node
    bst.insert(3)
    bst.insert(6)
    bst.insert(10)
    bst.insert(1)
    bst.insert(5)
    bst.insert(18)
    bst.insert(7)
    bst.insert(12)


def output_tree(node, level = 0):
    """Print the tree with the root to the left and children to the right"""

    if node is not None:
        output_tree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.data))
        output_tree(node.left, level + 1)


def main():
    """Create a binary search tree and search for an item"""

    # Instantiate a new tree object
    bst = BST()

    # Insert test data into the binary search tree
    insert_test_data(bst)

    # Get the root node
    root = bst.get_root()

    # Testing
    print("### Output the tree structure ###")
    print("The root is the left-most value and the children are to the right\n")
    output_tree(root)

    # Search for a value and return if it has been found
    item_to_find = 6
    found = bst.search(root, item_to_find)

    # Output the search result
    print(f"\nThe search item is {item_to_find}")
    
    if found == True:
        print(f"{item_to_find} was found in the binary search tree")
    else:
        print(f"{item_to_find} does not exist in the binary search tree")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
