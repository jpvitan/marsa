"""
rcj.utility.inputchecker
inputchecker.py

LICENSE: GNU General Public License v3 (GPLv3)
Created by Justine Paul Sanchez Vitan.
Copyright © 2020 Justine Paul Sanchez Vitan. All rights reserved.
"""

# IMPORT STATEMENTS
import math

from rcj.utility import rmath


def rsa_generate_key_pair(first_prime: int, second_prime: int):
    if not (rmath.is_prime(first_prime) and rmath.is_prime(second_prime)):
        raise Exception('first_prime or second_prime is not a prime number.')
    if first_prime == second_prime:
        raise Exception('first_prime and second_prime are equal primes.')
    if math.log(first_prime, 10) < 2 or math.log(second_prime, 10) < 2:
        raise Exception('first_prime or second_prime has less than 3 digits.')
