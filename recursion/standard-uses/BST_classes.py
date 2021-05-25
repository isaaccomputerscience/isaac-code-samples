# in this example, a class is defined for a Node
# however, it used as a Record (no methods are defined)


class Node:
    '''node in a binary search tree'''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class BST:
    '''binary search tree'''
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert (self, data):
        '''insert new node'''
        new_node = Node(data)
        if self.root == None: # new root node
            self.root = new_node
        else:                   
            placed = False
            current = self.root
            while placed == False:
                if current.data > data:#go left
                    if current.left == None:
                        current.left = new_node
                        placed = True
                    else:
                        current = current.left
                else: #go right
                    if current.right == None:
                        current.right = new_node
                        placed = True
                    else:
                        current = current.right                    
                    
                   
if __name__ == '__main__':
    #just for testing
    bst = BST()
    bst.insert('fred')
    bst.insert('elaine')
    bst.insert('george')
    bst.insert('harry')     
        
