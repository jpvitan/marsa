"""

MARSA
A Python library that lets you experiment with the mathematics of the Rivest–Shamir–Adleman (RSA) cryptosystem.

This project is under the MIT license.

Copyright © 2024 Justine Paul Vitan. All rights reserved.

License Information: https://github.com/jpvitan/marsa/blob/master/LICENSE
Developer's Website: https://jpvitan.com/

"""

from marsa import math


class Key:

    def __init__(self, product: int, exponent: int):
        self.product = product
        self.exponent = exponent


class KeyPair:

    def __init__(self, public_key: Key, private_key: Key):
        self.public_key = public_key
        self.private_key = private_key


class Encryptor:

    def __init__(self, public_key: Key):
        self.public_key = public_key

    def encrypt(self, message: int) -> int:
        return pow(message, self.public_key.exponent, self.public_key.product)


class Decryptor:

    def __init__(self, private_key: Key):
        self.private_key = private_key

    def decrypt(self, message: int) -> int:
        return pow(message, self.private_key.exponent, self.private_key.product)
