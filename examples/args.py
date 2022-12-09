"""AArgs arguments example"""
from aargs import command, arg, run

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
