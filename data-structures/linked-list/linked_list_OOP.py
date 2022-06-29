'''
code for ICS linked list
written for platform
written by Di
written November 2020

'''


class Node():
    '''node in a linked list'''   
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
    '''the linked list'''
    def __init__(self):
        self.head = None #empty list

    def insert_at_front(self, data):
        '''insert node at front of list'''
        new_node = Node(data) #example of composition
        if self.head == None:
            self.head = new_node
        else:
            new_node.set_next(self.head)            
            self.head = new_node

    def traverse(self):
        '''traverse list and output data from node'''
        current = self.head
        while current != None:
            print ('Item is {}'.format(current.get_data()))
            current = current.get_next()
        print ('\n')
            
    def insert_in_order(self, data):
        ''' insert node into an ordered list'''
        new_node = Node(data)
        current = self.head
        if current == None:  # no nodes in list
            self.head = new_node  
        elif current.get_data() >= new_node.get_data(): # special case
            new_node.set_next(self.head) # change pointer
            self.head = new_node #new node is head of list
        else :   
            # find the point of insertion          
            while(current.get_next() != None and current.get_next().get_data() < new_node.get_data()): 
                current = current.get_next()            
            new_node.set_next(current.get_next()) # change pointer
            current.set_next(new_node) #set pointer

    def delete (self, data):
        '''this assumes that the node does exist in the list'''
        current = self.head
        if current.get_data() == data: #deleting item at head of list
            self.head = current.get_next()
        else:
            while current.get_next().get_data() != data: 
                current = current.get_next()
            current.set_next(current.get_next().get_next()) #swap pointers
        
def test1(my_list):
    print ('Testing addding to front of list')
    my_list.insert_at_front('julie')
    my_list.insert_at_front('george')
    my_list.insert_at_front('fred')
    my_list.insert_at_front('diane')
    my_list.traverse()

def test2(my_list):
    print ('Testing inserting in order with empty list')
    my_list = LinkedList() #creates new empty list
    my_list.insert_in_order('abe')
    my_list.traverse()

def test3(my_list):    
    print ('Testing inserting in order')
    my_list.insert_in_order('gary') #in middle
    my_list.traverse()
    my_list.insert_in_order('abe') #at start
    my_list.traverse()
    my_list.insert_in_order('zeb') #at end
    my_list.traverse()

def test4(my_list):
    print ('Deleting node at head of list')
    my_list.delete('abe')
    my_list.traverse()
    print ('Deleting node at end of list')
    my_list.delete('zeb')
    my_list.traverse()
    print ('Deleting node in middle of list')
    my_list.delete('gary')
    my_list.traverse()
 

if __name__ == '__main__':
    my_list = LinkedList() #creates new empty list
    test1(my_list)
    test2(my_list)
    test3(my_list)
    test4(my_list)
    
    
