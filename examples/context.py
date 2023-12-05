#!/usr/bin/env python3
"""Arrrgs arguments example"""
from arrrgs import command, run


class User:
    """Represents user"""

    def say_hello(self):
        print(f"Hello, {self._name}!")

    def say_bye(self):
        print(f"Bye, {self._name}!")

    def __init__(self, name):
        self._name = name

    def get_name(self):
        """Returns user name"""
        return self._name

@command()
def hello(_, user: User):
    """Prints hello message to current user"""
    user.say_hello()

async def say_bye(_, user: User):
    """Prints bye message to current user"""
    user.say_bye()

async def prepare(args):
    """Creates app context"""
    return args, User("Mikhael")

if __name__ == "__main__":
    run(
        prepare=prepare,
        after=say_bye
    )
