import os
from setuptools import setup

INSTALL_REQUIRES = [
    "pytest==3.1.1"
]
VERSION="0.1.0"

setup(
    version=VERSION,
    install_requires=INSTALL_REQUIRES,
    name = "pytest-demo-parent",
    url = "https://github.com/cormac-yobota/pytest-demo-parent"
)

