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


def output_each_element(given_list):
    """Output every element in a three-dimensional list"""

    # Repeat for each year
    for year in range(0, len(given_list)):
        # Repeat for each level
        for level in range(0, len(given_list[year])):
            # Output each word for the current year and level
            for word in range(0, len(given_list[year][level])):
                 print(given_list[year][level][word])


def main():
    """Create a list and output every element"""

    # Create a three-dimensional list
    my_list = create_3D_list()

    # Output every element in the list
    print("### Output each element in the 3D list ###")
    output_each_element(my_list)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
