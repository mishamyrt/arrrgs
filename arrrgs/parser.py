"""AArg argument parser"""
from argparse import ArgumentParser

parser = ArgumentParser()
command_subparsers = parser.add_subparsers(dest="cmd")
