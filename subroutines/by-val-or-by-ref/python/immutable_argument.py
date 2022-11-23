# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_value_reference

def change_value(item):
    """demonstrates passing by reference"""
    print("\n")
    print(f"Original value in change_value: {item}")
    object_id = id(item)
    print(f"Original object id in change_value: {object_id}")
    item = "cat"
    print(f"New value in change_value: {item}")
    object_id = id(item)
    print(f"New object id in change_value: {object_id}")

def main():
    word = "dog"
    print(f"Original value in main: {word}")
    object_id = id(word)
    print(f"Original object id in main: {object_id}")
    change_value(word) # Call function to modify value
    print("\n")
    object_id = id(word)
    print(f"Value in main after function call: {word}")
    object_id = id(word)
    print(f"Object id in main after function call: {object_id}")


if __name__ == '__main__':
    main()
