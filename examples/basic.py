"""Basic AArgs example"""
from os import getlogin
from aargs import command, run

@command()
def hello():
    """Prints hello message to current user"""
    print(f"Hello, {getlogin()}")

if __name__ == "__main__":
    run()
