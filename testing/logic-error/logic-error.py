# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_softeng_debug

def add_vat (amount):
    '''calculates and applies VAT at standard rate'''
    RATE = 20
    vat = amount * RATE
    with_vat = amount + vat
    return with_vat
