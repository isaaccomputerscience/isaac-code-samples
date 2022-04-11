# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_using_subroutines

def global_example():
    """This function accesses a global variable"""
    print(number)

number = 5  # global variable
global_example()
print(number)
