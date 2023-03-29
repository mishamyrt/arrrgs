# Arrrgs [![PyPI version](https://badge.fury.io/py/arrrgs.svg)](https://pypi.org/project/arrrgs/) [![Quality assurance](https://github.com/mishamyrt/arrrgs/actions/workflows/qa.yaml/badge.svg)](https://github.com/mishamyrt/arrrgs/actions/workflows/qa.yaml)

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

### Custom command absence handler

Use the `root_command` decorator to set up a no-command handler. The same rules apply to this function as to normal command handlers except that it cannot have its own arguments.

```py
from arrrgs import run, root_command

@root_command()
def print_hello():
    """Prints hello message to current user"""
    print("Hello, user")

if __name__ == "__main__":
    run()
```


### Arguments

To add arguments for command you need to pass their description to the decorator arguments. If you need global arguments, pass them to `global_args` function. The available parameters of `arg` are the same as [for `add_argument` in `argparse`](https://docs.python.org/3/library/argparse.html#quick-links-for-add-argument).

```py
from arrrgs import command, arg, run, global_args

global_args(
    arg("--rage", "-r", action='store_true', help="Rage mod")
)

@command(
    arg("name", help="User name")
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

### Custom command name

A situation may arise where you have to name a command after a built-in function or type, e.g. `list`. To specify a command name other than the function name, use the `name` parameter.

```py
@command(name="list")
def list_numbers():
    """Prints list of numbers"""
    print("1, 2, 3")
```
