# rsa-jpv


## API Documentation


### class Key
A class that holds the prime product and auxiliary value.


#### Class Parameters
| Parameter     | Type | Description                                    |
|---------------|------|------------------------------------------------|
| prime_product | int  | The product of two primes                      |
| auxiliary     | int  | Exponent of the encrypted or decrypted message |


----------------------------------------
### class KeyPair
A class that holds the public key and private key.


#### Class Parameters
| Parameter   | Type | Description     |
|-------------|------|-----------------|
| public_key  | Key  | The public key  |
| private_key | Key  | The private key |


----------------------------------------
### class Encryptor
A class that encrypts data based on the key parameter.


#### Class Parameters
| Parameter  | Type | Description    |
|------------|------|----------------|
| public_key | Key  | The public key |


#### Functions


##### encrypt
A method that takes an integer and encrypts it.
```python
encrypt(self, message: int) -> int
```


----------------------------------------
### class Decryptor
A class that decrypts data based on the key parameter.


#### Class Parameters
| Parameter   | Type | Description     |
|-------------|------|-----------------|
| private_key | Key  | The private key |


#### Functions


##### decrypt
A method that takes an integer and decrypts it.
```python
decrypt(self, message: int) -> int
```


----------------------------------------
### def generate_key_pair
A function that generates a public key and private key.
```python
generate_key_pair() -> KeyPair
```


----------------------------------------
Written by Justine Paul Sanchez Vitan.


Copyright © 2021 Justine Paul Sanchez Vitan. All rights reserved.