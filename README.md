# rsa-jpv


![](https://img.shields.io/pypi/v/rsa-jpv?color=%231abc9c&style=flat-square)
![](https://img.shields.io/github/license/jpvitan/rsa-jpv?color=%23f39c12&style=flat-square)


A simple Python library that encrypts your data using the RSA cryptosystem.


![Demo](https://raw.githubusercontent.com/jpvitan/rsa-jpv/master/docs/demo.png)


## Installation
To install the library, open a terminal window and copy the command below.
```
$ pip install rsa-jpv
```
<b><i>Note:</i></b> Requires Python 3.6 or greater.


## Quick Note
Don't use this library to encrypt data in a production environment. This version of RSA is not optimized for such use and may cause security issues which may lead to data loss or theft.


## Documentation


### Application Programming Interface
[Link to API](https://github.com/jpvitan/rsa-jpv/blob/master/docs/api.md)


### Blog
[Link to Blog](https://www.jpvitan.com/blog-read.php?id=1)


### Example


#### Problem
Suppose that you and Bob are exchanging messages over an unencrypted communications channel. Bob informs you that he wants to send you a message that only the two of you should know. Since it's an unencrypted channel, anyone could tap into your communications and see your messages.


#### Solution
The RSA cryptosystem could help solve the problem described above by encrypting the messages sent by Bob to you.


Here's what you need to do:
1. Generate a key pair (public key and private key)
2. Keep the private key a secret (don't let anyone know except yourself)
3. Send the public key to Bob (the public key can't be used to decrypt messages)
4. Tell Bob to use the public key that you've given to encrypt his messages
5. Decrypt the encrypted messages sent by Bob using your private key


##### Generating a Key Pair
Generating a key pair is as easy as calling the ```generate_key_pair()``` function.
```pycon
>>> # Your code
>>> from rcj.cryptosystem import rsa
>>> key_pair = rsa.generate_key_pair()
>>> print(key_pair)
[PUBLIC KEY]
Key Contents:
Prime Product = 221147
Auxiliary = 11

[PRIVATE KEY]
Key Contents:
Prime Product = 221147
Auxiliary = 360131
```
The function returns an instance of type ```KeyPair``` and contains two attributes: ```public_key``` and ```private_key```. As you could see from the example above, calling the print function on the ```KeyPair``` class reveals the content of the ```public_key``` and ```private_key```.


At this point, you could already give Bob the public key by telling him the <b>prime product</b> and <b>auxiliary</b> under the public key section. Always remember to keep your private key a secret!


##### Encrypting Messages
Encrypting a message takes three steps:
1. Creating an instance of the ```Key``` class by using the values of the public key
2. Creating an instance of the ```Encryptor``` class by using the instance of the ```Key``` class we created in the first step
3. Encrypting your message by using the ```encrypt()``` method of the ```Encryptor``` class
```pycon
>>> # Bob's code
>>> from rcj.cryptosystem import rsa
>>> public_key = rsa.Key(221147, 11)
>>> encryptor = rsa.Encryptor(public_key)
>>> encrypted_message = encryptor.encrypt("Let's go to the pub tonight.")
>>> print(encrypted_message)
'ࡾ𨄘𯒭𫨦𗓭𞒅𠴁ਛ𞒅𯒭ਛ𞒅𯒭𒋿𨄘𞒅𫴢ꤸ𴉛𞒅𯒭ਛ𐋲𑯭𠴁𒋿𯒭䗆'
```
Creating an instance of the ```Key``` class takes two parameters: ```prime_product``` and ```auxiliary```. Since we are encrypting in this case, the ```prime_product``` and ```auxiliary``` that we need to pass are those of the public key. Creating an instance of the ```Encryptor``` class takes a single parameter of type ```Key```. In this case, you'll just pass the instance of the ```Key``` class with the values of the public key.


The ```encrypt()``` method of the ```Encryptor``` class takes in a string and returns the encrypted message.


Bob would need to follow the three steps described above to encrypt his message.


##### Decrypting Messages
Decrypting a message takes three steps:
1. Creating an instance of the ```Key``` class by using the values of the private key
2. Creating an instance of the ```Decryptor``` class by using the instance of the ```Key``` class we created in the first step
3. Decrypting your message by using the ```decrypt()``` method of the ```Decryptor``` class
```pycon
>>> # Your code
>>> from rcj.cryptosystem import rsa
>>> private_key = rsa.Key(221147, 360131)
>>> decryptor = rsa.Decryptor(private_key)
>>> message = decryptor.decrypt("ࡾ𨄘𯒭𫨦𗓭𞒅𠴁ਛ𞒅𯒭ਛ𞒅𯒭𒋿𨄘𞒅𫴢ꤸ𴉛𞒅𯒭ਛ𐋲𑯭𠴁𒋿𯒭䗆")
>>> print(message)
"Let's go to the pub tonight."
```


----------------------------------------
Written by Justine Paul Sanchez Vitan.


Copyright © 2021 Justine Paul Sanchez Vitan. All rights reserved.