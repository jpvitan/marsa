"""

MARSA
A Python library that lets you experiment with the mathematics of the Rivest–Shamir–Adleman (RSA) cryptosystem.

This project is under the MIT license.

Copyright © 2024 Justine Paul Vitan. All rights reserved.

License Information: https://github.com/jpvitan/marsa/blob/master/LICENSE
Developer's Website: https://jpvitan.com/

"""

from marsa import compute


class Key:
    def __init__(self, product: int, exponent: int):
        self.product = product
        self.exponent = exponent


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


class KeyPair:
    def __init__(self, size: int = 2048, public_exponent: int = 65537):
        first_prime = compute.generate_prime(size // 2)
        second_prime = compute.generate_prime(size // 2)

        product = first_prime * second_prime
        lambda_n = compute.lcd(first_prime - 1, second_prime - 1)

        private_exponent = (
            compute.gcd_linear_combination(public_exponent, lambda_n)[0] % lambda_n
        )

        self.public_key = Key(product, public_exponent)
        self.private_key = Key(product, private_exponent)
