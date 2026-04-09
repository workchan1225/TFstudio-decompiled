# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extension.pyc (Python 3.11)

'''
Shared methods for Index subclasses backed by ExtensionArray.
'''
from __future__ import annotations
from inspect import signature
from typing import TYPE_CHECKING, TypeVar
from pandas.util._decorators import cache_readonly
from pandas.core.dtypes.generic import ABCDataFrame
from pandas.core.indexes.base import Index
if TYPE_CHECKING:
    from collections.abc import Callable
    import numpy as np
    from pandas._typing import ArrayLike, npt
    from pandas.core.arrays import IntervalArray
    from pandas.core.arrays._mixins import NDArrayBackedExtensionArray
_ExtensionIndexT = TypeVar('_ExtensionIndexT', bound = 'ExtensionIndex')

def _inherit_from_data(name = None, delegate = None, cache = None, wrap = (False, False)):
    '''
    Make an alias for a method of the underlying ExtensionArray.

    Parameters
    ----------
    name : str
        Name of an attribute the class should inherit from its EA parent.
    delegate : class
    cache : bool, default False
        Whether to convert wrapped properties into cache_readonly
    wrap : bool, default False
        Whether to wrap the inherited result in an Index.

    Returns
    -------
    attribute, method, property, or cache_readonly
    '''
    pass
# WARNING: Decompyle incomplete


def inherit_names(names = None, delegate = None, cache = None, wrap = (False, False)):
    '''
    Class decorator to pin attributes from an ExtensionArray to an Index subclass.

    Parameters
    ----------
    names : List[str]
    delegate : class
    cache : bool, default False
    wrap : bool, default False
        Whether to wrap the inherited result in an Index.
    '''
    pass
# WARNING: Decompyle incomplete


class ExtensionIndex(Index):
    _data: 'IntervalArray | NDArrayBackedExtensionArray' = '\n    Index subclass for indexes backed by ExtensionArray.\n    '
    
    def _validate_fill_value(self, value):
        '''
        Convert value to be insertable to underlying array.
        '''
        return self._data._validate_setitem_value(value)

    _isnan = (lambda self = None: self._data.isna())()


class NDArrayBackedExtensionIndex(ExtensionIndex):
    _data: 'NDArrayBackedExtensionArray' = '\n    Index subclass for indexes backed by NDArrayBackedExtensionArray.\n    '
    
    def _get_engine_target(self = None):
        return self._data._ndarray

    
    def _from_join_target(self = None, result = None):
        pass
    # WARNING: Decompyle incomplete
