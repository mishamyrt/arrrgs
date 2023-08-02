#!/usr/bin/env python3
"""A script that prints out information about the system"""
from os import getcwd, getenv, getlogin

from arrrgs import arg, command, run


@command()
def user():
    """Prints current user name"""
    print(getlogin())

@command()
async def cwd():
    """Prints current working directory"""
    print(getcwd())

@command(arg("name", help="variable name"))
def variable(args):
    """Prints environment variable"""
    print(getenv(args.name))

if __name__ == "__main__":
    run()
