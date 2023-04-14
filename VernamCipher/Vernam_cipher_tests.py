import unittest
from string import ascii_letters
from Vernam_cipher import key_gen, vernam_cipher, vernam_decipher


class TestVernamCipher(unittest.TestCase):

    def test_key_gen(self):
        """
        Тестирование функции key_gen
        """
        length = 10
        key = key_gen(length)
        self.assertEqual(len(key), length)
        self.assertTrue(all(char in ascii_letters for char in key))

    def test_vernam_cipher(self):
        """
        Тестирование функции vernam_cipher
        """
        message = 'Hello, world!'
        cipher, key = vernam_cipher(message)
        self.assertEqual(len(cipher), len(message) * 8)
        self.assertTrue(all(char in '01' for char in cipher))
        self.assertEqual(len(key), len(message))
        self.assertTrue(all(char in ascii_letters for char in key))

        decrypted = vernam_decipher(cipher, key)
        self.assertEqual(decrypted, message)

    def test_vernam_decipher(self):
        """
        Тестирование функции vernam_decipher
        """
        message = 'Hello, world!'
        cipher, key = vernam_cipher(message)
        decrypted = vernam_decipher(cipher, key)
        self.assertEqual(decrypted, message)


if __name__ == '__main__':
    unittest.main()
