"""AArgs command"""
from asyncio import iscoroutinefunction
from .parser import command_subparsers

def command(*args, parent=command_subparsers):
    """Decorator to define a new subcommand"""
    def decorator(func):
        parser = parent.add_parser(func.__name__, description=func.__doc__)
        for arg in list(args):
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func, isasync=iscoroutinefunction(func))
    return decorator
