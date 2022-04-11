def global_example():
    """This function accesses a global variable"""
    print(number)

number = 5  # global variable
global_example()
print(number)
