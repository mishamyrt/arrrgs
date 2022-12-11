"""Arrrgs command"""
from .parser import command_subparsers, parser

def command(*args, parent=command_subparsers):
    """Decorator to define a new subcommand"""
    def decorator(func):
        cmd_parser = parent.add_parser(func.__name__, description=func.__doc__)
        for arg in list(args):
            cmd_parser.add_argument(*arg[0], **arg[1])
        cmd_parser.set_defaults(func=func)
    return decorator

def no_command():
    """Decorator to define a command absence handler"""
    def decorator(func):
        parser.set_defaults(no_command_handler=func)
    return decorator
