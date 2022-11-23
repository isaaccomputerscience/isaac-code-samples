# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


class Node():
    """A class for a node in the linked list"""
    
    def __init__(self, given_data):
        self.data = given_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList():
    """A class for the linked list"""
    
    def __init__(self):
        """Constructor method"""
        self.head = None # Initialise to None as the linked list is empty

    def insert_at_front(self, data):
        """Insert a node to the front of the list"""

        # Create a new node
        new_node = Node(data)

        # Check if the head node exists
        if self.head is None:
            self.head = new_node
        else:
            # Update the pointers so the new node is the head
            new_node.set_next(self.head)            
            self.head = new_node
            
    def insert_in_order(self, data):
        """Insert a node into the correct position in an ordered list"""

        # Create a new node
        new_node = Node(data)

        # Start at the head of the list
        current = self.head
        
        # Check if there are no nodes in the list
        if current is None:
            self.head = new_node

        # Check if the new node data is before the head data
        elif new_node.get_data() < current.get_data():
            # Set the new node as the head of the list
            new_node.set_next(self.head)
            self.head = new_node

        # Otherwise find where the new node should be positioned
        else:
            # Repeat until the point of insertion is found
            while (current.get_next() is not None
                  and current.get_next().get_data() < new_node.get_data()):
                # Get the next node
                current = current.get_next()

            # Update the pointers of the new and current nodes
            new_node.set_next(current.get_next())
            current.set_next(new_node)

    def traverse(self):
        """Traverse the list and output the data from each node"""
        
        # Set the current node as the head
        current = self.head

        # Repeat until there are no more linked nodes
        while current is not None:
            print(current.get_data())
            current = current.get_next()

    def delete(self, data):
        """Delete a node. This assumes that the node does exist in the list"""
        
        # Start at the head of the list
        current = self.head

        # Check if the head node is to be deleted
        if current.get_data() == data:
            # Update the head pointer
            self.head = current.get_next()
        else:
            # Repeat until the node has been found
            while current.get_next().get_data() != data:
                # Change the current node to be the next node
                current = current.get_next()

            # Set the pointer to be the next node's pointer
            current.set_next(current.get_next().get_next())
            

def insert_test_data(my_list):
    """"Insert test data into the linked list"""
    
    my_list.insert_in_order("Julie")
    my_list.insert_in_order("Rey")
    my_list.insert_in_order("Habib")
    my_list.insert_in_order("Sabrina")
    my_list.insert_in_order("Mina")


def main():
    """Create a linked list and insert, delete and traverse the list"""
    
    print("### Linked list (OOP) ###")

    # Instantiate an empty linked list object
    my_list = LinkedList()

    # Insert test data into the linked list
    print("\nInsert test data into the linked list in order:")
    insert_test_data(my_list)
    my_list.traverse()

    # Testing - insert at front
    print("\nInsert a node to the front of the list:")
    my_list.insert_at_front("Albus")
    my_list.traverse()

    # Testing - insert in order
    print("\nInsert a node to the end of the list:")
    my_list.insert_in_order("Zeb")
    my_list.traverse()
    
    # Testing - delete a node
    print("\nDelete a node from the list:")
    my_list.delete("Sabrina")
    my_list.traverse()
 

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
