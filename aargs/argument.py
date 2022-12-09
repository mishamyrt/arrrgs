"""AArgs argument"""
from typing import List

def arg(*name_or_flags: List[str], **kwargs):
    """Convenience function to properly format arguments
    to pass to the subcommand decorator."""
    return (list(name_or_flags), kwargs)
