**MARSA** is a Python library that lets you experiment with the mathematics of the Rivest–Shamir–Adleman (RSA) cryptosystem.


![Badge](https://img.shields.io/github/license/jpvitan/marsa)
![Badge](https://img.shields.io/badge/code%20style-black-000000.svg)


## 📋 Quick Guide


### Installation


You can install **MARSA** using pip. Simply run the following command in your terminal or command prompt:


```
pip install
```


### Key Generation


To generate a key pair, import the `rsa` module from the `marsa` package and create an instance of the `KeyPair` class:


```python
from marsa import rsa

key_pair = rsa.KeyPair()
```


### Encryption


To encrypt, create an instance of the `Encryptor` class with the public key from your `KeyPair` object and use the `encrypt()` method:


```python
encryptor = rsa.Encryptor(key_pair.public_key)
secret_message = encryptor.encrypt(message)
```


If you don't have access to the `KeyPair` object, you can manually create a key by using the `Key` class and passing in the required parameters:


```python
public_key = rsa.Key(product, exponent)
```


## 🛠️ Software


### Developer


Built by [Justine Paul Vitan](https://jpvitan.com) as a solo project to demonstrate his knowledge in cryptography and number theory. The source code of this project is open and available to the public via GitHub for transparency and open-source collaboration.


### License


This project is under the [MIT license](https://github.com/jpvitan/marsa/blob/master/LICENSE). Please read the terms and conditions stated within the license before attempting any modification or distribution of the software.