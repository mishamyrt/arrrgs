#!/usr/bin/env python3
"""Basic Arrrgs example"""
from os import getlogin

from arrrgs import command, run


@command()
def hello():
    """Prints hello message to current user"""
    print(f"Hello, {getlogin()}")

if __name__ == "__main__":
    run()
