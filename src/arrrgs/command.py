"""Arrrgs command"""
from .arguments import add_args
from .parser import command_subparsers, parser


def command(*args, name:str=None, parent=command_subparsers):
    """Decorator to define a new command"""
    def decorator(func):
        if name is not None:
            command_name = name
        else:
            command_name = func.__name__
        cmd_parser = parent.add_parser(command_name, description=func.__doc__)
        add_args(cmd_parser, args)
        cmd_parser.set_defaults(func=func)
    return decorator

def root_command(*args):
    """Decorator to define a command absence handler"""
    def decorator(func):
        parser.set_defaults(
            root_command_handler=func,
            root_command_args=list(args),
        )
    return decorator
