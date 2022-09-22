# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


class NodeRecord():
    """Use a class to represent a node as a record in the linked list"""
    
    def __init__ (self):
        self.data = None
        self.next = None


class LinkedList():
    """Use a class to represent the linked list"""
    
    def __init__(self):
        self.head = None # Initialise to None as the linked list is empty


def insert_at_front(my_list, data):
    """Insert a node to the front of the list"""

    # Create a new node
    new_node = NodeRecord()
    new_node.data = data

    # Update the pointers so the new node is the head
    new_node.next = my_list.head
    my_list.head = new_node

def insert_in_order(my_list, data):
    """Insert a node into the correct position in an ordered list"""
    
    # Create a new node
    new_node = NodeRecord()
    new_node.data = data

    # Start at the head of the list
    current = my_list.head

    # Check if there are no nodes in the list
    if current is None:
        my_list.head = new_node

    # Check if the new node data is less than the head data
    elif new_node.data < current.data:
        # Set the new node as the head of the list
        new_node.next = my_list.head
        my_list.head = new_node

    # Otherwise find where the new node should be positioned
    else:
        # Repeat until the point of insertion is found
        while (current.next is not None
              and current.next.data < new_node.data):
            # Get the next node
            current = current.next
            
        # Update the pointers of the new and current nodes
        new_node.next = current.next
        current.next = new_node

def traverse(my_list):
    """Traverse the list and output the data from each node"""

    # Set the current node as the head
    current = my_list.head

    # Repeat until there are no more linked nodes
    while current is not None:
        print(f"{current.data}")
        current = current.next

def delete(my_list, data):
    """Delete a node. This assumes that the node does exist in the list"""

    # Start at the head of the list
    current = my_list.head

    # Check if the head node is to be deleted
    if current.data == data:
        # Update the head pointer
        my_list.head = current.next
    else:
        # Repeat until the node has been found
        while current.next.data != data:
            # Change the current node to be the next node
            current = current.next

        # Set the pointer to be the next node's pointer
        current.next = current.next.next


def insert_test_data(my_list):
    """"Insert test data into the linked list"""
    
    insert_in_order(my_list, "Julie")
    insert_in_order(my_list, "Rey")
    insert_in_order(my_list, "Habib")
    insert_in_order(my_list, "Sabrina")
    insert_in_order(my_list, "Mina")


def main():
    """Create a linked list and insert, delete and traverse the list"""
    
    print("### Linked list (Record) ###")

    # Instantiate an empty linked list object
    my_list = LinkedList()

    # Insert test data into the linked list
    print("\nInsert test data into the linked list in order:")
    insert_test_data(my_list)
    traverse(my_list)

    # Testing - insert at front
    print("\nInsert a node to the front of the list:")
    insert_at_front(my_list, "Albus")
    traverse(my_list)

    # Testing - insert in order
    print("\nInsert a node to the end of the list:")
    insert_in_order(my_list, "Zeb")
    traverse(my_list)
    
    # Testing - delete a node
    print("\nDelete a node from the list:")
    delete(my_list, "Sabrina")
    traverse(my_list)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
