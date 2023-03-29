"""Arrrgs argument parser"""
from argparse import ArgumentParser

parser = ArgumentParser()
parser.set_defaults(
    root_command_handler=None,
    root_command_args=None,
)
command_subparsers = parser.add_subparsers(dest="cmd")
