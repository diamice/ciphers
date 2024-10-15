import re
from string import ascii_lowercase, ascii_uppercase
from itertools import cycle


class Vigenere:
    eng_alphabet_digits = dict(zip(ascii_lowercase, range(26)))
    eng_digits_alphabet = dict(zip(range(26), ascii_lowercase))

    ru_alphabet = ''.join([chr(i) for i in range(ord('а'), ord('я') + 1)])
    ru_alphabet = ru_alphabet[:6] + 'ё' + ru_alphabet[6:]

    ru_alphabet_digits = dict(zip(ru_alphabet, range(33)))
    ru_digits_alphabet = dict(zip(range(33), ru_alphabet))

    def __init__(self, key: str):
        self.key = key.lower()

    def _clean_text(self, text: str) -> str:
        return re.sub(r'[^a-zA-Zа-яА-ЯёЁ]+', '', text.lower())

    @staticmethod
    def _get_alphabet_consts(text: str):
        if set(text).intersection(set(ascii_lowercase)):
            return Vigenere.eng_alphabet_digits, Vigenere.eng_digits_alphabet, len(Vigenere.eng_alphabet_digits)
        return Vigenere.ru_alphabet_digits, Vigenere.ru_digits_alphabet, len(Vigenere.ru_digits_alphabet)

    def encode(self, text: str) -> str:
        cleaned_text = self._clean_text(text)
        result = []

        alphabet_digits, digits_alphabet, alphabet_size = self._get_alphabet_consts(cleaned_text[0])

        for symbol, k_letter in zip(cleaned_text, cycle(self.key)):
            res = (alphabet_digits[symbol] + alphabet_digits[k_letter]) % alphabet_size
            result.append(digits_alphabet[res])

        return ''.join(result)

    def decode(self, text: str) -> str:
        cleaned_text = self._clean_text(text)
        result = []

        alphabet_digits, digits_alphabet, alphabet_size = self._get_alphabet_consts(cleaned_text[0])

        for symbol, k_letter in zip(cleaned_text, cycle(self.key)):
            res = (alphabet_digits[symbol] - alphabet_digits[k_letter]) % alphabet_size
            if res < 0:
                res = (res + alphabet_size) % alphabet_size
            result.append(digits_alphabet[res])

        return ''.join(result)


if __name__ == '__main__':
    text = input("Введите текст для шифрования: ")
    key = input("Введите ключ: ")
    vigenere_cipher = Vigenere(key)
    encoded_text = vigenere_cipher.encode(text)
    print(f"Зашифрованный текст: {encoded_text}")
    decoded_text = vigenere_cipher.decode(encoded_text)
    print(f"Расшифрованный текст: {decoded_text}", end='\n\n')
