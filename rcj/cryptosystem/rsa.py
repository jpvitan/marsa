"""
rcj.cryptosystem.rsa
rsa.py

LICENSE: GNU General Public License v3 (GPLv3)
Created by Justine Paul Sanchez Vitan.
Copyright © 2021 Justine Paul Sanchez Vitan. All rights reserved.
"""

# IMPORT STATEMENTS

from rcj.utility import rmath


class Key:
    """
    A class that holds the product of two primes and exponent of the public or private key.

    Parameters:
    Product (int): The product of two primes.
    Exponent (int): The exponent of the public or private key.
    """

    def __init__(self, product: int, exponent: int):
        self.product = product
        self.exponent = exponent

    def __str__(self):
        return "Key Contents:\nProduct = {:d}\nExponent = {:d}".format(self.product, self.exponent)


class KeyPair:
    """
    A class that holds the public key and private key.

    Parameters:
    public_key (Key): The public key.
    private_key (Key): The private key.
    """

    def __init__(self, public_key: Key, private_key: Key):
        self.public_key = public_key
        self.private_key = private_key

    def __str__(self):
        return "[PUBLIC KEY]\n{:s}\n\n[PRIVATE KEY]\n{:s}".format(str(self.public_key), str(self.private_key))


class Encryptor:
    """
    A class that encrypts data based on the provided key.

    Parameters:
    public_key (Key): The public key.
    """

    def __init__(self, public_key: Key):
        self.public_key = public_key

    def encrypt(self, message: int) -> int:
        """
        A method that takes an integer and encrypts it.

        Parameters:
        message (int): The integer to be encrypted.

        Returns:
        int: The encrypted integer.
        """
        return pow(message, self.public_key.exponent, self.public_key.product)


class Decryptor:
    """
    A class that decrypts data based on the provided key.

    Parameters:
    private_key (Key): The private key.
    """

    def __init__(self, private_key: Key):
        self.private_key = private_key

    def decrypt(self, message: int) -> int:
        """
        A method that takes an integer and decrypts it.

        Parameters:
        message (int): The integer to be decrypted.

        Returns:
        int: The decrypted integer.
        """
        return pow(message, self.private_key.exponent, self.private_key.product)


def generate_key_pair() -> KeyPair:
    """
    A function that generates a public key and a private key.

    Returns:
    KeyPair: A class that holds the public key and private key.
    """

    first_prime = rmath.generate_prime_candidate(1024)
    second_prime = rmath.generate_prime_candidate(1024)

    product = first_prime * second_prime
    lambda_n = rmath.lcd(first_prime - 1, second_prime - 1)
    public_exponent = 65537
    private_exponent = rmath.gcd_linear_combination(public_exponent, lambda_n)[0] % lambda_n
    public_key = Key(product, public_exponent)
    private_key = Key(product, private_exponent)
    key_pair = KeyPair(public_key, private_key)

    return key_pair
