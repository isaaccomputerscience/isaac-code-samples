# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_value_reference

# Python does not strictly use pass by value
# However, arguments passed to a function become local variables inside that function

def double(x):

    # x becomes a separate local variable within the scope of double
    print( f"Local variables within double(): {locals()}" )
    x = x * 2
    print(f"x within double(): {x}")


def main():

    # Initialise x
    x = 25

    print(f"x in main() before procedure call: {x}")

    double(x)

    # The value of x within main has not been altered
    print(f"x in main() after procedure call: {x}")


if __name__ == '__main__':
    main()
