from BST_classes import BST, Node # Uses a binary search tree

def traverse_in_order(node):
    ''' In-order binary tree traversal '''
    if node != None:
        traverse_in_order(node.left)
        print (node.data)
        traverse_in_order(node.right)


def test_data(bst):
    ''' Inserts some test data into tree '''
    bst.insert('Zac')
    bst.insert('Lucy')
    bst.insert('Anil')
    bst.insert('Boris')
 
       
if __name__ == '__main__':
    my_tree = BST()
    test_data(my_tree) # Create some test data
    start = my_tree.get_root() # Get start node
    traverse_in_order(start) 
