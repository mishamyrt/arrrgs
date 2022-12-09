# Arrrgs [![PyPI version](https://badge.fury.io/py/arrrgs.svg)](https://pypi.org/project/arrrgs/)

<img align="right" width="104px" height="176px"
     alt="Logo"
     src="./assets/logo@2x.png">

The library for easily writing feature-rich Python scripts. Uses the built-in `argparse` module for parsing.

* Simple API
* Automatic async support
* Small size

## Installing

```sh
pip install arrrgs
```

## Usage

### Basic

To declare a command, write a function and add the `command` decorator to it. To start command processing, call the function `run`.

```py
from arrrgs import command, run
from os import getlogin

@command()
def hello():
    """Prints hello message to current user"""
    print(f"Hello, {getlogin()}")

if __name__ == "__main__":
    run()
```

Arrrgs will process the command and show the user the result. The help message will be generated from the function documentation.

```sh
python examples/basic.py hello --help
# usage: basic.py hello [-h]

# Prints hello message to current user

# optional arguments:
#   -h, --help  show this help message and exit
```

### Arguments

To add arguments you need to pass their description to the decorator arguments. The available parameters are the same as [for `add_argument` in `argparse`](https://docs.python.org/3/library/argparse.html#quick-links-for-add-argument).

```py
from arrrgs import command, arg, run

@command(
    arg("name", help="User name"),
    arg("--rage", "-r", action='store_true', help="Rage mod"),
)
def hello(args):
    """Prints hello message to current user"""
    user_name = args.name
    if args.rage:
        user_name = user_name.upper()
    print(f"Hello, {user_name}")

if __name__ == "__main__":
    run()
```

### Context

Sometimes all the teams in an application need a common entity that they interact with. Commands have a context for that. The context value is set when the function `run` is called.

```py
from arrrgs import command, run

class User:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        """Returns user name"""
        return self._name

@command()
def hello(_, context):
    """Prints hello message to current user"""
    print(f"Hello, {context.get_name()}")

if __name__ == "__main__":
    user = User("Mikhael")
    run(user)
```

### Async

To execute the command in an asynchronous context, simply add the `async` keyword in the function declaration.

```py
@command()
async def hello():
    """Prints hello message to current user"""
    print("Hello, async user")
```