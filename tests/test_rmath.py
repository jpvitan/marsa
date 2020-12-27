"""
UNIT TEST SCRIPT
test_rmath.py

LICENSE: GNU General Public License v3 (GPLv3)
Created by Justine Paul Sanchez Vitan.
Copyright © 2020 Justine Paul Sanchez Vitan. All rights reserved.
"""

# IMPORT STATEMENTS
import unittest

from rcj.utility import rmath


class TestRMath(unittest.TestCase):

    def setUp(self):
        self.in_test_is_prime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.ex_out_test_is_prime = [False, False, True, True, False, True, False, True, False, False, False, True,
                                     False, True, False, False]

        self.in_gcd = [(6, 8), (6, 9), (11, 17), (45, 83), (120, 130), (365, 910)]
        self.ex_out_gcd = [2, 3, 1, 1, 10, 5]

        self.in_gcd_linear_combination = self.in_gcd
        self.ex_out_gcd_linear_combination = [(15, -11), (17, -11), (31, -20), (24, -13), (259, -239), (5, -2)]

        self.in_find_number_relatively_prime = [4, 15, 23, 56, 98, 102, 114, 109, 156, 210]
        self.ex_out_find_number_relatively_prime = [3, 4, 3, 3, 3, 5, 5, 3, 5, 11]

        self.in_generate_prime_number_list = (2, 47)
        self.ex_out_generate_prime_number_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    def tearDown(self):
        pass

    def test_is_prime(self):
        for i in range(0, len(self.in_test_is_prime)):
            self.assertEqual(rmath.is_prime(self.in_test_is_prime[i]), self.ex_out_test_is_prime[i])

    def test_gcd(self):
        for i in range(0, len(self.in_gcd)):
            self.assertEqual(rmath.gcd(self.in_gcd[i][0], self.in_gcd[i][1]), self.ex_out_gcd[i])

    def test_gcd_linear_combination(self):
        for i in range(0, len(self.in_gcd_linear_combination)):
            self.assertEqual(rmath.gcd_linear_combination(self.in_gcd_linear_combination[i][0],
                                                          self.in_gcd_linear_combination[i][1]),
                             self.ex_out_gcd_linear_combination[i])

    def test_find_number_relatively_prime(self):
        for i in range(0, len(self.in_find_number_relatively_prime)):
            self.assertEqual(rmath.find_number_relatively_prime(self.in_find_number_relatively_prime[i]),
                             self.ex_out_find_number_relatively_prime[i])

    def test_generate_prime_number_list(self):
        self.assertEqual(rmath.generate_prime_number_list(self.in_generate_prime_number_list),
                         self.ex_out_generate_prime_number_list)


if __name__ == "__main__":
    unittest.main()
