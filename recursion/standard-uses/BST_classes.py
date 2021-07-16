# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

# In this example, a class is defined for a Node. However, it used here as a record structure (i.e. no methods are defined)


class Node:
    """Node for a binary search tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class BST:
    """Binary search tree."""
    def __init__(self):
        self.root = None
        

    def get_root(self):
        """Returns value of root node."""
        return self.root
    

    def insert (self, data):
        """Insert new node."""
        new_node = Node(data)
        if self.root == None:  # New root node
            self.root = new_node
        else:                   
            placed = False
            current = self.root
            while placed == False:
                if current.data > data:  # Go left
                    if current.left == None:
                        current.left = new_node
                        placed = True
                    else:
                        current = current.left
                else:  # Go right
                    if current.right == None:
                        current.right = new_node
                        placed = True
                    else:
                        current = current.right                    
                    
                   
if __name__ == '__main__':
    # Just for testing
    bst = BST()
    bst.insert('fred')
    bst.insert('elaine')
    bst.insert('george')
    bst.insert('harry')     
        
