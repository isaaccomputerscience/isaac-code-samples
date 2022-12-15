# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


class Node():
    """A node in a linked list"""

    # Constructor method
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
        
    def output_node(self):
        """Testing"""
        next_data = None
        if (self.next != None):
            next_data = self.next.data
        print(f"Data: {self.data}, next: {next_data}") 


class Stack():
    """A stack implemented as a linked list"""
    
    # Constructor method
    def __init__(self):
        self.top = None

    
    def is_empty(self):
        """Check if the stack is empty"""
        if self.top == None:
            return True
        else:
            return False


    def push(self, data):
        """Push a new item onto the stack"""
        
        new_node = Node(data)
        
        # Check if the stack is NOT empty
        if not self.is_empty():
             # Point to the next element in the list
            new_node.set_next(self.top)

        # Set top to point to the new node
        self.top = new_node         


    def pop(self):
        """Pop the item from the top of the stack"""
        
        popped_data = None
        
        if self.is_empty():
            print("\nStack is empty - nothing to pop")
        else:
             # Get data and change pointer to next item
            popped_data = self.top.get_data()
            self.top = self.top.get_next()
            
        return popped_data


    def peek(self):
        """Peek the item at the top of the stack"""
        
        peeked_data = None
        
        if self.top == None:
            print("\nStack is empty - nothing to peek")
        else:
             # Get data from the top of the stack
            peeked_data = self.top.get_data()

        return peeked_data


    def output_stack(self):
        """Output the state of the stack"""

        # Testing
        if self.top != None:
            print("------ State of the stack (first item is the top) ------")
            current_node = self.top
            current_node.output_node()
            while current_node.get_next() != None:
                current_node = current_node.get_next()
                current_node.output_node()
            print()
      


        
def main():
    """Create a stack and push, pop and peek items"""
    
    print("### Stack (OOP) ###\n")

    # Initialise the stack
    my_stack = Stack()

    # Insert test data onto the stack
    my_stack.push("Julie")
    my_stack.output_stack()
    
    my_stack.push("Rey")
    my_stack.output_stack()

    # Peek the top item of the stack
    peeked_item = my_stack.peek()
    print(f"Peeked top of the stack: {peeked_item}")
    my_stack.output_stack()
    
    # Insert more test data onto the stack
    my_stack.push("Habib")
    my_stack.output_stack()
    
    my_stack.push("Sabrina")
    my_stack.output_stack()

    # Pop the top item from the stack
    popped_item = my_stack.pop()
    print(f"Popped {popped_item}")
    my_stack.output_stack()
    
    # Insert more test data onto the stack
    my_stack.push("Mina")
    my_stack.output_stack()
    
    my_stack.push("Eirini")
    my_stack.output_stack()

 
# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
