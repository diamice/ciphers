import random
import math


class RSA:
    def __init__(self, p, q):
        if not self.is_prime(p):
            raise ValueError(f"{p} не является простым числом!")
        if not self.is_prime(q):
            raise ValueError(f"{q} не является простым числом!")
        if p == q:
            raise ValueError("p и q не должны быть равны!")

        self.p = p
        self.q = q
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)

        self.e = self.generate_e(self.phi_n)
        self.d = self.mod_inverse(self.e, self.phi_n)

    @staticmethod
    def is_prime(number):
        """Проверка, является ли число простым"""
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def mod_inverse(e, phi):
        """Вычисление модульного обратного"""
        for d in range(3, phi):
            if (d * e) % phi == 1:
                return d
        raise ValueError("Mod_inverse does not exist!")

    @staticmethod
    def generate_e(phi):
        """Генерация e"""
        e = random.randint(3, phi - 1)
        while math.gcd(e, phi) != 1:
            e = random.randint(3, phi - 1)
        return e

    def encode(self, message):
        """Шифрование сообщения"""
        message_encoded = [ord(ch) for ch in message]
        ciphertext = [pow(ch, self.e, self.n) for ch in message_encoded]
        return ciphertext

    def decode(self, ciphertext):
        """Дешифрование сообщения"""
        decoded_msg = [pow(ch, self.d, self.n) for ch in ciphertext]
        msg = "".join(chr(ch) for ch in decoded_msg)
        return msg


if __name__ == "__main__":
    p = int(input("Введите простое число p: "))
    q = int(input("Введите простое число q, отличное от p: "))


    try:
        rsa = RSA(p, q)

        message = input("Введите сообщение для шифрования: ")
        ciphertext = rsa.encode(message)
        print(f"{message} зашифровано в: {ciphertext}")

        decoded_message = rsa.decode(ciphertext)
        print("Расшифрованное сообщение:", decoded_message)

    except ValueError as e:
        print(e)
