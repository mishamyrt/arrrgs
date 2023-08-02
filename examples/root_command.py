#!/usr/bin/env python3
"""Arrrgs root command handler"""
from arrrgs import arg, command, run


@command(
    arg("--rage", "-r", action='store_true', help="Rage mod"),
    root=True
)
def hello(args):
    """Prints hello message to current user"""
    message = "Hello, user"
    if args.rage:
        message = message.upper()
    print(message)

@command()
def bye():
    """Prints bye message to current user"""
    print("Bye, user")

if __name__ == "__main__":
    run(debug=True)
