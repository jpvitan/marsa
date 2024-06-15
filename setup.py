"""

MARSA
A Python library that lets you experiment with the mathematics of the Rivest–Shamir–Adleman (RSA) cryptosystem.

This project is under the MIT license.

Copyright © 2024 Justine Paul Vitan. All rights reserved.

License Information: https://github.com/jpvitan/marsa/blob/master/LICENSE
Developer's Website: https://jpvitan.com/

"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="marsa",
    version="1.0.0",
    author="Justine Paul Vitan",
    author_email="justinepaulvitan5@gmail.com",
    description=(
        "A Python library that lets you experiment with the "
        "mathematics of the Rivest–Shamir–Adleman (RSA) cryptosystem."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jpvitan/marsa",
    packages=["marsa"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
