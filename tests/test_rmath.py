"""
UNIT TEST SCRIPT
test_rmath.py

LICENSE: GNU General Public License v3 (GPLv3)
Created by Justine Paul Sanchez Vitan.
Copyright © 2021 Justine Paul Sanchez Vitan. All rights reserved.
"""

# IMPORT STATEMENTS
import unittest

from rcj.utility import rmath


class TestRMath(unittest.TestCase):

    def setUp(self):
        self.in_gcd = [(6, 8), (6, 9), (11, 17), (45, 83), (120, 130), (365, 910)]
        self.ex_out_gcd = [2, 3, 1, 1, 10, 5]

        self.in_gcd_linear_combination = self.in_gcd
        self.ex_out_gcd_linear_combination = [(-1, 1), (-1, 1), (-3, 2), (24, -13), (-1, 1), (5, -2)]

        self.in_lcd = [(6, 8), (6, 9), (11, 17), (45, 83), (120, 130), (365, 910)]
        self.ex_out_lcd = [24, 18, 187, 3735, 1560, 66430]

    def tearDown(self):
        pass

    def test_gcd(self):
        for i in range(0, len(self.in_gcd)):
            self.assertEqual(rmath.gcd(self.in_gcd[i][0], self.in_gcd[i][1]), self.ex_out_gcd[i])

    def test_gcd_linear_combination(self):
        for i in range(0, len(self.in_gcd_linear_combination)):
            self.assertEqual(rmath.gcd_linear_combination(self.in_gcd_linear_combination[i][0],
                                                          self.in_gcd_linear_combination[i][1]),
                             self.ex_out_gcd_linear_combination[i])

    def test_lcd(self):
        for i in range(0, len(self.in_lcd)):
            self.assertEqual(rmath.lcd(self.in_lcd[i][0], self.in_lcd[i][1]), self.ex_out_lcd[i])


if __name__ == "__main__":
    unittest.main()
