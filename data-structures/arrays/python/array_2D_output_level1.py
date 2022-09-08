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


def output_level(given_list, level):
    """Output every element from a single level"""

    # Output each word from a particular level
    for word in range(0, len(given_list[level])):
         print(given_list[level][word])


def main():
    """Create a list and output every element in a single level"""

    # Create a two-dimensional list
    my_list = create_2D_list()

    # Output every element for level 1
    print("### Output each element for level 1 ###")
    output_level(my_list, LEVEL1)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
