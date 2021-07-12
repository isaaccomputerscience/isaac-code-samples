# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_value_reference


# Python does not use pure pass by reference so we have simulated this using a list


def double(x):
    # Modify the second item within the list x
    x[1] = x[1] * 2
    print(f"x within double(): {x}")


def main():

    # Initialise x
    x = [0, 1]

    print(f"x in main() before procedure call: {x}")

    double(x)

    # The value of x has been altered within the double() procedure
    print(f"x in main() after procedure call: {x}")


if __name__ == '__main__':
    main()
