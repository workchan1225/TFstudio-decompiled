# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _available_if.pyc (Python 3.11)

from functools import update_wrapper, wraps
from types import MethodType

class _AvailableIfDescriptor:
    '''Implements a conditional property using the descriptor protocol.

    Using this class to create a decorator will raise an ``AttributeError``
    if check(self) returns a falsey value. Note that if check raises an error
    this will also result in hasattr returning false.

    See https://docs.python.org/3/howto/descriptor.html for an explanation of
    descriptors.
    '''
    
    def __init__(self, fn, check, attribute_name):
        self.fn = fn
        self.check = check
        self.attribute_name = attribute_name
        update_wrapper(self, fn)

    
    def _check(self, obj, owner):
        attr_err_msg = f'''This {owner.__name__!r} has no attribute {self.attribute_name!r}'''
        
        try:
            check_result = self.check(obj)
        except Exception:
            e = None
            raise AttributeError(attr_err_msg), e
            e = None
            del e

        if not check_result:
            raise AttributeError(attr_err_msg)

    
    def __get__(self, obj, owner = (None,)):
        pass
    # WARNING: Decompyle incomplete



def available_if(check):
    '''An attribute that is available only if check returns a truthy value.

    Parameters
    ----------
    check : callable
        When passed the object with the decorated method, this should return
        a truthy value if the attribute is available, and either return False
        or raise an AttributeError if not available.

    Returns
    -------
    callable
        Callable makes the decorated method available if `check` returns
        a truthy value, otherwise the decorated method is unavailable.

    Examples
    --------
    >>> from sklearn.utils.metaestimators import available_if
    >>> class HelloIfEven:
    ...    def __init__(self, x):
    ...        self.x = x
    ...
    ...    def _x_is_even(self):
    ...        return self.x % 2 == 0
    ...
    ...    @available_if(_x_is_even)
    ...    def say_hello(self):
    ...        print("Hello")
    ...
    >>> obj = HelloIfEven(1)
    >>> hasattr(obj, "say_hello")
    False
    >>> obj.x = 2
    >>> hasattr(obj, "say_hello")
    True
    >>> obj.say_hello()
    Hello
    '''
    pass
# WARNING: Decompyle incomplete
