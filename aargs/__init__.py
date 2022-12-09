"""AArgs library"""
import asyncio
from typing import Any
from inspect import signature, iscoroutine
from .parser import cli
from .command import command
from .argument import arg

def run(context: Any = None):
    """Runs application"""
    parsed_args = cli.parse_args()
    if parsed_args.cmd is None:
        cli.print_help()
    else:
        # Fill arguments
        params = signature(parsed_args.func).parameters
        params_count = len(params)
        args = []
        if params_count >= 1:
            args.append(parsed_args)
        if params_count >= 2:
            args.append(context)
        # Run function
        if parsed_args.isasync:
            asyncio.run(parsed_args.func(*args))
        else:
            parsed_args.func(*args)
