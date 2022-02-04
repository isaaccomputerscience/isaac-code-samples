# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

from BST_classes import Node, BST
                 
def bst_search(node, search_item):
    """Recursively searches a binary search tree. Returns a Boolean."""
    if search_item == node.data: 
        return True
    elif search_item > node.data and node.right != None:
        return bst_search(node.right, search_item)
    elif search_item < node.data and node.left != None:
        return bst_search(node.left, search_item)
    return False
  

def insert_test_data(bst):
    """Inserts some test data into tree."""
    bst.insert('fred')
    bst.insert('elaine')
    bst.insert('george')
    bst.insert('harry')

def test(bst):
    """Carries out some basic tests."""
    start_node = bst.get_root()  # Start search at root
    if bst_search(start_node, "aaron") != False:
        print("aaron - test failed")
    if bst_search(start_node, "harry") != True:
        print("harry - test failed")
    if bst_search(start_node, "zac") != False:
        print("zac - test failed")
    print("Tests complete")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
      
if __name__ == '__main__':
    my_bst = BST()
    insert_test_data(my_bst)  # Create some test data
    test(my_bst)  # Run test script
