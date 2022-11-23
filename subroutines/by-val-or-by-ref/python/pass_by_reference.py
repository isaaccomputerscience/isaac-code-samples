# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_sub_value_reference

def add_new_item(a_list, item):
    """Adds an item to a list"""
    a_list.append(item)  # Uses built in method   
    
def main():
    shopping_list = []  # An empty list
    new_item = "milk"
    add_new_item(shopping_list, new_item)
    new_item = "bread"
    add_new_item(shopping_list, new_item)
    new_item = "cake"
    add_new_item(shopping_list, new_item)
    print(shopping_list)


if __name__ == '__main__':
    main()
