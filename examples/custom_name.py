#!/usr/bin/env python3
"""Basic Arrrgs example"""
from arrrgs import command, run


@command(name="list")
def list_numbers():
    """Prints list of numbers"""
    print("1, 2, 3")

if __name__ == "__main__":
    run()
