"""AArg argument parser"""
from argparse import ArgumentParser

cli = ArgumentParser()
command_subparsers = cli.add_subparsers(dest="cmd")
