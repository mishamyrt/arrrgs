"""Arrrgs starter"""
import asyncio
from argparse import Namespace
from inspect import signature
from logging import DEBUG
from typing import Any, Callable, Dict, List, Tuple, Union

from .arguments import add_args
from .log import get_logger
from .parser import parser

log = get_logger("arrrgs.run")

ContextPreparer = Callable[[Namespace, Any], Tuple[Namespace, Any]]

def run(ctx: Any = None, prepare: Union[ContextPreparer, None] = None, debug=False):
    """Runs application"""
    asyncio.run(async_run(ctx, prepare, debug))

async def async_run(ctx: Any = None, prepare: Union[ContextPreparer, None] = None, debug=False):
    """Runs application asynchronously"""
    args, argv = parser.parse_known_args()
    if debug:
        log.setLevel(DEBUG)
        log.info("Running in debug mode")
    handler: Callable
    if args.cmd is None:
        if args.root_command_handler is None:
            log.info("root command handler is not found. Printing help")
            parser.print_help()
            return
        add_args(parser, args.root_command_args)
        args = parser.parse_args()
        handler = args.root_command_handler
    else:
        if argv:
            parser.error(f"unrecognized arguments: {' '.join(argv)}")
        handler = args.func
        if prepare is not None:
            log.info("Running 'prepare' callback")
            (prepared_args, prepared_context) = await _run_safe(prepare, args, ctx)
            # Updating values
            args = prepared_args
            ctx = prepared_context
    log.info(args)
    await _run_safe(handler, args, ctx)

def _prepare_args(handler: Callable, parsed_args: Namespace, ctx: Any) -> List[str]:
    sig = signature(handler)
    params_count = len(sig.parameters)
    args = []
    if params_count >= 1:
        args.append(parsed_args)
    if params_count >= 2:
        args.append(ctx)
    return args

async def _run_safe(handler: Callable, parsed_args: Dict[str, Any], ctx: Any):
    args = _prepare_args(handler, parsed_args, ctx)
    return await _run_async_safe(handler, args)

async def _run_async_safe(handler: Callable, args: List[any]):
    if asyncio.iscoroutinefunction(handler):
        return await handler(*args)
    return handler(*args)
