from random import randint


class CaesarCipher:
    def __init__(self, lang):
        if lang.lower() == 'ru':
            self.lower_dict, self.upper_dict = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",\
                "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        else:
            self.lower_dict, self.upper_dict = "abcdefghijklmnopqrstuvwxyz", \
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encryptor(self, text, key=None):
        if not key:
            key = randint(1, len(self.lower_dict))
            print(f'Ваш случайно сгенерированный ключ: {key}')
        text = list(text)
        for i in range(len(text)):
            if text[i].islower():
                new_index = (self.lower_dict.find(text[i]) + key) % len(self.lower_dict)
                text[i] = self.lower_dict[new_index]
            else:
                new_index = (self.upper_dict.find(text[i]) + key) % len(self.lower_dict)
                text[i] = self.upper_dict[new_index]

        return ''.join(text)

    def decryptor(self, text, key):
        text = list(text)
        for i in range(len(text)):
            if text[i].islower():
                new_index = (self.lower_dict.find(text[i]) - key) % len(self.lower_dict)
                text[i] = self.lower_dict[new_index]
            else:
                new_index = (self.upper_dict.find(text[i]) - key) % len(self.lower_dict)
                text[i] = self.upper_dict[new_index]

        return ''.join(text)


f = CaesarCipher('ru')
print(f.encryptor('Приветствую', 3))
print(f.decryptor('ТулезхфхецБ', 3))
