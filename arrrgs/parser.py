"""Arrrgs argument parser"""
from argparse import ArgumentParser

parser = ArgumentParser()
parser.set_defaults(no_command_handler=None)
command_subparsers = parser.add_subparsers(dest="cmd")
