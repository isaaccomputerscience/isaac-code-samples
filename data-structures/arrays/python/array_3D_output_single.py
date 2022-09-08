# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


# Index values of each year
YEAR1 = 0
YEAR2 = 1

# Index values of each level
LEVEL1 = 0 
LEVEL2 = 1
LEVEL3 = 2


def create_3D_list():
    """Create a three-dimensional list of words, levels and years"""

    # Declare and initialise a three-dimensional list
    spelling_words = [
        [
            ["me", "do", "her", "it", "him"],
            ["put", "ask", "says", "red", "any"],
            ["they", "where", "friend", "fast", "class"]
        ],
        [
            ["door", "find", "most", "bath", "eye"],
            ["every", "great", "climb", "prove", "behind"],
            ["clothes", "again", "improve", "should", "parents"]
        ]
    ]

    # Return the list
    return spelling_words


def main():
    """Create a list and output a single element"""

    # Create a three-dimensional list
    my_list = create_3D_list()

    # Output a single element from the list
    print("### Output a single element from the 3D list ###")
    print(my_list[YEAR2][LEVEL3][4])


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
