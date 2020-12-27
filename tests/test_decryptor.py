"""
UNIT TEST SCRIPT
test_decryptor.py

LICENSE: GNU General Public License v3 (GPLv3)
Created by Justine Paul Sanchez Vitan.
Copyright © 2020 Justine Paul Sanchez Vitan. All rights reserved.
"""

# IMPORT STATEMENTS
import unittest

from rcj.cryptosystem import rsa


class TestDecryptor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_decrypt(self):
        private_key = rsa.Key(221147, 360131)
        decryptor = rsa.Decryptor(private_key)
        message = decryptor.decrypt("ࡾ𨄘𯒭𫨦𗓭𞒅𠴁ਛ𞒅𯒭ਛ𞒅𯒭𒋿𨄘𞒅𫴢ꤸ𴉛𞒅𯒭ਛ𐋲𑯭𠴁𒋿𯒭䗆")
        self.assertEqual("Let's go to the pub tonight.", message)


if __name__ == "__main__":
    unittest.main()
