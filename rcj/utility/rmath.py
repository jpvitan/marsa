"""
rcj.utility.rmath
rmath.py

LICENSE: GNU General Public License v3 (GPLv3)
Created by Justine Paul Sanchez Vitan.
Copyright © 2020 Justine Paul Sanchez Vitan. All rights reserved.
"""

# IMPORT STATEMENTS
import math
import random


def power_modulo(base, exponent, divisor) -> int:
    if exponent < 10:
        return base ** exponent % divisor
    quotient = exponent // 2
    remainder = exponent % 2
    return (power_modulo(base, remainder + quotient, divisor) * power_modulo(base, quotient, divisor)) % divisor


def is_prime(x: int) -> bool:
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def gcd(x: int, y: int) -> int:
    if x > y:
        temp = y
        y = x
        x = temp
    if x == 0:
        return y

    while True:
        r = y % x
        if r == 0:
            break
        y = x
        x = r
    return x


def gcd_linear_combination(x: int, y: int) -> tuple:
    if x > y:
        temp = y
        y = x
        x = temp
    if x == 0:
        return y

    original_x = x
    original_y = y

    coefficient_list = []
    coefficient_list.append((0, 1))
    coefficient_list.append((1, -int(y / x)))

    iteration = 1

    while True:
        r = y % x
        if r == 0:
            break

        if iteration != 1:
            quotient = int(y / x)
            a = int(coefficient_list[iteration - 2][0] - (coefficient_list[iteration - 1][0] * quotient))
            b = int(coefficient_list[iteration - 2][1] - (coefficient_list[iteration - 1][1] * quotient))
            coefficient_list.append((a, b))

        y = x
        x = r
        iteration = iteration + 1

    a = coefficient_list[-1][1]
    b = coefficient_list[-1][0]

    if a < 0:
        i = 2
        while True:
            a_candidate = a + i * original_y
            b_candidate = b - i * original_x

            if a_candidate > 0:
                a = a_candidate
                b = b_candidate
                break
            i = i + 1
    return a, b


def find_number_relatively_prime(x: int, starting_number=3) -> int:
    y = starting_number
    while True:
        if gcd(y, x) == 1:
            break
        y = y + 1
    return y


def generate_prime_number_list(prime_range=(101, 997), size: int = None, shuffle=False) -> list:
    min_number = prime_range[0]
    max_number = prime_range[1]

    if min_number > max_number:
        temp = min_number
        min_number = max_number
        max_number = temp

    prime_number_list = list(range(2, max_number + 1))
    for i in prime_number_list:
        for j in prime_number_list:
            if i == j:
                continue
            if j % i == 0:
                prime_number_list.remove(j)

    while True:
        if prime_number_list[0] < min_number:
            prime_number_list.remove(prime_number_list[0])
            continue
        break

    if shuffle:
        random.shuffle(prime_number_list)

    if size is None:
        return prime_number_list

    return prime_number_list[:size]
