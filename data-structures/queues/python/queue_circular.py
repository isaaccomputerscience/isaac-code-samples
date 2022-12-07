# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


MAX_SIZE = 4 # Max size of the queue


def is_empty(front):
    """Check if the queue is empty"""
    
    if front == -1:
        return True
    else:
        return False


def is_full(front, rear):
    """Check if the queue is full"""
    
    if (rear + 1) % MAX_SIZE == front:
        return True
    else:
        return False

    
def enqueue(queue, front, rear, data):
    """Enqueue an item"""
    
    if is_full(front, rear) == True:
        print(f"\nQueue is full - {data} not added")
    else:
        rear = (rear + 1) % MAX_SIZE
        queue[rear] = data
        if front == -1: # First item to be queued
            front = 0
    return front, rear


def dequeue(queue, front, rear):
    """Dequeue an item"""
    
    if is_empty(front) == True:
        print("\nQueue is empty - nothing to dequeue")
        dequeued_item = None
    else:
        dequeued_item = queue[front]
        queue[front] = None # Testing
        # Check if the queue is empty
        if front == rear:
            front = -1
            rear = -1       
        else:
            front = (front + 1) % MAX_SIZE
            
    return dequeued_item, front, rear


def output_queue(queue, front, rear):
    """Output the state of the queue"""

    # Testing
    print(f"\nQueue: {queue}")
    print(f"Front: {front}")
    print(f"Rear: {rear}")

        
def main():
    """Create a circular queue and enqueue and dequeue items"""
    
    print("### Circular queue ###")

    # Initialise the queue and pointers
    queue = []
    front = -1
    rear = -1

    # Simulate a fixed size array
    for i in range(MAX_SIZE):
        queue.append(None)
    output_queue(queue, front, rear)

    # Insert test data into the queue
    front, rear = enqueue(queue, front, rear, "Julie")
    output_queue(queue, front, rear)
    
    front, rear = enqueue(queue, front, rear, "Rey")
    output_queue(queue, front, rear)
    
    front, rear = enqueue(queue, front, rear, "Habib")
    output_queue(queue, front, rear)
    
    front, rear = enqueue(queue, front, rear, "Sabrina")
    output_queue(queue, front, rear)

    # Trying to enqueue - should say queue is full
    front, rear = enqueue(queue, front, rear, "Mina")
    output_queue(queue, front, rear)

    # Dequeue some of the items
    item, front, rear = dequeue(queue, front, rear)
    print(f"\nDequeued {item}")
    output_queue(queue, front, rear)
    
    item, front, rear = dequeue(queue, front, rear)
    print(f"\nDequeued {item}")
    output_queue(queue, front, rear)
    
    # Insert data into the empty slots in the queue
    front, rear = enqueue(queue, front, rear, "Eirini")
    output_queue(queue, front, rear)
    
    front, rear = enqueue(queue, front, rear, "Diane")
    output_queue(queue, front, rear)

    # Trying to enqueue - should say queue is full
    front, rear = enqueue(queue, front, rear, "Fergus")
    output_queue(queue, front, rear)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
