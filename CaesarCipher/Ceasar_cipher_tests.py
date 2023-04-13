import unittest

from Ceasar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher('ru')

    def test_cipher_with_key(self):
        # Проверка функции-шифратора
        text = "Привет, мир!"
        key = 10
        cipher_text = self.cipher.cipher(text, key)
        self.assertEqual(cipher_text, "Щътлоь, цтъ!")

    def test_cipher_without_key(self):
        # Проверка функции-шифратора без ключа
        text = "Привет, мир!"
        cipher_text = self.cipher.cipher(text)
        self.assertNotEqual(cipher_text, "Привет, мир!")

    def test_decipher(self):
        # Проверка функции-дешифратора с переданным ключом
        cipher_text = "Щътлоь, цтъ!"
        key = 10
        decipher_text = self.cipher.decipher(cipher_text, key)
        self.assertEqual(decipher_text, "Привет, мир!")

    def test_decrypt(self):
        cipher_text = 'Хцозкш, тоц!'
        decrypt_list = self.cipher.decrypt(cipher_text)
        self.assertTrue('Текст со сдвигом в 6: привет, мир!' in decrypt_list)


if __name__ == '__main__':
    unittest.main()
