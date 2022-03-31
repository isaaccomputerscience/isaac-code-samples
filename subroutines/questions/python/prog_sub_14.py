def multiply(a, b):
    """Multiplies two numbers together and retursn the product"""
    return a * b


def add(a, b):
    """Adds two numbers together and returns the sum"""
    return a + b


def find_y(x, m, c):
    print("x=" + str(x) + " y=", end="")
    print(add(multiply(m, x), c))


find_y(5, 2, 3)
