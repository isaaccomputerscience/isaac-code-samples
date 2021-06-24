def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def find_y(x, m, c):
    print("x=" + STR(x) + "y=")
    print(add(multiply(m, x), c))


find_y(5, 2, 3)