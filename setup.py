from setuptools import setup, find_packages

from Test_pkg import __version__

setup(
    name="MACLC_Test_Functions",
    python_requires=">=3.8",
    packages=find_packages(),
    setup_requires=["wheel"],
    version=__version__,
    description="This is a test package for demo purposes",
    author="Kerianne Hourihan (Mathematica)",
    license="CC0 1.0 Universal"
)