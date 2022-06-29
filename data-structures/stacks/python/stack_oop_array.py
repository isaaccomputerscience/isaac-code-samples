'''
OOP implementation of stack using Python list to simulate static aray
coded by Diane
October 2020
version 1
Important - note that this pop method will override the built in list method
'''


class Stack():
    '''a stack stored as an array with defined maximum size'''    
    def __init__(self, max_size):
        self.contents = []
        self.max_size = max_size
        self.top = -1
        for i in range(max_size):
            self.contents.append(None)

    def push(self, data):
        '''pushes data onto top of stack and adjusts top pointer'''
        if self.top == self.max_size - 1:
            print ('Stack is full')
        else:
            self.top += 1
            self.contents [self.top] = data

    def peek(self):
        '''returns copy of item from top of stack but item stays on the stack'''
        if self.top == -1:
            print ('Stack is empty')
            peeked_item = None
        else:
            peeked_item = self.contents[self.top]
        return peeked_item

    def pop(self):
        '''returns item from top of stack and adjusts top pointer'''
        if self.top == -1:
            print ('Stack is empty')
            popped_item = None
        else:
            popped_item = self.contents[self.top]
            self.top -= 1
        return popped_item


    def show (self):
        '''just for testing'''
        print ('------ state of stack (first is top) ------')
        i = self.top
        while self.contents[i] != None:
            print (self.contents[i])
            i -= 1
        print ('\n')
        

                
        
            

if __name__ == '__main__':
    max_size = 10
    my_stack = Stack(max_size)
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
    #testing max capacity
    for i in range(max_size + 1):
        print ('trying to push item - {}'.format(i + 1))
        my_stack.push('test') #should eventually say stack full
