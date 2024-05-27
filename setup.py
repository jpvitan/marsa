"""

MARSA
A Python library that lets you experiment with the mathematics of the Rivest–Shamir–Adleman (RSA) cryptosystem.

This project is under the MIT license.
Please read the terms and conditions stated within the license before attempting any modification or distribution of the software.

Copyright © 2024 Justine Paul Vitan. All rights reserved.

License Information: https://github.com/jpvitan/marsa/blob/master/LICENSE
Developer's Website: https://jpvitan.com/

"""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rsa-jpv',
    version='1.0.3',
    author='Justine Paul Sanchez Vitan',
    author_email='justinepaulvitan5@gmail.com',
    description='A 2048-bit RSA library that operates solely on integers.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jpvitan/rsa-jpv',
    packages=['rcj', 'rcj.cryptosystem', 'rcj.utility'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
