# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: callbacks.pyc (Python 3.11)

from functools import wraps

class Callback:
    '''
    Base class and interface for callback mechanism

    This class can be used directly for monitoring file transfers by
    providing ``callback=Callback(hooks=...)`` (see the ``hooks`` argument,
    below), or subclassed for more specialised behaviour.

    Parameters
    ----------
    size: int (optional)
        Nominal quantity for the value that corresponds to a complete
        transfer, e.g., total number of tiles or total number of
        bytes
    value: int (0)
        Starting internal counter value
    hooks: dict or None
        A dict of named functions to be called on each update. The signature
        of these must be ``f(size, value, **kwargs)``
    '''
    
    def __init__(self, size, value, hooks = (None, 0, None), **kwargs):
