# rsa-jpv


A simple Python library that encrypts your data using the RSA cryptosystem.
```python
>>> from rcj.cryptosystem import rsa
>>> key_pair = rsa.generate_key_pair()
>>> encryptor = rsa.Encryptor(key_pair.public_key)
>>> encrypted_message = encryptor.encrypt("I love you!")
>>> encrypted_message
'𢍺𐱽灭ߺ梬𡖉𐱽𘍇ߺ𡆾ꧣ'
>>> decryptor = rsa.Decryptor(key_pair.private_key)
>>> message = decryptor.decrypt(encrypted_message)
>>> message
'I love you!'
```

## Latest Release
### v0.0.1
* Initial release


To view the full changelog, [click here](https://github.com/jpvitan/rsa-jpv/blob/master/CHANGELOG.md).

## Installation
To install the library, open a terminal window and copy the command below:
```
$ pip install rsa-jpv
```
<b><i>Note:</i></b> Requires Python 3.6 or greater.

## Quick Note
While this Python library is capable of encrypting data using the RSA cryptosystem, I would highly advise against using this to encrypt <b>extremely critical and sensitive data</b>. The RSA that is used in practice operates on extremely large numbers, which as of the moment, this library isn't designed to handle.

## Documentation
* [API Documentation](https://github.com/jpvitan/rsa-jpv/blob/master/docs/api.md)

### A Simple Example
#### Problem
Suppose that you and Bob are exchanging messages over an unsecure communications channel. Bob informs you that he wants to send you a message that only you and him should know. Since it's an unsecure channel, anyone could tap into your communications and see your messages.

#### Solution
The RSA cryptosystem could help solve the problem described above by encrypting the messages sent by Bob to you.


Here's what you need to do:
1. Generate a key pair (public key and private key)
2. Keep the private key a secret (don't let anyone know except yourself)
3. Send the public key to Bob (the public key can't be used to decrypt messages)
4. Tell Bob to use the public key that you've given to encrypt his messages
5. Decrypt the encrypted messages sent by Bob using your private key


The following sections will show you how it's done.

#### Generating a Key Pair
Generating a key pair is as easy as calling the ```generate_key_pair()``` function.
```python
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

#### Encrypting Messages
Encrypting a message takes three steps:
1. Creating an instance of the ```Key``` class by using the values of the public key
2. Creating an instance of the ```Encryptor``` class by using the instance of the ```Key``` class we created in the first step
3. Encrypting your message by using the ```encrypt()``` method of the ```Encryptor``` class.
```python
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


Bob would need to follow the three steps described above to successfully encrypt his messages. Once Bob does that, he is now ready to send his encrypted message to you.

#### Decrypting Messages
Decrypting a message takes three steps:
1. Creating an instance of the ```Key``` class by using the values of the private key
2. Creating an instance of the ```Decryptor``` class by using the instance of the ```Key``` class we created in the first step
3. Decrypting your message by using the ```decrypt()``` method of the ```Decryptor``` class.
```python
>>> # Your code
>>> from rcj.cryptosystem import rsa
>>> private_key = rsa.Key(221147, 360131)
>>> decryptor = rsa.Decryptor(private_key)
>>> message = decryptor.decrypt("ࡾ𨄘𯒭𫨦𗓭𞒅𠴁ਛ𞒅𯒭ਛ𞒅𯒭𒋿𨄘𞒅𫴢ꤸ𴉛𞒅𯒭ਛ𐋲𑯭𠴁𒋿𯒭䗆")
>>> print(message)
"Let's go to the pub tonight."
```
The steps for decrypting a message is very similar to the steps of encrypting a message. The only difference is that the public key is replaced with the private key and the ```Encryptor``` class is replaced with the ```Decryptor``` class.

----------------------------------------
Written by Justine Paul Sanchez Vitan.


Copyright © 2020 Justine Paul Sanchez Vitan. All rights reserved.
