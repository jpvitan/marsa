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
A method that takes a string and encrypts it.
```python
encrypt(self, message: str) -> str
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
A method that takes a string and decrypts it.
```python
decrypt(self, message: str) -> str
```


----------------------------------------
### def generate_key_pair
A function that generates a public key and private key.
```python
generate_key_pair(first_prime: int=None, second_prime: int=None) -> KeyPair
```

#### Function Parameters
| Parameter         | Type | Description             |
|-------------------|------|-------------------------|
| first_prime=None  | int  | The first prime number  |
| second_prime=None | int  | The second prime number |


If no parameters are specified, the function will automatically generate primes for you. It is recommended that you leave the parameters by their default values.

----------------------------------------
Written by Justine Paul Sanchez Vitan.


Copyright © 2021 Justine Paul Sanchez Vitan. All rights reserved.
