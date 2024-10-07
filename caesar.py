from string import ascii_lowercase
from typing import Tuple


class Caesar:
    ENGLISH_ABC = 26
    RU_ABC = 32

    def __init__(self, text: str, shift: int):
        self.text = text
        self.shift = shift

    @staticmethod
    def _get_alphabet_consts(text: str) -> Tuple[int, int, int]:
        if set(text.lower()).intersection(set(ascii_lowercase)):
            return Caesar.ENGLISH_ABC, ord('A'), ord('a')
        return Caesar.RU_ABC, ord('А'), ord('а')

    def _transform(self, shift: int) -> str:
        alphabet_offset, upper_start, lower_start = self._get_alphabet_consts(self.text)
        result = []
        for symbol in self.text:
            if symbol.isalpha():
                symbol_reg = [upper_start, lower_start][symbol.islower()]
                shifted_letter = chr((ord(symbol) - symbol_reg + shift) % alphabet_offset + symbol_reg)
                result.append(shifted_letter)
            else:
                result.append(symbol)
        self.text = ''.join(result)
        return self.text

    def encode(self) -> str:
        return self._transform(self.shift)

    def decode(self) -> str:
        return self._transform(-self.shift)


if __name__ == "__main__":
    text = input("Введите текст для шифрования: ")
    shift = int(input("Введите сдвиг: "))
    caesar_cipher = Caesar(text, shift)
    encoded_text = caesar_cipher.encode()
    print(f"Зашифрованный текст: {encoded_text}")
    decoded_text = caesar_cipher.decode()
    print(f"Дешифрованный текст: {decoded_text}")
