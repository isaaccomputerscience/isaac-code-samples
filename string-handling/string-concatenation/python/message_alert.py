# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def message_alert(new_messages):
    """Example of type conversion for string concatenation"""    
    print("You have " + str(new_messages) + " new messages")
    

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    messages = 5
    message_alert(messages)
