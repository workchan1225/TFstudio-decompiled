# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _query.pyc (Python 3.11)

'''Query string handling.'''
import math
from collections.abc import Iterable, Mapping, Sequence
from typing import TYPE_CHECKING, Any, SupportsInt, Union, cast
from multidict import istr
from _quoters import QUERY_PART_QUOTER, QUERY_QUOTER
SimpleQuery = Union[(str, SupportsInt, float)]
QueryVariable = Union[(SimpleQuery, Sequence[SimpleQuery])]
Query = Union[(None, str, Mapping[(str, QueryVariable)], Sequence[tuple[(str, QueryVariable)]])]

def query_var(v = None):
    '''Convert a query variable to a string.'''
    cls = type(v)
    if cls is int:
        return str(v)
    if None(v, str):
        return v
    if None(v, float):
        if math.isinf(v):
            raise ValueError("float('inf') is not supported")
        if math.isnan(v):
            raise ValueError("float('nan') is not supported")
        return str(float(v))
    if None is not bool and isinstance(v, SupportsInt):
        return str(int(v))
    raise None('Invalid variable type: value should be str, int or float, got {!r} of type {}'.format(v, cls))


def get_str_query_from_sequence_iterable(items = None):
    '''Return a query string from a sequence of (key, value) pairs.

    value is a single value or a sequence of values for the key

    The sequence of values must be a list or tuple.
    '''
    pass
# WARNING: Decompyle incomplete


def get_str_query_from_iterable(items = None):
    '''Return a query string from an iterable.

    The iterable must contain (key, value) pairs.

    The values are not allowed to be sequences, only single values are
    allowed. For sequences, use `_get_str_query_from_sequence_iterable`.
    '''
    pass
# WARNING: Decompyle incomplete


def get_str_query(*args, **kwargs):
    '''Return a query string from supported args.'''
    if kwargs:
        if args:
            msg = 'Either kwargs or single query parameter must be present'
            raise ValueError(msg)
        query = kwargs
    elif len(args) == 1:
        query = args[0]
    else:
        raise ValueError('Either kwargs or single query parameter must be present')
# WARNING: Decompyle incomplete
