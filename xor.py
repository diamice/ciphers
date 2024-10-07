from itertools import cycle


def xor_bytes_cipher(text: bytes, key: str) -> bytes:
    key = key.encode('utf8')
    return bytes([a ^ b for a, b in zip(text, cycle(key))])


def xor_digits(num, key):
    return num ^ key


if __name__ == '__main__':
    text = input("Введите текст для шифрования: ")
    key = input("Введите ключ: ")

    if text.isdigit():
        print("Зашифрованный текст:", encoded_text := xor_digits(int(text), int(key)))
        print("Расшифрованный текст:", decoded_text := xor_digits(int(encoded_text), int(key)))
    else:
        encoded_text = xor_cipher(text.encode('utf8'), key)
        print(f"Зашифрованный текст: {encoded_text}")

        decoded_text = xor_cipher(encoded_text, key).decode('utf8')
        print(f"Расшифрованный текст: {decoded_text}")
