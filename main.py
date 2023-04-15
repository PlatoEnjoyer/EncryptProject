import argparse
from CaesarCipher.Ceasar_cipher import CaesarCipher
from VernamCipher.Vernam_cipher import vernam_cipher, vernam_decipher
from VigenereCipher.Vigenere_cipher import VigenereCipher


def process_values(values):
    return values.split('--')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt or decrypt text')
    parser.add_argument('--caesar_encrypt', dest='caesar_plaintext', help='Choose an algorithm')
    parser.add_argument('--caesar_encrypt_with_key', dest='caesar_plaintext_with_key', help='Choose an algorithm')
    parser.add_argument('--caesar_decrypt', dest='caesar_ciphertext', help='Choose an algorithm')
    parser.add_argument('--caesar_break', dest='caesar_ciphertext_without_key', help='Choose an algorithm')

    parser.add_argument('--vernam_encrypt', dest='vernam_plaintext', help='Choose an algorithm')
    parser.add_argument('--vernam_decrypt', dest='vernam_ciphertext', help='Choose an algorithm')

    parser.add_argument('--vigenere_encrypt', dest='vigenere_plaintext', help='Choose an algorithm')
    parser.add_argument('--vigenere_decrypt', dest='vigenere_ciphertext', help='Choose an algorithm')
    args = parser.parse_args()

    if args.caesar_plaintext:
        values = process_values(args.caesar_plaintext)
        with open(values[1], 'r') as file:
            text = file.read()
        caesar = CaesarCipher(values[0])
        print(caesar.cipher(text))

    elif args.caesar_ciphertext:
        values = process_values(args.caesar_ciphertext)
        with open(values[1], 'r') as file:
            text = file.read()
        caesar = CaesarCipher(values[0])
        print(caesar.decipher(values[1], int(values[2])))

    elif args.caesar_plaintext_with_key:
        values = process_values(args.caesar_plaintext_with_key)
        with open(values[1], 'r') as file:
            text = file.read()
        caesar = CaesarCipher(values[0])
        print(caesar.cipher(values[1], int(values[2])))

    elif args.caesar_ciphertext_without_key:
        values = process_values(args.caesar_ciphertext_without_key)
        with open(values[1], 'r') as file:
            text = file.read()
        caesar = CaesarCipher(values[0])
        print(caesar.decrypt(values[1]))

    elif args.vernam_plaintext:
        with open(args.vernam_plaintext, 'r') as file:
            text = file.read()
        vernam = vernam_cipher(text)
        print(vernam)

    elif args.vernam_ciphertext:
        values = process_values(args.vernam_ciphertext)
        with open(values[1], 'r') as file:
            text = file.read()
        vernam = vernam_decipher(values[0], values[1])
        print(vernam)

    elif args.vigenere_plaintext:
        values = process_values(args.vigenere_plaintext)
        with open(values[1], 'r') as file:
            text = file.read()
        vigenere = VigenereCipher(values[0])
        print(vigenere.vigenere_cipher(values[1], values[2]))

    elif args.vigenere_ciphertext:
        values = process_values(args.vigenere_ciphertext)
        with open(values[1], 'r') as file:
            text = file.read()
        vigenere = VigenereCipher(values[0])
        print(vigenere.vigenere_decipher(values[1], values[2]))
