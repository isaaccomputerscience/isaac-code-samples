# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_sub_local_and_global


def calculate_reduced_vat():

    """Calculate vat at a reduced rate"""

    # Local variable also called vat_rate overrides the vat_rate from global scope
    vat_rate = 0.05 

    amount = float(input("Enter amount to calculate VAT on: "))
    vat = amount * vat_rate
    print(vat)



if __name__ == '__main__':

    # Global variable vat_rate is defined within the global scope
    vat_rate = 0.2
    calculate_reduced_vat()