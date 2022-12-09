"""Arrrgs arguments example"""
from arrrgs import command, run

class User:
    """Represents user"""

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
