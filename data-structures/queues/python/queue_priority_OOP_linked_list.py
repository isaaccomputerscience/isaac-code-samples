'''
OOP implementation of priority queue
coded by Diane
QA by Alex
October 2020
version 2 - updated to add getters and setters
'''

class Node():
    '''a node in a linked list'''
    def __init__(self, item_data, item_priority):
        self.data = item_data
        self.priority = item_priority
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def get_priority(self):
        return self.priority
        
    def show(self):
        '''just for testing'''
        print ('Data is {}, priority is {}, next is {}'.format(self.data, self.priority, self.next))
    


class PriorityQueue():
    ''' a priority queue stored as a linked list '''    
    def __init__(self):
        self.front = None
        self.rear = None

    def set_front(self, new_front):
        self.front = new_front

    def get_front(self):
        return self.front

    def set_rear(self, new_rear):
        self.rear = new_rear

    def get_rear(self):
        return self.rear
    
    def is_empty(self):
        '''checks whether queue is empty'''
        if self.front == None:
            print ('Queue is empty')
            return True
        else:
            return False

    def enqueue(self, data, priority):
        new_node = Node(data, priority)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            if new_node.get_priority() > self.front.get_priority(): # new node will be new front of queue
                new_node.set_next(self.front) # don't lose the next node!
                self.front = new_node
            elif new_node.get_priority() <= self.rear.get_priority(): # new node will added to end of queue
                self.rear.set_next(new_node)
                self.rear = new_node
            else:
                current = self.front
                while(current.get_priority() >= new_node.get_priority()): #find insertion point
                    previous = current
                    current = current.get_next()
                new_node.set_next(current)
                previous.set_next(new_node)
                

    def dequeue(self):
        dequeued_item = None
        if self.is_empty(): #queue is empty
            print ('Nothing dequeued - queue is empty')
        else:
            dequeued_item = self.front.get_data()
            self.front = self.front.get_next() #change pointer to next item
        return dequeued_item
    

    def show (self):
        '''just for testing'''
        print ('------ state of queue ------')
        if self.front == None:
            print ('Queue is empty')
        else:
            print ('Head is {}:{}'.format(self.front, self.front.data))
            current_node = self.front
            current_node.show()
            while current_node.next != None:
                current_node = current_node.next
                current_node.show()
        print ('\n')

def test_enqueue(my_queue):
    print ('Adding A with priority 3')
    my_queue.enqueue('A', 3)
    my_queue.show()
    print ('Adding B with priority 2 - should be behind A')
    my_queue.enqueue('B', 2) 
    my_queue.show()
    print ('Adding C with priority 3 - should be in front of B')
    my_queue.enqueue('C', 3)
    my_queue.show()
    print ('Adding D with priority 3 - should be after C')
    my_queue.enqueue('D', 3)
    my_queue.show()
    print ('Adding E with priority 3 - should be after D')
    my_queue.enqueue('E', 3)
    my_queue.show()
    print ('Adding F with priority 1 - should be after B')
    my_queue.enqueue('F', 1) 
    my_queue.show()
    print ('Adding G with priority 4 - should be head of queue')
    my_queue.enqueue('G', 4)
    my_queue.show()
    print ('Adding H with priority 5 - should be head of queue')
    my_queue.enqueue('H', 5)
    my_queue.show()
    print ('Adding I with priority 5 - should be after H')
    my_queue.enqueue('I', 5)
    my_queue.show()

def test_dequeue(my_queue):
    print ('Dequeuing 10 items')
    for i in range (10):
        my_queue.dequeue()
        my_queue.show()


def quick_question():
    my_queue = PriorityQueue()
    my_queue.enqueue ('peas', 3)
    my_queue.enqueue ('turnips',4)
    my_queue.enqueue ('cabbage',4)
    my_queue.enqueue ('carrots',3)
    dequeued_element = my_queue.dequeue()
    print (dequeued_element)
        
            

if __name__ == '__main__':
    my_queue = PriorityQueue()
    test_enqueue(my_queue)
    test_dequeue(my_queue)
    quick_question()
