'''
OOP implementation of stack using linked list
coded by Diane
October 2020
version 1

note that this version adds new_node to the front of the list
as this is more efficient
'''



class Node():
    '''a node in a linked list'''
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    

    def show(self):
        '''just for testing'''
        print ('Node is {}, next is {}'.format(self.data, self.next))
    


class Stack():
    '''a stack implemented as a linked list'''    
    def __init__(self):
        self.top = None # points to first element of the linked list

    def push(self, data):
        '''pushes new element onto stack'''
        new_node = Node(data)
        if self.top != None: # stack is not empty
            new_node.set_next(self.top) # point to next element in the list
        self.top = new_node # set top to point to new node          

    def pop(self):        
        '''pops element from stack'''
        if self.top == None: # stack is empty
            print ('Stack is empty')
            popped_data = None
        else:
            popped_data = self.top.get_data() # get data from node at top of stack
            self.top = self.top.get_next() # change pointer to next item
        return popped_data

    def peek(self):
        '''peeks at element at top of stack'''
        if self.top == None: # stack is empty
            print ('Stack is empty')
            peeked_data = None
        else:
            peeked_data = self.top.get_data() # get data from node at top of stack
        return peeked_data
      

    def show (self):
        '''this method is just for testing'''
        print ('------ state of stack (first is top) ------')
        if self.top == None:
            print ('Stack is empty')
        else:
            current_node = self.top
            print (current_node.get_data())
            while current_node.get_next() != None:
                current_node = current_node.get_next()
                print (current_node.get_data())
        print ('\n')
                
        
            

if __name__ == '__main__':
    my_stack = Stack()
    print ('Pushing Diane')
    my_stack.push('Diane')
    my_stack.show()
    print ('Pushing Eirini')
    my_stack.push('Eirini')
    my_stack.show()
    print ('Peeking - should show Eirini')
    peeked_element = my_stack.peek()
    print ('{} was peeked'.format(peeked_element))
    my_stack.show()
    print ('Pushing Sean')
    my_stack.push('Sean')
    my_stack.show()
    print ('Popping - should remove Sean')
    popped_element = my_stack.pop()
    print ('{} removed from stack'.format(popped_element))
    my_stack.show()
    print ('Popping - should remove Eirini')
    popped_element = my_stack.pop()
    print ('{} removed from stack'.format(popped_element))
    my_stack.show()
    print ('Popping - should remove Diane')
    popped_element = my_stack.pop()
    print ('{} removed from stack'.format(popped_element))
    my_stack.show()
    print ('Popping - should say stack empty')
    popped_element = my_stack.pop()
