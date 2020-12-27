"""
setup
setup.py

LICENSE: GNU General Public License v3 (GPLv3)
Created by Justine Paul Sanchez Vitan.
Copyright © 2020 Justine Paul Sanchez Vitan. All rights reserved.
"""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rsa-jpv',
    version='0.0.1',
    author='Justine Paul Sanchez Vitan',
    author_email='justinepaulvitan5@gmail.com',
    description='A simple Python library that encrypts your data using the RSA cryptosystem.',
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
