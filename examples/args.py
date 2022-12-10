"""Arrrgs arguments example"""
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
