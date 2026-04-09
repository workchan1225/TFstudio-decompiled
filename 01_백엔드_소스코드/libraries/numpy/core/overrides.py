# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: overrides.pyc (Python 3.11)

'''Implementation of __array_function__ overrides from NEP-18.'''
import collections
import functools
import os
from _utils import set_module
from _utils._inspect import getargspec
from numpy.core._multiarray_umath import add_docstring, _get_implementing_args, _ArrayFunctionDispatcher
ARRAY_FUNCTIONS = set()
array_function_like_doc = 'like : array_like, optional\n        Reference object to allow the creation of arrays which are not\n        NumPy arrays. If an array-like passed in as ``like`` supports\n        the ``__array_function__`` protocol, the result will be defined\n        by it. In this case, it ensures the creation of an array object\n        compatible with that passed in via this argument.'

def set_array_function_like_doc(public_api):
    pass
# WARNING: Decompyle incomplete

add_docstring(_ArrayFunctionDispatcher, '\n    Class to wrap functions with checks for __array_function__ overrides.\n\n    All arguments are required, and can only be passed by position.\n\n    Parameters\n    ----------\n    dispatcher : function or None\n        The dispatcher function that returns a single sequence-like object\n        of all arguments relevant.  It must have the same signature (except\n        the default values) as the actual implementation.\n        If ``None``, this is a ``like=`` dispatcher and the\n        ``_ArrayFunctionDispatcher`` must be called with ``like`` as the\n        first (additional and positional) argument.\n    implementation : function\n        Function that implements the operation on NumPy arrays without\n        overrides.  Arguments passed calling the ``_ArrayFunctionDispatcher``\n        will be forwarded to this (and the ``dispatcher``) as if using\n        ``*args, **kwargs``.\n\n    Attributes\n    ----------\n    _implementation : function\n        The original implementation passed in.\n    ')
add_docstring(_get_implementing_args, '\n    Collect arguments on which to call __array_function__.\n\n    Parameters\n    ----------\n    relevant_args : iterable of array-like\n        Iterable of possibly array-like arguments to check for\n        __array_function__ methods.\n\n    Returns\n    -------\n    Sequence of arguments with __array_function__ methods, in the order in\n    which they should be called.\n    ')
ArgSpec = collections.namedtuple('ArgSpec', 'args varargs keywords defaults')

def verify_matching_signatures(implementation, dispatcher):
    '''Verify that a dispatcher function has the right signature.'''
    pass
# WARNING: Decompyle incomplete


def array_function_dispatch(dispatcher, module, verify, docs_from_dispatcher = (None, None, True, False)):
    """Decorator for adding dispatch with the __array_function__ protocol.

    See NEP-18 for example usage.

    Parameters
    ----------
    dispatcher : callable or None
        Function that when called like ``dispatcher(*args, **kwargs)`` with
        arguments from the NumPy function call returns an iterable of
        array-like arguments to check for ``__array_function__``.

        If `None`, the first argument is used as the single `like=` argument
        and not passed on.  A function implementing `like=` must call its
        dispatcher with `like` as the first non-keyword argument.
    module : str, optional
        __module__ attribute to set on new function, e.g., ``module='numpy'``.
        By default, module is copied from the decorated function.
    verify : bool, optional
        If True, verify the that the signature of the dispatcher and decorated
        function signatures match exactly: all required and optional arguments
        should appear in order with the same names, but the default values for
        all optional arguments should be ``None``. Only disable verification
        if the dispatcher's signature needs to deviate for some particular
        reason, e.g., because the function has a signature like
        ``func(*args, **kwargs)``.
    docs_from_dispatcher : bool, optional
        If True, copy docs from the dispatcher function onto the dispatched
        function, rather than from the implementation. This is useful for
        functions defined in C, which otherwise don't have docstrings.

    Returns
    -------
    Function suitable for decorating the implementation of a NumPy function.

    """
    pass
# WARNING: Decompyle incomplete


def array_function_from_dispatcher(implementation, module, verify, docs_from_dispatcher = (None, True, True)):
    '''Like array_function_dispatcher, but with function arguments flipped.'''
    pass
# WARNING: Decompyle incomplete
