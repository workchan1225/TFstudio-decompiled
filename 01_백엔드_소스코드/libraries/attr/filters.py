# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: filters.pyc (Python 3.11)

'''
Commonly useful filters for `attrs.asdict` and `attrs.astuple`.
'''
from _make import Attribute

def _split_what(what):
    '''
    Returns a tuple of `frozenset`s of classes and attributes.
    '''
    return (None, frozenset, (lambda .0: pass# WARNING: Decompyle incomplete
)(what()))


def include(*what):
    """
    Create a filter that only allows *what*.

    Args:
        what (list[type, str, attrs.Attribute]):
            What to include. Can be a type, a name, or an attribute.

    Returns:
        Callable:
            A callable that can be passed to `attrs.asdict`'s and
            `attrs.astuple`'s *filter* argument.

    .. versionchanged:: 23.1.0 Accept strings with field names.
    """
    pass
# WARNING: Decompyle incomplete


def exclude(*what):
    """
    Create a filter that does **not** allow *what*.

    Args:
        what (list[type, str, attrs.Attribute]):
            What to exclude. Can be a type, a name, or an attribute.

    Returns:
        Callable:
            A callable that can be passed to `attrs.asdict`'s and
            `attrs.astuple`'s *filter* argument.

    .. versionchanged:: 23.3.0 Accept field name string as input argument
    """
    pass
# WARNING: Decompyle incomplete
