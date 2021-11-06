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
    A class that holds the prime product and auxiliary value.

    Parameters:
    prime_product (int): The product of two primes.
    auxiliary (int): Exponent of the encrypted or decrypted message.
    """

    def __init__(self, prime_product: int, auxiliary: int):
        self.prime_product = prime_product
        self.auxiliary = auxiliary

    def __str__(self):
        return "Key Contents:\nPrime Product = {:d}\nAuxiliary = {:d}".format(self.prime_product, self.auxiliary)


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
    A class that encrypts data based on the key parameter.

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
        return pow(message, self.public_key.auxiliary, self.public_key.prime_product)


class Decryptor:
    """
    A class that decrypts data based on the key parameter.

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
        return pow(message, self.private_key.auxiliary, self.private_key.prime_product)


def generate_key_pair() -> KeyPair:
    """
    A function that generates a public key and private key.

    Returns:
    KeyPair: A class that holds the public key and private key.
    """

    first_prime = rmath.generate_prime_candidate(1024)
    second_prime = rmath.generate_prime_candidate(1024)

    prime_product = first_prime * second_prime
    lambda_n = rmath.lcd(first_prime - 1, second_prime - 1)
    public_auxiliary = 65537
    private_auxiliary = rmath.gcd_linear_combination(public_auxiliary, lambda_n)[
                            0] % lambda_n

    public_key = Key(prime_product, public_auxiliary)
    private_key = Key(prime_product, private_auxiliary)
    key_pair = KeyPair(public_key, private_key)

    return key_pair
