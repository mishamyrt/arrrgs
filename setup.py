"""Arrrgs setup script"""
import setuptools

with open(".version", "r", encoding="utf-8") as fh:
    VERSION = ''.join(fh.read().split())

with open("README.md", "r", encoding="utf-8") as fh:
    README = fh.read()

setuptools.setup(
    name="arrrgs",
    version=VERSION,
    author="Mikhael Khrustik",
    description="The library for easily writing feature-rich Python scripts",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=[
        'arrrgs'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
    package_dir={'':'.'},
)
