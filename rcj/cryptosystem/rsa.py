"""
rcj.cryptosystem.rsa
rsa.py

LICENSE: GNU General Public License v3 (GPLv3)
Created by Justine Paul Sanchez Vitan.
Copyright © 2020 Justine Paul Sanchez Vitan. All rights reserved.
"""

# IMPORT STATEMENTS
from rcj.utility import inputchecker

from rcj.utility import rmath


class Key:

    def __init__(self, prime_product: int, auxiliary: int):
        self.prime_product = prime_product
        self.auxiliary = auxiliary

    def __str__(self):
        return "Key Contents:\nPrime Product = {:d}\nAuxiliary = {:d}".format(self.prime_product, self.auxiliary)


class KeyPair:

    def __init__(self, public_key: Key, private_key: Key):
        self.public_key = public_key
        self.private_key = private_key

    def __str__(self):
        return "[PUBLIC KEY]\n{:s}\n\n[PRIVATE KEY]\n{:s}".format(str(self.public_key), str(self.private_key))


class Encryptor:

    def __init__(self, public_key: Key):
        self.public_key = public_key

    def encrypt(self, message: str) -> str:
        encrypted_message = ""
        for character in message:
            encrypted_character = chr((ord(character) ** self.public_key.auxiliary) % self.public_key.prime_product)
            encrypted_message = encrypted_message + encrypted_character
        return encrypted_message


class Decryptor:

    def __init__(self, private_key: Key):
        self.private_key = private_key

    def decrypt(self, message: str) -> str:
        decrypted_message = ""
        for character in message:
            decrypted_character = chr((ord(character) ** self.private_key.auxiliary) % self.private_key.prime_product)
            decrypted_message = decrypted_message + decrypted_character
        return decrypted_message


def generate_key_pair(first_prime: int = None, second_prime: int = None) -> KeyPair:
    prime_pair = rmath.generate_prime_number_list(size=2, shuffle=True)
    if first_prime is None:
        first_prime = prime_pair[0]
        if first_prime == second_prime:
            first_prime = prime_pair[1]
    if second_prime is None:
        second_prime = prime_pair[1]
        if first_prime == second_prime:
            second_prime = prime_pair[0]
    inputchecker.rsa_generate_key_pair(first_prime, second_prime)

    prime_product = first_prime * second_prime
    prime_product_minus_one = (first_prime - 1) * (second_prime - 1)
    public_auxiliary = rmath.find_number_relatively_prime(prime_product_minus_one)
    private_auxiliary = rmath.gcd_linear_combination(public_auxiliary, prime_product_minus_one)[0]

    public_key = Key(prime_product, public_auxiliary)
    private_key = Key(prime_product, private_auxiliary)
    key_pair = KeyPair(public_key, private_key)

    return key_pair
