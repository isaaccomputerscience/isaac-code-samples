# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def hash_string(hash_key, number_of_slots):
    """Produce a hash value from a string using the ASCII values"""

    # Initialise total
    total = 0

    # Repeat for every character in the hash key
    for i in range(len(hash_key)):
        # Add the character's ASCII value to the total
        ascii_code = ord(hash_key[i])
        total = total + ascii_code
        
    # Generate the hash value using the modulo operator
    hash_value = total % number_of_slots
    
    # Return the hash value
    return hash_value


def main():
    """Test the hashing function"""

    # Generate a hash value from a string hash key
    key = "A5RD"
    slots = 97
    value = hash_string(key, slots)
    print(f"Hash value for {key} is {value}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
