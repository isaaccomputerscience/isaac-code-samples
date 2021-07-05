def calculate_product(n1, n2):
    """Calculates the product of two numbers."""
    product = n1 * n2
    print(product)


def main():
    """Simple program to demonstrate use of call stack."""
    num1 = input("Enter a number ")
    num2 = input("Enter another number ")
    num1_int = int(num1)
    num2_int = int(num2)
    calculate_product(num1_int, num2_int)
    print("I hope you enjoyed using the product calculator")


if __name__ == '__main__':
    main()
