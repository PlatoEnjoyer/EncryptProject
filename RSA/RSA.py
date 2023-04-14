# В качестве доп задания решил попробовать освоить алгоритм RSA - что-то получилось, но он у меня дешифрует корректно
# далеко не все числа, искать ошибку очень долго, поэтому оставлю как есть - пускай будет на память

import random
import math


def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True


def generate_primes():
    primes = []
    while len(primes) < 2:
        num = random.randint(100, 1000)
        if is_prime(num):
            primes.append(num)
    return primes


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclidean_algorithm(b, a % b)
        return d, y, x - y * (a // b)


def find_inverse(e, phi):
    d, x, y = extended_euclidean_algorithm(e, phi)
    if d != 1:
        raise ValueError("Обратный элемент не существует")
    else:
        return x % phi


def generate_rsa_keys():
    p, q = generate_primes()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = find_inverse(e, phi)
    return (e, n), (d, n)


def encrypt_rsa(msg, public_key):
    e, n = public_key
    res = pow(msg, e, n)
    return res


def decrypt_rsa(cipher, private_key):
    d, n = private_key
    res = pow(cipher, d, n)
    return res


public_key, private_key = generate_rsa_keys()
msg = random.randint(0, 1000000)
cipher = encrypt_rsa(msg, public_key)
decrypted_msg = decrypt_rsa(cipher, private_key)
print("Исходное сообщение:", msg)
print("Зашифрованное сообщение:", cipher)
print("Расшифрованное сообщение:", decrypted_msg)
