from string import ascii_letters
from random import choice


def key_gen(length):
    key = ''.join([choice(ascii_letters) for _ in range(length)])
    return key


def vernam_cipher(message):
    """
    Шифрует сообщение шифром Вернама
    :param message: Исходное сообщение, составленное только из символов, входящих в кодировку ASCII
    :return: Двоичное число и ключ, подав их в паре функции-дешифратору, вы получите исходное сообщение
    """
    key = key_gen(len(message))
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_key = ''.join(format(ord(char), '08b') for char in key)

    cipher = ''
    for i in range(len(binary_message)):
        cipher += str(int(binary_message[i]) ^ int(binary_key[i]))

    return f'Ваш зашифрованный текст - {cipher} \nВаш ключ - {key}'


def vernam_decipher(cipher_text, key):
    binary_key = ''.join(format(ord(char), '08b') for char in key)
    decipher = ''
    for i in range(len(cipher_text)):
        decipher += str(int(cipher_text[i]) ^ int(binary_key[i]))

    decipher = [int(decipher[i:i+8], 2) for i in range(0, len(decipher), 8)]
    decipher = ''.join([chr(i) for i in decipher])
    return decipher
