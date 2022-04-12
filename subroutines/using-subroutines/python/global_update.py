# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_using_subroutines

def global_update_example():
    global number
    number = 10
    print(number)

number = 5
global_update_example()
print(number)
