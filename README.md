# ChipherProject
Documentation for Encryption and Decryption Program
This program allows the user to encrypt or decrypt text using various ciphers - Caesar Cipher, Vernam Cipher, and Vigenere Cipher.

Usage
To run the program, navigate to the directory where the program is located and run the following command:

python encryption_decryption.py --[cipher_type] [arguments]
Here, [cipher_type] refers to the type of cipher to use - caesar_encrypt, caesar_encrypt_with_key, caesar_decrypt, caesar_break, vernam_encrypt, vernam_decrypt, vigenere_encrypt, or vigenere_decrypt.

The arguments vary based on the cipher type:

Caesar Cipher:
--caesar_encrypt - requires two arguments - the encryption key and the path to the plaintext file.
--caesar_encrypt_with_key - requires three arguments - the encryption key, the path to the plaintext file, and the key for the cipher.
--caesar_decrypt - requires three arguments - the decryption key, the path to the ciphertext file, and the key for the cipher.
--caesar_break - requires one argument - the path to the ciphertext file.

Vernam Cipher:
--vernam_encrypt - requires one argument - the path to the plaintext file.
--vernam_decrypt - requires two arguments - the path to the ciphertext file and the key for the cipher.

Vigenere Cipher:
--vigenere_encrypt - requires three arguments - the encryption key, the path to the plaintext file, and the key for the cipher.
--vigenere_decrypt - requires three arguments - the decryption key, the path to the ciphertext file, and the key for the cipher.

Here are some examples of how to use the program:

python encryption_decryption.py --caesar_encrypt 5 plaintext.txt
This encrypts the text in the plaintext.txt file using a Caesar cipher with a key of 5.

python encryption_decryption.py --caesar_decrypt 5 ciphertext.txt
This decrypts the text in the ciphertext.txt file using a Caesar cipher with a key of 5.

python encryption_decryption.py --vernam_encrypt plaintext.txt
This encrypts the text in the plaintext.txt file using a Vernam cipher.

python encryption_decryption.py --vigenere_encrypt secretkey plaintext.txt cipherkey
This encrypts the text in the plaintext.txt file using a Vigenere cipher with a secret key of secretkey and a cipher key of cipherkey.
