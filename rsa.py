import random


def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_rsa_keys():
    primes = sieve_of_eratosthenes(1000)
    p = random.choice(primes)
    q = random.choice(primes)
    while q == p:
        q = random.choice(primes)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.choice([x for x in range(2, phi) if gcd(x, phi) == 1])

    d = pow(e, -1, phi)

    return (e, n), (d, n)


def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext


def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext


public_key, private_key = generate_rsa_keys()

message = "HELLO"
ciphertext = encrypt(message, public_key)
print("Зашифрованное сообщение:", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("Расшифрованное сообщение:", decrypted_message)
