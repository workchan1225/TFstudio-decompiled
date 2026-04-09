# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: deprecation.pyc (Python 3.11)

import functools
import warnings
from inspect import signature
__all__ = [
    'deprecated']

class deprecated:
    """Decorator to mark a function or class as deprecated.

    Issue a warning when the function is called/the class is instantiated and
    adds a warning to the docstring.

    The optional extra argument will be appended to the deprecation message
    and the docstring. Note: to use this with the default value for extra, put
    in an empty of parentheses:

    Examples
    --------
    >>> from sklearn.utils import deprecated
    >>> deprecated()
    <sklearn.utils.deprecation.deprecated object at ...>
    >>> @deprecated()
    ... def some_function(): pass

    Parameters
    ----------
    extra : str, default=''
          To be added to the deprecation messages.
    """
    
    def __init__(self, extra = ('',)):
        self.extra = extra

    
    def __call__(self, obj):
        '''Call method

        Parameters
        ----------
        obj : object
        '''
        if isinstance(obj, type):
            return self._decorate_class(obj)
        if None(obj, property):
            return self._decorate_property(obj)
        return None._decorate_fun(obj)

    
    def _decorate_class(self, cls):
        pass
    # WARNING: Decompyle incomplete

    
    def _decorate_fun(self, fun):
        '''Decorate function fun'''
        pass
    # WARNING: Decompyle incomplete

    
    def _decorate_property(self, prop):
        pass
    # WARNING: Decompyle incomplete



def _is_deprecated(func):
    '''Helper to check if func is wrapped by our deprecated decorator'''
    closures = getattr(func, '__closure__', [])
# WARNING: Decompyle incomplete
