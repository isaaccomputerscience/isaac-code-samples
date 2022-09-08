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


def main():
    """Create a list and output every element"""

    # Create a two-dimensional list
    my_list = create_2D_list()

    # Output a single element from the list
    print("### Output a single element from the 2D list ###")
    print(my_list[LEVEL2][3])


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
