#!/usr/bin/env python3
"""Arrrgs arguments example"""
from arrrgs import command, run


class User:
    """Represents user"""

    def __init__(self, name):
        self._name = name

    def get_name(self):
        """Returns user name"""
        return self._name

@command()
def hello(_, context):
    """Prints hello message to current user"""
    print(f"Hello, {context.get_name()}")

async def prepare(args):
    """Creates app context"""
    context = User("Mikhael")
    return args, context

if __name__ == "__main__":
    run(prepare=prepare)
