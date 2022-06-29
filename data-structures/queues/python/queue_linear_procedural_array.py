'''
Procedural implementation of linear queue
Uses list with maximum size to simulate a static array
coded by Diane
QA by Alex
February 2021
'''

MAX_SIZE = 4

def is_empty(front, rear):
    '''checks if queue is empty'''
    if front > rear:
        return True
    else:
        return False

def is_full(rear):
    '''checks if queue is full'''
    if rear + 1 == MAX_SIZE:
        return True
    else:
        return False

def enqueue(queue, rear, data):
    '''enqueues item'''
    if is_full(rear) == True:
        print ('Queue is full')
    else:          
        rear = rear + 1
        queue[rear] = data
    return rear

def dequeue(queue, front, rear):
    '''dequeues item'''
    if is_empty(front, rear) == True:
        print ('Queue is empty')
        dequeued_item = None
    else:
        dequeued_item = queue[front]
        front = front + 1
    return dequeued_item, front     


def show(queue, front, rear):
    '''just for testing'''
    print ('------ state of queue -----')
    print (queue)
    print ('Front is {}, rear is {}'.format(front,rear))
    print ('\n')

def test(queue, front, rear):
    print ('Trying to dequeue from empty queue - should say empty')
    item, front = dequeue(queue, front, rear)
    print ('Trying to enqueue Diane - should write into slot 0')
    rear = enqueue(queue, rear, 'Diane')
    show(queue, front, rear)
    print ('Trying to enqueue Eirini - should write into slot 1')
    rear = enqueue(queue, rear, 'Eirini')
    show(queue, front, rear)
    print ('Trying to enqueue Sean - should write into slot 2')
    rear = enqueue(queue, rear, 'Sean')
    show(queue, front, rear)
    print ('Trying to enqueue Fergus - should write into slot 3')
    rear = enqueue(queue, rear, 'Fergus')
    show(queue, front, rear)
    print ('Trying to enqueue Duncan - should say queue is full')
    rear = enqueue(queue, rear, 'Duncan')
    show(queue, front, rear)
    print ('Trying to dequeue - should remove Diane')
    item, front = dequeue(queue, front, rear)
    show(queue, front, rear)
    print ('Trying to dequeue - should remove Eirini')
    item, front = dequeue(queue, front, rear)
    show(queue, front, rear)
    print ('Trying to dequeue - should remove Sean')
    item, front = dequeue(queue, front, rear)
    show(queue, front, rear)
    print ('Trying to enqueue Sandra - should say full')
    rear = enqueue(queue, rear, 'Sandra') 
    show(queue, front, rear)
    print ('Trying to dequeue - should remove Fergus - queue is empty')
    item, front = dequeue(queue, front, rear)
    show(queue, front, rear)
    print ('Trying to dequeue - should say queue is empty')
    item, front = dequeue(queue, front, rear)
    show(queue, front, rear)
    # This shouldn't enqueue Bert since there is no implementation for
    # writing over any dequeued elements
    print ('Trying to enqueue Bert - should say queue is full')
    rear = enqueue(queue, rear, 'Bert')
    show(queue, front, rear)
        
def main():
    queue = []
    front = 0
    rear = -1
    for i in range(MAX_SIZE):
        queue.append(None) #do this to simulate fixed size array
    test(queue, front, rear)

if __name__ == '__main__':
    main()
