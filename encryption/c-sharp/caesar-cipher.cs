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

namespace IsaacCodeSamples
{
    class CaesarCipher
    {
        readonly static char[] alphabet = { //Read-only as we will not be changing the values of the array
            'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z'
        };
        public static void Main()
        {
            string plaintext = "a byte is eight bits";
            int key = 13;

            string ciphertext = CaesarShift(plaintext, key);

            Console.WriteLine($"\nPlaintext: {plaintext}");
            Console.WriteLine($"\nCiphertext: {ciphertext}");

            string decrypt = CaesarShift(ciphertext, -key);
            Console.WriteLine($"\nDecrypted ciphertext: {decrypt}");
        }

        public static string CaesarShift(string plaintext, int key)
        {
            string ciphertext = "";
            foreach (char c in plaintext.ToCharArray())
            {
                if (c != ' ')
                {
                    int this_index = Array.IndexOf(alphabet, c);
                    int new_index = (this_index += key) % alphabet.Length; // Wrap around to the start of the alphabet if new index is past z
                    if (new_index < 0)
                    {
                        new_index += alphabet.Length; // Avoid problems with negative indices.
                    }
                    ciphertext += alphabet[new_index].ToString();
                }
                else
                {
                    ciphertext += ' '.ToString();
                }
            }
            return ciphertext;
        }
    }
}