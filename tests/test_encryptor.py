"""
UNIT TEST SCRIPT
test_encryptor.py

LICENSE: GNU General Public License v3 (GPLv3)
Created by Justine Paul Sanchez Vitan.
Copyright © 2020 Justine Paul Sanchez Vitan. All rights reserved.
"""

# IMPORT STATEMENTS
import unittest

from rcj.cryptosystem import rsa


class TestEncryptor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_encrypt(self):
        public_key = rsa.Key(221147, 11)
        encryptor = rsa.Encryptor(public_key)
        encrypted_message = encryptor.encrypt("Let's go to the pub tonight.")
        self.assertEqual('ࡾ𨄘𯒭𫨦𗓭𞒅𠴁ਛ𞒅𯒭ਛ𞒅𯒭𒋿𨄘𞒅𫴢ꤸ𴉛𞒅𯒭ਛ𐋲𑯭𠴁𒋿𯒭䗆', encrypted_message)


if __name__ == "__main__":
    unittest.main()
