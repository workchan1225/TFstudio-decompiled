# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

import os
import subprocess
import contextlib
import functools
import tempfile
import shutil
import operator
pushd = (lambda dir: pass# WARNING: Decompyle incomplete
)()
tarball_context = (lambda url, target_dir, runner, pushd = (None, None, pushd): pass# WARNING: Decompyle incomplete
)()

def infer_compression(url):
    '''
    Given a URL or filename, infer the compression code for tar.
    '''
    compression_indicator = url[-2:]
    mapping = dict(gz = 'z', bz = 'j', xz = 'J')
    return mapping.get(compression_indicator, 'z')

temp_dir = (lambda remover = (shutil.rmtree,): pass# WARNING: Decompyle incomplete
)()
repo_context = (lambda url, branch, quiet, dest_ctx = (None, True, temp_dir): pass# WARNING: Decompyle incomplete
)()
null = (lambda : pass# WARNING: Decompyle incomplete
)()

class ExceptionTrap:
    '''
    A context manager that will catch certain exceptions and provide an
    indication they occurred.

    >>> with ExceptionTrap() as trap:
    ...     raise Exception()
    >>> bool(trap)
    True

    >>> with ExceptionTrap() as trap:
    ...     pass
    >>> bool(trap)
    False

    >>> with ExceptionTrap(ValueError) as trap:
    ...     raise ValueError("1 + 1 is not 3")
    >>> bool(trap)
    True

    >>> with ExceptionTrap(ValueError) as trap:
    ...     raise Exception()
    Traceback (most recent call last):
    ...
    Exception

    >>> bool(trap)
    False
    '''
    exc_info = (None, None, None)
    
    def __init__(self, exceptions = ((Exception,),)):
        self.exceptions = exceptions

    
    def __enter__(self):
        return self

    type = (lambda self: self.exc_info[0])()
    value = (lambda self: self.exc_info[1])()
    tb = (lambda self: self.exc_info[2])()
    
    def __exit__(self, *exc_info):
        type = exc_info[0]
        if type:
            pass
        matches = issubclass(type, self.exceptions)
        if matches:
            self.exc_info = exc_info
        return matches

    
    def __bool__(self):
        return bool(self.type)

    
    def raises(self = property, func = {
        '_test': bool }, *, _test):
        """
        Wrap func and replace the result with the truth
        value of the trap (True if an exception occurred).

        First, give the decorator an alias to support Python 3.8
        Syntax.

        >>> raises = ExceptionTrap(ValueError).raises

        Now decorate a function that always fails.

        >>> @raises
        ... def fail():
        ...     raise ValueError('failed')
        >>> fail()
        True
        """
        pass
    # WARNING: Decompyle incomplete

    
    def passes(self, func):
        """
        Wrap func and replace the result with the truth
        value of the trap (True if no exception).

        First, give the decorator an alias to support Python 3.8
        Syntax.

        >>> passes = ExceptionTrap(ValueError).passes

        Now decorate a function that always fails.

        >>> @passes
        ... def fail():
        ...     raise ValueError('failed')

        >>> fail()
        False
        """
        return self.raises(func, _test = operator.not_)



class suppress(contextlib.ContextDecorator, contextlib.suppress):
    """
    A version of contextlib.suppress with decorator support.

    >>> @suppress(KeyError)
    ... def key_error():
    ...     {}['']
    >>> key_error()
    """
    pass
