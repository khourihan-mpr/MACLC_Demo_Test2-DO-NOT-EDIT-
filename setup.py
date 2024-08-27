from setuptools import setup, find_packages

from Test_pkg.Test_module import __version__

setup(
    name="My Package",
    python_requires=">=3.8",
    packages=find_packages(),
    version=__version__,
    description="This is a description of my package",
    author="My name"
)