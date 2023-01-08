/*
Raspberry Pi Foundation
Developed to be used alongside Isaac Computer Science, part of the National Centre for Computing Education
Usage licensed under CC BY-SA 4

Note: This file is designed to be copied out and compiled on your machine.
In order for it to compile properly you need to ensure that the project name is the same as the "namespace" in this file.
To run this file you need to:
1. Copy the contents
2. Paste them into the C# IDE of your choice (Visual Studio, for example)
3. Change the namespace to match your project (if necessary)
4. Compile the program
5. Run the program
*/

using System;
using System.Collections.Generic;
using System.Text;

namespace IsaacCodeSamples
{
    class VernamCipher
    {
        // The Main method is the entry point for all C# programs
        public static void Main()
        {
            string plaintext = "HELLO";
            string key = "PLUTO";

            string ciphertext = Vernam(plaintext, key);

            Console.WriteLine($"\nPlaintext: '{plaintext}'");
            Console.WriteLine($"\nCiphertext: '{ciphertext}'");

            string decrypt = Vernam(ciphertext, key);
            Console.WriteLine($"\nDecrypted ciphertext: '{decrypt}'");
        }

        /*
        The Vernam cipher is, in theory, a perfect cipher. 
        Instead of a single key, each plain text character is encrypted using its own key. 
        This means that there is no way that the cipher text can be deciphered without the key.
        https://isaaccomputerscience.org/concepts/data_encrypt_vernam?examBoard=all&stage=all
        */
        public static string Vernam(string plaintext, string key)
        {
            byte[] plaintext_binary = Encoding.ASCII.GetBytes(plaintext); // Convert the plaintext string to binary
            byte[] key_binary = Encoding.ASCII.GetBytes(key.Substring(0, plaintext.Length)); // We only need to convert as many characters of the key as we are going to use
            byte[] ciphertext_binary = new byte[plaintext_binary.Length];

            for (int i = 0; i < plaintext_binary.Length; i++) // Iterate through each character
            {
                ciphertext_binary[i] = (byte)(plaintext_binary[i] ^ key_binary[i]); // XOR the plaintext byte with the key byte
            }

            string ciphertext = Encoding.ASCII.GetString(ciphertext_binary); // Convert the binary ciphertext back to a string
            return ciphertext;
        }
    }
}