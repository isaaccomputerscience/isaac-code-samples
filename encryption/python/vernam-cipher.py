# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

"""
    The Vernam cipher is, in theory, a perfect cipher. 
    Instead of a single key, each plain text character is encrypted using its own key. 
    This means that there is no way that the cipher text can be deciphered without the key.
    https://isaaccomputerscience.org/concepts/data_encrypt_vernam?examBoard=all&stage=all
"""


def vernam(plaintext, key):
    # Vernam cipher key should be the same length or longer than the plain text.
    if len(plaintext) > len(key):
        print("Key is not long enough!")
        return None

    ciphertext = ""

    for i in range(len(plaintext)):
        # ord("") returns the ascii value of a character as an integer
        plaintext_character = ord(plaintext[i])
        key_character = ord(key[i])

        # XOR plaintext with key to get ciphertext
        cipher_character = plaintext_character ^ key_character

        print(
            f"'{plaintext[i]}' (Binary: {bin(plaintext_character)}) XOR '{key[i]}' (Binary: {bin(key_character)}) = {bin(cipher_character)}")
        ciphertext += chr(cipher_character)

    return ciphertext


def main():
    plaintext = "HELLO"
    key = "PLUTO"

    print(f"\nPlaintext: '{plaintext}'")

    print("\n--- Encrypting ---")
    encrypt = vernam(plaintext, key)
    print(f"Encrypted text: '{encrypt}'")

    print("\n--- Decrypting ---")
    decrypt = vernam(encrypt, key)
    print(f"Decrypted text: '{decrypt}'")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main()
