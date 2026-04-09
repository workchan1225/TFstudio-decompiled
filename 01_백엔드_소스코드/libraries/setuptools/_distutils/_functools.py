# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _functools.pyc (Python 3.11)

import functools

def pass_none(func):
    """
    Wrap func so it's not called if its first param is None

    >>> print_text = pass_none(print)
    >>> print_text('text')
    text
    >>> print_text(None)
    """
    pass
# WARNING: Decompyle incomplete
