"""Arrrgs command"""
from argparse import ArgumentParser
from typing import Callable, Tuple

from .arguments import add_args
from .parser import command_subparsers, parser


def register_handler(
    parent: ArgumentParser,
    func: Callable,
    args: Tuple[str, ...],
    name:str=None
):
    """Add new command handler to parser"""
    if name is not None:
        command_name = name
    else:
        command_name = func.__name__
    cmd_parser = parent.add_parser(command_name, description=func.__doc__)
    add_args(cmd_parser, args)
    cmd_parser.set_defaults(func=func)

def command(*args, name:str=None, root=False, parent=command_subparsers, root_parser=parser):
    """Decorator to define a new command"""
    def decorator(func):
        if root:
            root_parser.set_defaults(
                root_command_handler=func,
                root_command_args=list(args),
            )
        register_handler(parent, func, args, name)
    return decorator
