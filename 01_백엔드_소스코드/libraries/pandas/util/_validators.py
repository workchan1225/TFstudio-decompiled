# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _validators.pyc (Python 3.11)

'''
Module that contains many useful utilities
for validating data or function arguments
'''
from __future__ import annotations
from collections.abc import Iterable, Sequence
from typing import TypeVar, overload
import numpy as np
from pandas._libs import lib
from pandas._libs.missing import NA
from pandas.core.dtypes.common import is_bool, is_integer
BoolishT = TypeVar('BoolishT', bool, int)
BoolishNoneT = TypeVar('BoolishNoneT', bool, int, None)

def _check_arg_length(fname = None, args = None, max_fname_arg_count = None, compat_args = ('return', 'None')):
    """
    Checks whether 'args' has length of at most 'compat_args'. Raises
    a TypeError if that is not the case, similar to in Python when a
    function is called with too many arguments.
    """
    if max_fname_arg_count < 0:
        raise ValueError("'max_fname_arg_count' must be non-negative")
    if len(args) > len(compat_args):
        max_arg_count = len(compat_args) + max_fname_arg_count
        actual_arg_count = len(args) + max_fname_arg_count
        argument = 'argument' if max_arg_count == 1 else 'arguments'
        raise TypeError(f'''{fname}() takes at most {max_arg_count} {argument} ({actual_arg_count} given)''')


def _check_for_default_values(fname = None, arg_val_dict = None, compat_args = None):
    '''
    Check that the keys in `arg_val_dict` are mapped to their
    default values as specified in `compat_args`.

    Note that this function is to be called only when it has been
    checked that arg_val_dict.keys() is a subset of compat_args
    '''
    pass
# WARNING: Decompyle incomplete


def validate_args(fname = None, args = None, max_fname_arg_count = None, compat_args = ('return', 'None')):
    '''
    Checks whether the length of the `*args` argument passed into a function
    has at most `len(compat_args)` arguments and whether or not all of these
    elements in `args` are set to their default values.

    Parameters
    ----------
    fname : str
        The name of the function being passed the `*args` parameter
    args : tuple
        The `*args` parameter passed into a function
    max_fname_arg_count : int
        The maximum number of arguments that the function `fname`
        can accept, excluding those in `args`. Used for displaying
        appropriate error messages. Must be non-negative.
    compat_args : dict
        A dictionary of keys and their associated default values.
        In order to accommodate buggy behaviour in some versions of `numpy`,
        where a signature displayed keyword arguments but then passed those
        arguments **positionally** internally when calling downstream
        implementations, a dict ensures that the original
        order of the keyword arguments is enforced.

    Raises
    ------
    TypeError
        If `args` contains more values than there are `compat_args`
    ValueError
        If `args` contains values that do not correspond to those
        of the default values specified in `compat_args`
    '''
    _check_arg_length(fname, args, max_fname_arg_count, compat_args)
    kwargs = dict(zip(compat_args, args, strict = False))
    _check_for_default_values(fname, kwargs, compat_args)


def _check_for_invalid_keys(fname = None, kwargs = None, compat_args = None):
    """
    Checks whether 'kwargs' contains any keys that are not
    in 'compat_args' and raises a TypeError if there is one.
    """
    diff = set(kwargs) - set(compat_args)
    if diff:
        bad_arg = next(iter(diff))
        raise TypeError(f'''{fname}() got an unexpected keyword argument \'{bad_arg}\'''')


def validate_kwargs(fname = None, kwargs = None, compat_args = None):
    '''
    Checks whether parameters passed to the **kwargs argument in a
    function `fname` are valid parameters as specified in `*compat_args`
    and whether or not they are set to their default values.

    Parameters
    ----------
    fname : str
        The name of the function being passed the `**kwargs` parameter
    kwargs : dict
        The `**kwargs` parameter passed into `fname`
    compat_args: dict
        A dictionary of keys that `kwargs` is allowed to have and their
        associated default values

    Raises
    ------
    TypeError if `kwargs` contains keys not in `compat_args`
    ValueError if `kwargs` contains keys in `compat_args` that do not
    map to the default values specified in `compat_args`
    '''
    kwds = kwargs.copy()
    _check_for_invalid_keys(fname, kwargs, compat_args)
    _check_for_default_values(fname, kwds, compat_args)


def validate_args_and_kwargs(fname, args = None, kwargs = None, max_fname_arg_count = None, compat_args = ('return', 'None')):
    '''
    Checks whether parameters passed to the *args and **kwargs argument in a
    function `fname` are valid parameters as specified in `*compat_args`
    and whether or not they are set to their default values.

    Parameters
    ----------
    fname: str
        The name of the function being passed the `**kwargs` parameter
    args: tuple
        The `*args` parameter passed into a function
    kwargs: dict
        The `**kwargs` parameter passed into `fname`
    max_fname_arg_count: int
        The minimum number of arguments that the function `fname`
        requires, excluding those in `args`. Used for displaying
        appropriate error messages. Must be non-negative.
    compat_args: dict
        A dictionary of keys that `kwargs` is allowed to
        have and their associated default values.

    Raises
    ------
    TypeError if `args` contains more values than there are
    `compat_args` OR `kwargs` contains keys not in `compat_args`
    ValueError if `args` contains values not at the default value (`None`)
    `kwargs` contains keys in `compat_args` that do not map to the default
    value as specified in `compat_args`

    See Also
    --------
    validate_args : Purely args validation.
    validate_kwargs : Purely kwargs validation.

    '''
    _check_arg_length(fname, args + tuple(kwargs.values()), max_fname_arg_count, compat_args)
    args_dict = dict(zip(compat_args, args, strict = False))
    for key in args_dict:
        if key in kwargs:
            raise TypeError(f'''{fname}() got multiple values for keyword argument \'{key}\'''')
        kwargs.update(args_dict)
        validate_kwargs(fname, kwargs, compat_args)
        return None


def validate_bool_kwarg(value = None, arg_name = None, none_allowed = None, int_allowed = (True, False)):
