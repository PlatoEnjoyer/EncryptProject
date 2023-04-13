from random import randint


class CaesarCipher:
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

    def cipher(self, text: str, key: int = None):
        """
        Возвращает зашифрованный с помощью шифра Цезаря текст.
        Шифрует только буквы алфавита выбранного языка.
        :param text: Текст который нужно зашифровать.
        :param key: Ключ можно указать, в противном случае он будет сгенерирован случайным образом.
        :return: Возвращает зашифрованный текст
        """
        if not key:
            key = randint(1, len(self.lower_dict))
            print(f'Ваш случайно сгенерированный ключ: {key}')
        text = list(text)
        for i in range(len(text)):

            if text[i].islower():
                new_index = (self.lower_dict.find(text[i]) + key) % len(self.lower_dict)
                text[i] = self.lower_dict[new_index]

            elif text[i].isupper():
                new_index = (self.upper_dict.find(text[i]) + key) % len(self.lower_dict)
                text[i] = self.upper_dict[new_index]

        return ''.join(text)

    def decipher(self, text, key):
        # Метод-дешифратор с ключом
        text = list(text)
        for i in range(len(text)):
            if text[i].islower():
                new_index = (self.lower_dict.find(text[i]) - key) % len(self.lower_dict)
                text[i] = self.lower_dict[new_index]
            elif text[i].isupper():
                new_index = (self.upper_dict.find(text[i]) - key) % len(self.lower_dict)
                text[i] = self.upper_dict[new_index]

        return ''.join(text)

    def decrypt(self, ciphertext):
        """
        Метод-дешифратор без ключа.
        :param ciphertext: Зашифрованный текст.
        :return: Массив текстов с перебором ключей.
        """
        # Обработка зашифрованного текса - приводим все символы в lowercase
        ciphertext = [el.lower() for el in ciphertext]
        # Если текст слишком большой - обрезаем его
        if len(ciphertext) > 50:
            ciphertext = ciphertext[:50]

        res = []
        for key in range(len(self.lower_dict)):
            res.append(f'Текст со сдвигом в {key}' + ': ' + self.decipher(ciphertext, key))

        return res


c = CaesarCipher('ru')
print(c.decrypt('Хцозкш тоц!'))
