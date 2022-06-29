'''
Procedural implementation of circular queue
Uses list with maximum size to simulate a static array
coded by Diane
QA by Alex
October 2020
version 1
'''

MAX_SIZE = 4

def is_empty(front):
    '''checks if queue is empty'''
    if front == -1:
        return True
    else:
        return False


def is_full(front, rear):
    '''checks if queue is full'''
    if (rear + 1) % MAX_SIZE == front:
        return True
    else:
        return False
    
def enqueue(queue, front, rear, data):
    '''enqueues item'''
    if is_full(front, rear) == True:
        print ('The queue is full')
    else:        
        rear = (rear + 1) % MAX_SIZE
        queue[rear] = data
        if front == -1: #adding first item
            front = 0
    return front, rear


def dequeue(queue, front, rear):
    '''dequeues item'''
    if is_empty(front) == True:
        print ('The queue is empty')
        dequeued_item = None
    else:
        dequeued_item = queue[front]
        if front == rear: #nothing left in queue
            front = -1
            rear = -1       
        else:
            front = (front + 1) % MAX_SIZE
    return dequeued_item, front, rear     

def show(queue, front, rear):
    '''just for testing'''
    print ('------ state of queue -----')
    print (queue)
    print ('Front is {}, rear is {}'.format(front,rear))
    print ('\n')


def test(queue, front, rear):
    print ('trying to dequeue from empty queue - should say empty')
    item, front, rear = dequeue(queue, front, rear)
    print ('Trying to enqueue Diane - should write into slot 0')
    front, rear = enqueue(queue, front, rear, 'Diane')
    show(queue, front, rear)
    print ('Trying to enqueue Eirini - should write into slot 1')
    front, rear = enqueue(queue, front, rear, 'Eirini')
    show(queue, front, rear)
    print ('Trying to enqueue Sean - should write into slot 2')
    front, rear = enqueue(queue, front, rear, 'Sean')
    show(queue, front, rear)
    print ('Trying to enqueue Fergus - should write into slot 3')
    front, rear = enqueue(queue, front, rear, 'Fergus')
    show(queue, front, rear)
    print ('Trying to enqueue Duncan - should say queue is full')
    front, rear = enqueue(queue, front, rear, 'Duncan')
    show(queue, front, rear)
    print ('Trying to dequeue - should remove Diane')
    item, front, rear = dequeue(queue, front, rear)
    show(queue, front, rear)
    print ('Trying to dequeue - should remove Eirini')
    item, front, rear = dequeue(queue, front, rear)
    show(queue, front, rear)
    print ('Trying to dequeue - should remove Sean')
    item, front, rear = dequeue(queue, front, rear)
    show(queue, front, rear)
    print ('Trying to enqueue Sandra - should write into slot 0')
    front, rear = enqueue(queue, front, rear, 'Sandra') 
    show(queue, front, rear)
    print ('Trying to dequeue - should remove Fergus')
    item, front, rear = dequeue(queue, front, rear)
    show(queue, front, rear)
    print ('Trying to dequeue - should remove Sandra')
    item, front, rear = dequeue(queue, front, rear)
    show(queue, front, rear)
    print ('Trying to dequeue - should say queue is empty')
    item, front, rear = dequeue(queue, front, rear)
    show(queue, front, rear)
    print ('Trying to enqueue Bert - should write into slot 0')
    front, rear = enqueue(queue, front, rear, 'Bert')
    show(queue, front, rear)
    print ('Trying to enqueue Lily - should write into slot 1')
    front, rear = enqueue(queue, front, rear, 'Lily')
    show(queue, front, rear)
        
def main():
    queue = []
    front = -1
    rear = -1
    for i in range(MAX_SIZE):
        queue.append(None) #do this to simulate fixed size array
    test(queue, front, rear)

if __name__ == '__main__':
    main()
