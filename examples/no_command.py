"""Arrrgs custom command absence handler"""
from arrrgs import run, no_command

@no_command()
def print_hello():
    """Prints hello message to current user"""
    print("Hello, user")

if __name__ == "__main__":
    run()
