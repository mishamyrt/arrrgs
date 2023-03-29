"""Arrrgs arguments"""
from argparse import ArgumentParser
from typing import Any, Dict, Tuple

from .parser import parser


def arg(*name_or_flags: Tuple[str, ...], **kwargs: Dict[str, Any]) -> None:
    """Convenience function to properly format arguments
    to pass to the subcommand decorator."""
    return (list(name_or_flags), kwargs)

def global_args(*args: Tuple[str, ...]) -> None:
    """Adds global arguments to app"""
    add_args(parser, args)

def add_args(_parser: ArgumentParser, args: Tuple[str, ...]) -> None:
    """Adds arguments to the parser"""
    for argument in list(args):
        _parser.add_argument(*argument[0], **argument[1])
