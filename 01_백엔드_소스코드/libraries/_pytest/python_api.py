# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: python_api.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Collection
from collections.abc import Mapping
from collections.abc import Sequence
from collections.abc import Sized
from decimal import Decimal
import math
from numbers import Complex
import pprint
import sys
from typing import Any
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from numpy import ndarray

def _compare_approx(full_object, message_data, number_of_elements = None, different_ids = None, max_abs_diff = None, max_rel_diff = ('full_object', 'object', 'message_data', 'Sequence[tuple[str, str, str]]', 'number_of_elements', 'int', 'different_ids', 'Sequence[object]', 'max_abs_diff', 'float', 'max_rel_diff', 'float', 'return', 'list[str]')):
    pass
# WARNING: Decompyle incomplete


class ApproxBase:
    '''Provide shared utilities for making approximate comparisons between
    numbers or sequences of numbers.'''
    __array_ufunc__ = None
    __array_priority__ = 100
    
    def __init__(self = None, expected = None, rel = None, abs = (None, None, False), nan_ok = ('nan_ok', 'bool', 'return', 'None')):
        __tracebackhide__ = True
        self.expected = expected
        self.abs = abs
        self.rel = rel
        self.nan_ok = nan_ok
        self._check_type()

    
    def __repr__(self = None):
        raise NotImplementedError

    
    def _repr_compare(self = None, other_side = None):
        return [
            'comparison failed',
            f'''Obtained: {other_side}''',
            f'''Expected: {self}''']

    
    def __eq__(self = None, actual = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __bool__(self):
        __tracebackhide__ = True
        raise AssertionError('approx() is not supported in a boolean context.\nDid you mean: `assert a == approx(b)`?')

    __hash__ = None
    
    def __ne__(self = None, actual = None):
        return not (actual == self)

    
    def _approx_scalar(self = None, x = None):
        if isinstance(x, Decimal):
            return ApproxDecimal(x, rel = self.rel, abs = self.abs, nan_ok = self.nan_ok)
        return None(x, rel = self.rel, abs = self.abs, nan_ok = self.nan_ok)

    
    def _yield_comparisons(self, actual):
        '''Yield all the pairs of numbers to be compared.

        This is used to implement the `__eq__` method.
        '''
        raise NotImplementedError

    
    def _check_type(self = None):
        '''Raise a TypeError if the expected value is not a valid type.'''
        pass



def _recursive_sequence_map(f, x):
    '''Recursively map a function over a sequence of arbitrary depth'''
    pass
# WARNING: Decompyle incomplete


class ApproxNumpy(ApproxBase):
    pass
# WARNING: Decompyle incomplete


class ApproxMapping(ApproxBase):
    pass
# WARNING: Decompyle incomplete


class ApproxSequenceLike(ApproxBase):
    pass
# WARNING: Decompyle incomplete


class ApproxScalar(ApproxBase):
    '''Perform approximate comparisons where the expected value is a single number.'''
    DEFAULT_ABSOLUTE_TOLERANCE: 'float | Decimal' = 1e-12
    DEFAULT_RELATIVE_TOLERANCE: 'float | Decimal' = 1e-06
    
    def __repr__(self = None):
