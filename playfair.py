from string import ascii_uppercase


class Playfair:
    def __init__(self, key: str):
        self.key = self.make_key(key)
        self.matrix = self.create_matrix(self.key)

    def make_key(self, key: str):
        """Подготовка ключа: убираем повторы"""
        key = key.upper().replace('J', 'I')
        unique_key = set()
        prepared_key = ''
        for letter in key:
            if letter.isalpha() and letter not in unique_key:
                unique_key.add(letter)
                prepared_key += letter
        return prepared_key

    def create_matrix(self, key: str):
        """Создание матрицы"""
        alphabet = ascii_uppercase.replace('J', '')
        unique_matrix = set(key)
        matrix = key
        for letter in alphabet:
            if letter not in unique_matrix:
                matrix += letter
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_position(self, char):
        """Поиск буквы в матрице"""
        for i, row in enumerate(self.matrix):
            if char in row:
                return i, row.index(char)
        return None, None

    def encode_pair(self, a, b):
        """Кодировка биграмм"""
        row_a, col_a = self.find_position(a)
        row_b, col_b = self.find_position(b)

        if row_a is None or row_b is None:
            raise ValueError(f"Символы '{a}' или '{b}' не найдены в матрице")

        if row_a == row_b:
            return self.matrix[row_a][(col_a + 1) % 5] + self.matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            return self.matrix[(row_a + 1) % 5][col_a] + self.matrix[(row_b + 1) % 5][col_b]
        else:
            return self.matrix[row_a][col_b] + self.matrix[row_b][col_a]

    def encode(self, text):
        text = text.upper().replace('J', 'I')
        cleaned_text = []

        for char in text:
            if char.isalpha():
                cleaned_text.append(char)

        i = 0
        while i < len(cleaned_text):
            a = cleaned_text[i]
            b = cleaned_text[i + 1] if i + 1 < len(cleaned_text) else 'X'

            if a == b:
                cleaned_text.insert(i + 1, 'X')
                b = 'X'

            pairs = self.encode_pair(a, b)
            cleaned_text[i:i + 2] = pairs
            i += 2

        return "".join(cleaned_text)


key = "HOLLYWOOD"

playfair_cipher = Playfair(key)
cleaned_key = playfair_cipher.make_key(key)
our_matrix = playfair_cipher.create_matrix(cleaned_key)


text = "HELLOOOZ"

encoded_text = playfair_cipher.encode(text)

print("Зашифрованный текст:", encoded_text)
