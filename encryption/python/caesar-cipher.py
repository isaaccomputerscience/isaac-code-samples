# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

import string

"""
    The Caesar Cipher uses a constant integer: "key" to convert plaintext to ciphertext
    by shifting each letter along in the alphabet by the value of the key.
"""


def caesar_cipher_shift(plaintext, key):
    # This shift will only work on lowercase letters!
    alphabet = string.ascii_lowercase
    ciphertext = ""

    for letter in plaintext:
        if letter == " ":
            ciphertext += " "
        else:
            current_index = alphabet.index(letter)
            shifted_index = (current_index + key) % len(alphabet)
            ciphertext += alphabet[shifted_index]

    return ciphertext


def main():
    plaintext = "a byte is eight bits"
    key = 13

    print(f"\nPlaintext: {plaintext}")

    print("\n--- Encrypting ---")
    encrypt = caesar_cipher_shift(plaintext, key)
    print(encrypt)

    print("\n--- Decrypting ---")
    decrypt = caesar_cipher_shift(encrypt, -key)
    print(decrypt)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main()
