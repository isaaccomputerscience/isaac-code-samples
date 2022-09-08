# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def create_list():
    """Create a list of words"""

    # Declare an empty list
    spelling_words = []

    # Append 10 words to the list
    spelling_words.append("path")
    spelling_words.append("floor")
    spelling_words.append("sugar")
    spelling_words.append("because")
    spelling_words.append("beautiful")
    spelling_words.append("clothes")
    spelling_words.append("whole")
    spelling_words.append("behind")
    spelling_words.append("move")
    spelling_words.append("busy")

    # Return the list
    return spelling_words


def output_each_element(given_list):
    """Output every element in a list"""

    # Output each word in the list
    for i in range(0, len(given_list)):
        print(given_list[i])


def main():
    """Create a list and output every element"""

    # Create a list
    my_list = create_list()

    # Output every element in the list
    print("### Output each element in the list ###")
    output_each_element(my_list)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
