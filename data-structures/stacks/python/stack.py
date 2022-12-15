# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


MAX_SIZE = 4 # Max size of the stack


def is_empty(top):
    """Check if the stack is empty"""
    
    if top == -1:
        return True
    else:
        return False  


def is_full(top):
    """Check if the stack is full"""
    
    if top == MAX_SIZE - 1:
        return True
    else:
        return False


def push(stack, top, data):
    """Push data onto the top of the stack"""
    
    if is_full(top) == True:
        print(f"Stack is full - {data} not added")
    else:
        top = top + 1
        stack[top] = data
    return top      


def peek(stack, top):
    """Return a copy of the item from the top of stack without removing it"""
    
    if is_empty(top):
        print("Stack is empty - nothing to peek")
        peeked_item = None
    else:
        peeked_item = stack[top]
    return peeked_item


def pop(stack, top):
    """Return the item from the top of stack and remove it from the stack"""
    
    if is_empty(top) == True:
        print("\nStack is empty - nothing to pop")
        popped_item = None
    else:
        popped_item = stack[top]
        stack[top] = None # Testing
        top = top - 1
        
    return popped_item, top


def output_stack(stack, top):
    """Output the state of the stack"""
    
    print("\n------ State of the stack (first item is the top) ------")
    for i in range(MAX_SIZE - 1, -1, -1):
        print(stack[i])
    print(f"Top pointer: {top}")


def main():
    """Create a stack and push, pop and peek items"""
    
    print("### Stack ###")

    # Initialise the stack and pointers
    stack = []
    top = -1

    # Simulate a fixed size array
    for i in range(MAX_SIZE):
        stack.append(None)
    output_stack(stack, top)

    # Insert test data onto the stack
    top = push(stack, top, "Julie")
    output_stack(stack, top)
    
    top = push(stack, top, "Rey")
    output_stack(stack, top)
    
    top = push(stack, top, "Habib")
    output_stack(stack, top)
    
    top = push(stack, top, "Sabrina")
    output_stack(stack, top)

    # Trying to push - should say stack is full
    top = push(stack, top, "Mina")
    output_stack(stack, top)

    # Peek the top item of the stack
    peeked_item = peek(stack, top)
    print(f"\nPeeked top of the stack: {peeked_item}", end="")
    output_stack(stack, top)

    # Pop all of the items
    for item in stack:
        item, top = pop(stack, top)
        print(f"\nPopped {item}", end="")
        output_stack(stack, top)

    # Try to pop - should say stack is empty
    item, top = pop(stack, top)
    print(f"Popped {item}", end="")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
