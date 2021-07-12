# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_local_and_global

def basic_tax_rate():
    amount = float(input("£"))
    tax = amount * 0.2
    print(tax)  # You could format this to two decimal places using print(f"£{tax:.2f}")  


def higher_tax_rate():
    amount = float(input("£"))
    tax = amount * 0.4
    print(tax)    

def main():
    print("Enter an amount in pounds to find the basic tax rate:")
    basic_tax_rate()
    print("Enter an amount in pounds to find the higher tax rate:")
    higher_tax_rate()


if __name__ == '__main__':
    main() 