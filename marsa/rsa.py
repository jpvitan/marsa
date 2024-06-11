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

    def __str__(self):
        return "Key Contents:\nProduct = {:d}\nExponent = {:d}".format(
            self.product, self.exponent
        )


class KeyPair:

    def __init__(self, public_key: Key, private_key: Key):
        self.public_key = public_key
        self.private_key = private_key

    def __str__(self):
        return "[PUBLIC KEY]\n{:s}\n\n[PRIVATE KEY]\n{:s}".format(
            str(self.public_key), str(self.private_key)
        )


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


def generate_key_pair() -> KeyPair:

    first_prime = math.generate_prime(1024)
    second_prime = math.generate_prime(1024)

    product = first_prime * second_prime
    lambda_n = math.lcd(first_prime - 1, second_prime - 1)
    public_exponent = 65537
    private_exponent = (
        math.gcd_linear_combination(public_exponent, lambda_n)[0] % lambda_n
    )
    public_key = Key(product, public_exponent)
    private_key = Key(product, private_exponent)
    key_pair = KeyPair(public_key, private_key)

    return key_pair
