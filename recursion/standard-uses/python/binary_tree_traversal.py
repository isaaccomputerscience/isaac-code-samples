# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

from BST_classes import BST, Node  # Uses a binary search tree

def traverse_in_order(node):
    """In-order binary tree traversal"""
    if node != None:
        traverse_in_order(node.left)
        print(node.data)
        traverse_in_order(node.right)


def insert_test_data(bst):
    """Inserts some test data into tree"""
    bst.insert('Zac')
    bst.insert('Lucy')
    bst.insert('Anil')
    bst.insert('Boris')
 
       
# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':
    my_tree = BST()
    insert_test_data(my_tree)  # Create some test data
    start = my_tree.get_root()  # Get start node
    traverse_in_order(start) 
