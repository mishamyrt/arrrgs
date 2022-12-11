"""Arrrgs arguments"""
from typing import Tuple, Dict, Any
from .parser import parser

def arg(*name_or_flags: Tuple[str, ...], **kwargs: Dict[str, Any]) -> None:
    """Convenience function to properly format arguments
    to pass to the subcommand decorator."""
    return (list(name_or_flags), kwargs)

def global_args(*args: Tuple[str, ...]) -> None:
    """Adds global arguments to app"""
    for argument in list(args):
        parser.add_argument(*argument[0], **argument[1])
