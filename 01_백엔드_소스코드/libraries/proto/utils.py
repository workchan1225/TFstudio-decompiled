# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import functools

def has_upb():
    
    try:
        _message = _message
        import google._upb
        has_upb = True
    except ImportError:
        has_upb = False

    return has_upb


def cached_property(fx):
    '''Make the callable into a cached property.

    Similar to @property, but the function will only be called once per
    object.

    Args:
        fx (Callable[]): The property function.

    Returns:
        Callable[]: The wrapped function.
    '''
    pass
# WARNING: Decompyle incomplete

__all__ = ('cached_property',)
