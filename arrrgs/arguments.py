"""Arrrgs arguments"""
from typing import List
from .parser import cli

def arg(*name_or_flags: List[str], **kwargs):
    """Convenience function to properly format arguments
    to pass to the subcommand decorator."""
    return (list(name_or_flags), kwargs)

def global_args(*args):
    """Adds global arguments to app"""
    for argument in list(args):
        cli.add_argument(*argument[0], **argument[1])
