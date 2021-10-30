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


def lcd(x: int, y: int):
    return x * y // gcd(x, y)


def find_number_relatively_prime(x: int, starting_number=3) -> int:
    y = starting_number
    while True:
        if gcd(y, x) == 1:
            break
        y = y + 1
    return y


def generate_prime_candidate(size: int) -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
              349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
              467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
              613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
              751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
              887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031,
              1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151,
              1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279,
              1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423,
              1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523,
              1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627,
              1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777,
              1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907,
              1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039]

    lower_bound = 2 ** (size - 1) + 1
    upper_bound = 2 ** size - 1

    if lower_bound <= primes[len(primes) - 1]:
        raise Exception("Size is too small!")

    while True:
        prime_candidate = random.randint(lower_bound, upper_bound)
        prime_candidate_is_composite = False

        for prime in primes:
            if prime_candidate % prime == 0:
                prime_candidate_is_composite = True
                break

        if prime_candidate_is_composite:
            continue
        return prime_candidate


def generate_prime_number_list(prime_range=(2, 1021), size: int = None, shuffle=False) -> list:
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
