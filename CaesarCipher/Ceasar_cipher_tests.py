import unittest

from Ceasar_cipher import CaesarCipher


class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher('ru')

    def test_encryptor_with_key(self):
        text = "Привет, мир!"
        key = 10
        encrypted_text = self.cipher.encryptor(text, key)
        self.assertEqual(encrypted_text, "Щътлоь, цтъ!")

    def test_encryptor_without_key(self):
        text = "Привет, мир!"
        encrypted_text = self.cipher.encryptor(text)
        self.assertNotEqual(encrypted_text, "Привет, мир!")

    def test_decryptor(self):
        encrypted_text = "Щътлоь, цтъ!"
        key = 10
        decrypted_text = self.cipher.decryptor(encrypted_text, key)
        self.assertEqual(decrypted_text, "Привет, мир!")


if __name__ == '__main__':
    unittest.main()
