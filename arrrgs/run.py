"""Arrrgs starter"""
import asyncio
from logging import DEBUG
from typing import Any, Callable, List, Dict
from inspect import signature
from .parser import parser
from .log import get_logger

log = get_logger("arrrgs.run")

def _run_async_safe(handler: Callable, args: List[any]):
    if asyncio.iscoroutinefunction(handler):
        asyncio.run(handler(*args))
    else:
        handler(*args)

def _run_handler(handler: Callable, parsed_args: Dict[str, Any], context: Any):
    sig = signature(handler)
    params_count = len(sig.parameters)
    args = []
    if params_count >= 1:
        args.append(parsed_args)
    if params_count >= 2:
        args.append(context)
    _run_async_safe(handler, args)

def run(context: Any = None, debug=False):
    """Runs application"""
    parsed_args = parser.parse_args()
    if debug:
        log.setLevel(DEBUG)
        log.info("Running in debug mode")
    log.info(parsed_args)
    handler: Callable
    if parsed_args.cmd is None:
        if parsed_args.no_command_handler is None:
            log.info("no_command handler is not found. Printing help")
            parser.print_help()
            return
        else:
            handler = parsed_args.no_command_handler
    else:
        handler = parsed_args.func
    _run_handler(handler, parsed_args, context)
