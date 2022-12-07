# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


class Node():
    """A node in a linked list"""

    # Constructor method
    def __init__(self, item_data, item_priority):
        self.data = item_data
        self.priority = item_priority
        self.next = None

    def get_data(self):
        return self.data

    def get_priority(self):
        return self.priority

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
        
    def output_node(self):
        """Testing"""
        next_data = None
        if (self.next != None):
            next_data = self.next.data
        print(f"Data: {self.data}, priority: {self.priority}, next: {next_data}")    


class PriorityQueue():
    """A priority queue stored as a linked list"""
    
    # Constructor method
    def __init__(self):
        self.front = None
        self.rear = None

    def get_front(self):
        return self.front

    def set_front(self, new_front):
        self.front = new_front

    def get_rear(self):
        return self.rear

    def set_rear(self, new_rear):
        self.rear = new_rear
    
    def is_empty(self):
        """Check if the queue is empty"""
        if self.front == None:
            return True
        else:
            return False

    def enqueue(self, data, priority):
        """Enqueue an item based on the priority"""
    
        new_node = Node(data, priority)

        # Check if the queue is empty
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            # Check if new node should be the new front of queue
            if new_node.get_priority() > self.front.get_priority():
                # Change the current head pointer
                new_node.set_next(self.front)
                self.front = new_node
            # Check if new node should be added to the end of the queue
            elif new_node.get_priority() <= self.rear.get_priority():
                self.rear.set_next(new_node)
                self.rear = new_node
            else:
                # Find the insertion point
                current = self.front
                while(current.get_priority() >= new_node.get_priority()):
                    previous = current
                    current = current.get_next()
                new_node.set_next(current)
                previous.set_next(new_node)
                

    def dequeue(self):
        """Dequeue an item"""
        
        dequeued_item = None
        
        if self.is_empty():
            print("\nQueue is empty - nothing to dequeue")
        else:
             # Get data and change pointer to next item
            dequeued_item = self.front.get_data()
            self.front = self.front.get_next()
            
        return dequeued_item


    def output_queue(self):
        """Output the state of the queue"""

        # Testing
        if self.front != None:
            print("------ State of the queue ------")
            print("Head ", end="")
            current_node = self.front
            current_node.output_node()
            while current_node.get_next() != None:
                current_node = current_node.get_next()
                current_node.output_node()
            print()


def test_enqueue(my_queue):
    print("Adding A with priority 3")
    my_queue.enqueue("A", 3)
    my_queue.output_queue()
    
    print("Adding B with priority 2 - should be behind A")
    my_queue.enqueue("B", 2) 
    my_queue.output_queue()
    
    print("Adding C with priority 3 - should be in front of B")
    my_queue.enqueue("C", 3)
    my_queue.output_queue()
    
    print("Adding D with priority 3 - should be after C")
    my_queue.enqueue("D", 3)
    my_queue.output_queue()
    
    print("Adding E with priority 3 - should be after D")
    my_queue.enqueue("E", 3)
    my_queue.output_queue()
    
    print("Adding F with priority 1 - should be after B")
    my_queue.enqueue("F", 1) 
    my_queue.output_queue()
    
    print("Adding G with priority 4 - should be head of queue")
    my_queue.enqueue("G", 4)
    my_queue.output_queue()
    
    print("Adding H with priority 5 - should be head of queue")
    my_queue.enqueue("H", 5)
    my_queue.output_queue()
    
    print("Adding I with priority 5 - should be after H")
    my_queue.enqueue("I", 5)
    my_queue.output_queue()


def test_dequeue(my_queue):
    print("\n------ Dequeuing 10 items ------\n")
    for i in range(10):
        my_queue.dequeue()
        my_queue.output_queue()

        
def main():
    """Create a priority queue and enqueue and dequeue items"""
    
    print("### Priority queue (OOP) ###\n")

    # Initialise the queue
    my_queue = PriorityQueue()

    # Insert test data into the queue
    test_enqueue(my_queue)
    
    # Remove test data from the queue
    test_dequeue(my_queue)

 
# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
