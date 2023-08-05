#!/usr/bin/env python3
"""Arrrgs root command handler"""
from arrrgs import arg, command, run


@command(
    arg("--rage", "-r", action='store_true', help="Rage mod"),
    root=True
)
def hello(args, name: str):
    """Prints hello message to current user"""
    message = f"Hello, {name}"
    if args.rage:
        message = message.upper()
    print(message)

@command()
def bye(_, name: str):
    """Prints bye message to current user"""
    print(f"Bye, {name}")

async def prepare(args):
    """Creates app context"""
    return args, "Mikhael"

if __name__ == "__main__":
    run(prepare=prepare)
