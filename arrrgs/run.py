"""Arrrgs starter"""
import asyncio
from logging import DEBUG
from argparse import Namespace
from typing import Any, Callable, List, Dict, Tuple, Union
from inspect import signature
from .parser import parser
from .log import get_logger

log = get_logger("arrrgs.run")

ContextPreparer = Callable[[Namespace, Any], Tuple[Namespace, Any]]

def run(ctx: Any = None, prepare: Union[ContextPreparer, None] = None, debug=False):
    """Runs application"""
    asyncio.run(async_run(ctx, prepare, debug))

async def async_run(ctx: Any = None, prepare: Union[ContextPreparer, None] = None, debug=False):
    """Runs application asynchronously"""
    parsed_args = parser.parse_args()
    if debug:
        log.setLevel(DEBUG)
        log.info("Running in debug mode")
    log.info(parsed_args)
    if prepare is not None:
        log.info("Running 'prepare' callback")
        (prepared_args, prepared_context) = await _run_safe(prepare, parsed_args, ctx)
        # Updating values
        parsed_args = prepared_args
        ctx = prepared_context
    handler: Callable
    if parsed_args.cmd is None:
        if parsed_args.no_command_handler is None:
            log.info("no_command handler is not found. Printing help")
            parser.print_help()
            return
        handler = parsed_args.no_command_handler
    else:
        handler = parsed_args.func
    await _run_safe(handler, parsed_args, ctx)

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
