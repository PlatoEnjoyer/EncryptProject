import argparse
from CaesarCipher.Ceasar_cipher import CaesarCipher
from VernamCipher.Vernam_cipher import vernam_cipher, vernam_decipher
from VigenereCipher.Vigenere_cipher import VigenereCipher


def process_values(values):
    return values.split(' ')


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
        caesar = CaesarCipher(values[0])
        print(caesar.cipher(values[1]))

    elif args.caesar_ciphertext:
        values = process_values(args.caesar_ciphertext)
        caesar = CaesarCipher(values[0])
        print(caesar.decipher(values[1], int(values[2])))

    elif args.caesar_plaintext_with_key:
        values = process_values(args.caesar_plaintext_with_key)
        caesar = CaesarCipher(values[0])
        print(caesar.cipher(values[1], int(values[2])))

    elif args.caesar_ciphertext_without_key:
        values = process_values(args.caesar_ciphertext_without_key)
        caesar = CaesarCipher(values[0])
        print(caesar.decrypt(values[1]))

    elif args.vernam_plaintext:
        vernam = vernam_cipher(args.vernam_plaintext)
        print(vernam)

    elif args.vernam_ciphertext:
        values = process_values(args.vernam_ciphertext)
        vernam = vernam_decipher(values[0], values[1])
        print(vernam)

    elif args.vigenere_plaintext:
        values = process_values(args.vigenere_plaintext)
        vigenere = VigenereCipher(values[0])
        print(vigenere.vigenere_cipher(values[1], values[2]))

    elif args.vigenere_ciphertext:
        values = process_values(args.vigenere_ciphertext)
        vigenere = VigenereCipher(values[0])
        print(vigenere.vigenere_decipher(values[1], values[2]))
