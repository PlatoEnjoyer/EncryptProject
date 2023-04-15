class VigenereCipher:
    def __init__(self, alphabet, voluntary=False):
        if voluntary:
            self.lower_dict = input('Введите Ваш алфавит в строчном виде')
            self.upper_dict = self.lower_dict.upper()
        else:
            if alphabet.lower() == 'ru':
                self.lower_dict, self.upper_dict = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",\
                    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
            else:
                self.lower_dict, self.upper_dict = "abcdefghijklmnopqrstuvwxyz", \
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def vigenere_cipher(self, text, key):
        """
        Функция шифрует текст шифром Виженера, общая формула шифра - Ci = (Mi + Ki) mod len(alphabet)
        Ci - зашифрованный символ исходного текста, Mi - номер буквы открытого текста, Ki - номер буквы ключа.
        :param text: Исходный текст
        :param key: Ключ - обязательно должен быть составлен из символов алфавита исходного текста
        :return: Зашифрованный текст
        """
        res = ''
        key = key.lower()

        for i, char in enumerate(text):
            if char.isalpha():
                shift = self.lower_dict.index(key[i % len(key)])
                shifted_char = self.lower_dict[(self.lower_dict.index(char.lower()) + shift) % len(self.lower_dict)]
                if char.isupper():
                    shifted_char = shifted_char.upper()
                res += shifted_char
            else:
                res += char
        return res

    def vigenere_decipher(self, text, key):
        # Работает так же как и шифратор, только в обратную сторону
        # Общая формула дешифровки - Mi = (Ci - Ki) mod len(alphabet)
        res = ''
        key = key.lower()

        for i, char in enumerate(text):
            if char.isalpha():
                shift = self.lower_dict.index(key[i % len(key)])
                shifted_char = self.lower_dict[(self.lower_dict.index(char.lower()) - shift) % len(self.lower_dict)]
                if char.isupper():
                    shifted_char = shifted_char.upper()
                res += shifted_char
            else:
                res += char
        return res