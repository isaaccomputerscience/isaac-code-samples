# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
# https://isaaccomputerscience.org/concepts/prog_softeng_test_plans 

def check_password(password):
    """Checks that a password length is between 8 and 14 characters. Returns True if valid"""
    is_valid = True
    if len(password) < 8 or len(password) > 14:
        is_valid = False
    return is_valid
