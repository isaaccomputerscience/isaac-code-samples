'''
code for ICS linked list
simulates a record strcture and uses procedural paradigm
written for platform
written by Di
written November 2020

uses an extra class for LinkedList as best way to get close to pseudocode

'''

class NodeRecord():
    '''node in a linked list'''
    def __init__ (self):
        self.data = None
        self.next = None

class LinkedList():
    '''not used in pseudocode'''
    def __init__(self):
        self.head = None    


def insert_at_front(mylist, data):
    '''replace mylist.head with head in pseudocode'''
    new_node = NodeRecord()
    new_node.data = data
    new_node.next = mylist.head
    mylist.head = new_node


def traverse(my_list):
    '''replace mylist.head with head in pseudocode'''
    current = my_list.head
    while current != None:
        print ('Item is {}'.format(current.data))
        current = current.next
    print ('\n')

def insert_in_order(my_list, data):
    '''replace mylist.head with head in pseudocode'''
    new_node = NodeRecord()
    new_node.data = data
    current = my_list.head
    if current == None:  # no nodes in list
        my_list.head = new_node  
    elif current.data >= new_node.data: # special case
        new_node.next = my_list.head # change pointer
        my_list.head = new_node #new node is head of list
    else :   
        # find the point of insertion          
        while(current.next != None and current.next.data < new_node.data): 
            current = current.next            
        new_node.next = current.next # change pointer
        current.next = new_node #set pointer

def delete (my_list, data):
    '''replace mylist.head with head in pseudocode'''
    '''this assumes that the node does exist in the list'''
    current = my_list.head
    if current.data == data:
        my_list.head = current.next
    else:
        while current.next.data != data: 
            current = current.next
        current.next = current.next.next #swap pointers
    


def test1(my_list):
    print ('Testing addding to front of list')
    insert_at_front(my_list, 'diane')
    insert_at_front(my_list, 'george')
    insert_at_front(my_list, 'fred')
    insert_at_front(my_list, 'julie')
    #print (my_list.head.next.next.next.data) #woohoo!
    print ('List should be julie, fred, george, diane')
    traverse(my_list)

def test2(my_list):    
    print ('Testing inserting in order')
    insert_in_order(my_list, 'gary') #in middle
    traverse(my_list)
    insert_in_order(my_list, 'abe') #at start
    traverse(my_list)
    insert_in_order(my_list, 'zeb') #at end
    traverse(my_list)
    insert_in_order(my_list, 'jules') #in middle
    traverse(my_list)
    print ('Adding in order to empty list')
    my_list = LinkedList() #creates new empty list
    insert_in_order(my_list, 'abe') #empty list
    traverse(my_list)

def test3 (my_list):
    print ('Testing delete function')
    print ('Making list to delete from')
    my_list = LinkedList()
    test1(my_list)    
    print ('deleting george from middle of list')
    delete (my_list, 'george') #delete from middle
    traverse(my_list)
    print ('deleting diane from end of list')
    delete (my_list, 'diane') #delete from end
    traverse(my_list)
    print ('deleting julie from front of list')
    delete (my_list, 'julie') #delete from front
    traverse(my_list)
    print ('deleting single node - fred')
    delete (my_list, 'fred') #delete last node
    traverse(my_list)

    

if __name__ == '__main__':
    my_list = LinkedList() #creates new empty list
    test1(my_list)
    my_list = LinkedList() #creates new empty list
    test2(my_list)
    test3(my_list)
    
