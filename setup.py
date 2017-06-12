import os
from setuptools import setup

DEPENDENCY_LINKS = [
    "-e git+https://github.com/cormac-yobota/pytest-demo-parent.git@master#egg=pytest-demo-parent"
]
INSTALL_REQUIRES = [
    "pytest-demo-parent",
    "pytest==3.1.1"
]

setup(
    dependency_links=DEPENDENCY_LINKS,
    install_requires=INSTALL_REQUIRES,
    name = "pytest-demo-parent",
    url = "https://github.com/cormac-yobota/pytest-demo-child"
)

