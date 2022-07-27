# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_softeng_debug

def add_vat (amount):
    '''calculate and applies VAT at standard rate'''
    RATE = 20
    vat = amount * RATE
    with_vat = amount + vat
    return with_vat