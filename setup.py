from setuptools import setup, find_packages

from Test_pkg.Test_module import __version__

setup(
    name="MACLC_Test_Functions",
    python_requires=">=3.8",
    packages=find_packages(),
    version=__version__,
    description="This is a test package for demo purposes",
    author="Kerianne Hourihan (Mathematica)"
)