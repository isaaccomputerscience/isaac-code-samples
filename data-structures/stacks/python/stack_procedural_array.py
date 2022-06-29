'''
Procedural implementation of stack using Python list to simulate static aray
coded by Diane
October 2020
version 1
Important - note that this pop method will override the built in list method
'''


MAX_SIZE = 10

def is_full(top):
    '''checks if stack is full'''
    if top == MAX_SIZE - 1:
        return True
    else:
        return False

def is_empty(top):
    '''checks if stack is empty'''
    if top == -1:
        return True
    else:
        return False  

def push(stack, top, data):
    '''pushes data onto top of stack and adjusts top pointer'''
    if is_full(top):
        print ('Stack is full')
    else:
        top = top + 1
        stack[top] = data
    return top      

def peek(stack, top):
    '''returns copy of item from top of stack but item stays on the stack'''
    if is_empty(top):
        print ('Stack is empty')
        peeked_item = None
    else:
        peeked_item = stack[top]
    return peeked_item

def pop(stack, top):
    '''returns item from top of stack and adjusts top pointer'''
    if is_empty(top):
        print ('Stack is empty')
        popped_item = None
    else:
        popped_item = stack[top]
        top = top - 1
    return popped_item, top


def show (stack, top):
    '''just for testing'''
    print ('------ state of stack (first is top) ------')
    while stack[top] != None:
        print (stack[top])
        top = top -1 
    print ('\n')

def test(my_stack, top):
    print ('top = pushing Diane')
    top = push(my_stack, top, 'Diane')
    show(my_stack, top)
    print ('top = pushing Eirini')
    top = push(my_stack, top, 'Eirini')
    show(my_stack, top)
    print ('Peeking - should show Eirini')
    peeked_element = peek(my_stack, top)
    print ('{} was peeked'.format(peeked_element))
    show(my_stack, top)
    print ('top = pushing Sean')
    top = push(my_stack, top, 'Sean')
    show(my_stack, top)
    print ('Popping - should remove Sean')
    popped_element, top = pop(my_stack, top)
    print ('{} removed from stack'.format(popped_element))
    show(my_stack, top)
    print ('Popping - should remove Eirini')
    popped_element, top = pop(my_stack, top)
    print ('{} removed from stack'.format(popped_element))
    show(my_stack, top)
    print ('Popping - should remove Diane')
    popped_element, top = pop(my_stack, top)
    print ('{} removed from stack'.format(popped_element))
    show(my_stack, top)
    print ('Popping - should say stack empty')
    popped_element, top = pop(my_stack, top)
    #testing max capacity
    for i in range(MAX_SIZE + 1):
        print ('trying to push item - {}'.format(i + 1))
        top = push(my_stack, top, 'test') #should eventually say stack full 
        

if __name__ == '__main__':
        my_stack = []
        top = -1
        for i in range(MAX_SIZE):
            my_stack.append(None) #to simulate static array
        test(my_stack, top)
