# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


MAX_SIZE = 4 # Max size of the queue


def is_empty(front, rear):
    """Check if the queue is empty"""
    
    if front > rear:
        return True
    else:
        return False


def is_full(rear):
    """Check if the queue is full"""
    
    if rear + 1 == MAX_SIZE:
        return True
    else:
        return False


def enqueue(queue, rear, data):
    """Enqueue an item"""
    
    if is_full(rear) == True:
        print(f"\nQueue is full - {data} not added")
    else:          
        rear = rear + 1
        queue[rear] = data
    return rear


def dequeue(queue, front, rear):
    """Dequeue an item"""
    
    if is_empty(front, rear) == True:
        print("\nQueue is empty - nothing to dequeue")
        dequeued_item = None
    else:
        dequeued_item = queue[front]
        front = front + 1
    return dequeued_item, front


def output_queue(queue, front, rear):
    """Output the state of the queue"""

    # Testing
    print(f"\nQueue: {queue}")
    print(f"Front: {front}")
    print(f"Rear: {rear}")

        
def main():
    """Create a queue and enqueue and dequeue items"""
    
    print("### Queue ###")

    # Initialise the queue and pointers
    queue = []
    front = 0
    rear = -1

    # Simulate a fixed size array
    for i in range(MAX_SIZE):
        queue.append(None)
    output_queue(queue, front, rear)

    # Insert test data into the queue
    rear = enqueue(queue, rear, "Julie")
    output_queue(queue, front, rear)
    
    rear = enqueue(queue, rear, "Rey")
    output_queue(queue, front, rear)
    
    rear = enqueue(queue, rear, "Habib")
    output_queue(queue, front, rear)
    
    rear = enqueue(queue, rear, "Sabrina")
    output_queue(queue, front, rear)

    # Trying to enqueue - should say queue is full
    rear = enqueue(queue, rear, "Mina")
    output_queue(queue, front, rear)

    # Dequeue all of the items
    for item in queue:
        item, front = dequeue(queue, front, rear)
        print(f"\nDequeued {item}")

    # This shouldn't enqueue Eirini since there is no implementation for
    # writing over any dequeued elements
    rear = enqueue(queue, rear, "Eirini")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
