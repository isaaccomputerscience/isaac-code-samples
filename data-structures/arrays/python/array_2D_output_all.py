# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


# Index values of each level
LEVEL1 = 0 
LEVEL2 = 1
LEVEL3 = 2


def create_2D_list():
    """Create a two-dimensional list of words and levels"""

    # Declare and initialise a two-dimensional list
    spelling_words = [["any", "poor", "gold", "wild", "kind"],
                      ["both", "break", "pretty", "floor", "water"],
                      ["sugar", "clothes", "again", "money", "children"]]

    # Return the list
    return spelling_words


def output_each_element(given_list):
    """Output every element in a two-dimensional list"""

    # Repeat for each level
    for level in range(0, len(given_list)):
        # Output each word for the current level
        for word in range(0, len(given_list[level])):
             print(given_list[level][word])


def main():
    """Create a list and output every element"""

    # Create a two-dimensional list
    my_list = create_2D_list()

    # Output every element in the list
    print("### Output each element in the 2D list ###")
    output_each_element(my_list)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
