"""
rcj.utility.rmath
rmath.py

LICENSE: GNU General Public License v3 (GPLv3)
Created by Justine Paul Sanchez Vitan.
Copyright © 2021 Justine Paul Sanchez Vitan. All rights reserved.
"""

# IMPORT STATEMENTS
import random


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

        passed_rabin_miller = True
        for i in range(4):
            if not rabin_miller(prime_candidate):
                passed_rabin_miller = False
                break
        if not passed_rabin_miller:
            continue

        return prime_candidate


def rabin_miller(p: int) -> bool:
    a = random.randint(1, p - 1)
    s = 0
    t = p - 1
    while t % 2 == 0:
        s = s + 1
        t = t // 2
    modulo_result = pow(a, t, p)
    if modulo_result == 1 or modulo_result == p - 1:
        return True
    for i in range(1, s):
        modulo_result = pow(a, 2 ** i * t, p)
        if modulo_result == p - 1:
            return True
    return False


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

    a_last = 0
    b_last = 1
    a = 1
    b = -(y // x)

    iteration = 1

    while True:
        r = y % x
        if r == 0:
            break

        if iteration != 1:
            quotient = y // x
            a_temp = a
            b_temp = b
            a = a_last - (a * quotient)
            b = b_last - (b * quotient)
            a_last = a_temp
            b_last = b_temp

        y = x
        x = r
        iteration = iteration + 1

    temp = a
    a = b
    b = temp

    return a, b


def lcd(x: int, y: int) -> int:
    return x * y // gcd(x, y)
