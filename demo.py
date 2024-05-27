"""

MARSA
A Python library that lets you experiment with the mathematics of the Rivest–Shamir–Adleman (RSA) cryptosystem.

This project is under the MIT license.
Please read the terms and conditions stated within the license before attempting any modification or distribution of the software.

Copyright © 2024 Justine Paul Vitan. All rights reserved.

License Information: https://github.com/jpvitan/marsa/blob/master/LICENSE
Developer's Website: https://jpvitan.com/

"""

# IMPORT STATEMENTS
from rcj.cryptosystem import rsa

first_message = 1024
second_message = 2048

key_pair = rsa.generate_key_pair()  # Generate a key pair (public key and private key).
print(key_pair)

encryptor = rsa.Encryptor(key_pair.public_key)  # Create an instance of the Encryptor class by using the public key.
first_encrypted_message = encryptor.encrypt(first_message)  # Encrypt the first message.
second_encrypted_message = encryptor.encrypt(second_message)  # Encrypt the second message.

decryptor = rsa.Decryptor(key_pair.private_key)  # Create an instance of the Decryptor class by using the private key.
first_decrypted_message = decryptor.decrypt(first_encrypted_message)  # Decrypt the first message.
second_decrypted_message = decryptor.decrypt(second_encrypted_message)  # Decrypt the second message.

print("Encrypted message 1:", first_encrypted_message)
print("Encrypted message 2:", second_encrypted_message)
print("Decrypted message 1:", first_decrypted_message)
print("Decrypted message 2:", second_decrypted_message)
