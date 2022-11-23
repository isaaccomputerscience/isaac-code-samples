# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def hash_integer(hash_key, number_of_slots):
    """Produce a hash value from an integer"""

    # Generate the hash value using the modulo operator
    hash_value = hash_key % number_of_slots

    # Return the hash value
    return hash_value


def main():
    """Test the hashing function"""

    # Generate a hash value from an integer hash key
    key = 12345
    slots = 97
    value = hash_integer(key, slots)
    print(f"Hash value for {key} is {value}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
