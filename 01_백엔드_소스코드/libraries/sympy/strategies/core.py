# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

''' Generic SymPy-Independent Strategies '''
from __future__ import annotations
from collections.abc import Callable, Mapping
from typing import TypeVar
from sys import stdout
_S = TypeVar('_S')
_T = TypeVar('_T')

def identity(x = None):
    return x


def exhaust(rule = None):
    ''' Apply a rule repeatedly until it has no effect '''
    pass
# WARNING: Decompyle incomplete


def memoize(rule = None):
    '''Memoized version of a rule

    Notes
    =====

    This cache can grow infinitely, so it is not recommended to use this
    than ``functools.lru_cache`` unless you need very heavy computation.
    '''
    pass
# WARNING: Decompyle incomplete


def condition(cond = None, rule = None):
    ''' Only apply rule if condition is true '''
    pass
# WARNING: Decompyle incomplete


def chain(*rules):
    '''
    Compose a sequence of rules so that they apply to the expr sequentially
    '''
    pass
# WARNING: Decompyle incomplete


def debug(rule, file = (None,)):
    ''' Print out before and after expressions each time rule is used '''
    pass
# WARNING: Decompyle incomplete


def null_safe(rule = None):
    ''' Return original expr if rule returns None '''
    pass
# WARNING: Decompyle incomplete


def tryit(rule = None, exception = None):
    ''' Return original expr if rule raises exception '''
    pass
# WARNING: Decompyle incomplete


def do_one(*rules):
    ''' Try each of the rules until one works. Then stop. '''
    pass
# WARNING: Decompyle incomplete


def switch(key = None, ruledict = None):
    ''' Select a rule based on the result of key called on the function '''
    pass
# WARNING: Decompyle incomplete


def _identity(x):
    return x


def minimize(*, objective, *rules):
    ''' Select result of rules that minimizes objective

    >>> from sympy.strategies import minimize
    >>> inc = lambda x: x + 1
    >>> dec = lambda x: x - 1
    >>> rl = minimize(inc, dec)
    >>> rl(4)
    3

    >>> rl = minimize(inc, dec, objective=lambda x: -x)  # maximize
    >>> rl(4)
    5
    '''
    pass
# WARNING: Decompyle incomplete
