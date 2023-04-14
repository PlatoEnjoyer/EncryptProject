import unittest
from Vigenere_cipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = VigenereCipher('eng')

    def test_vigenere_cipher(self):
        cipher_text = self.cipher.vigenere_cipher("ATTACKATDAWN", "LEMONLEMONLE")
        self.assertEqual(cipher_text, 'LXFOPVEFRNHR')

    def test_vigenere_decipher(self):
        text = self.cipher.vigenere_decipher('LXFOPVEFRNHR', 'LEMONLEMONLE')
        self.assertEqual(text, "ATTACKATDAWN")
