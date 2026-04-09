# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''
Extend pandas with custom array types.
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast, overload
import numpy as np
from pandas._libs import missing as libmissing
from pandas._libs.hashtable import object_hash
from pandas._libs.properties import cache_readonly
from pandas.errors import AbstractMethodError
from pandas.util._decorators import set_module
from pandas.core.dtypes.generic import ABCDataFrame, ABCIndex, ABCSeries
if TYPE_CHECKING:
    from pandas._typing import DtypeObj, Shape, npt, type_t
    from pandas import Index
    from pandas.core.arrays import ExtensionArray
    ExtensionDtypeT = TypeVar('ExtensionDtypeT', bound = 'ExtensionDtype')
ExtensionDtype = <NODE:12>()

class StorageExtensionDtype(ExtensionDtype):
    pass
# WARNING: Decompyle incomplete

register_extension_dtype = (lambda cls = set_module('pandas.api.extensions'): _registry.register(cls)cls)()

class Registry:
    '''
    Registry for dtype inference.

    The registry allows one to map a string repr of an extension
    dtype to an extension dtype. The string alias can be used in several
    places, including

    * Series and Index constructors
    * :meth:`pandas.array`
    * :meth:`pandas.Series.astype`

    Multiple extension types can be registered.
    These are tried in order.
    '''
    
    def __init__(self = None):
        self.dtypes = []

    
    def register(self = None, dtype = None):
        '''
        Parameters
        ----------
        dtype : ExtensionDtype class
        '''
        if not issubclass(dtype, ExtensionDtype):
            raise ValueError('can only register pandas extension dtypes')
        self.dtypes.append(dtype)

    find = (lambda self = None, dtype = None: pass)()
    find = (lambda self = None, dtype = None: pass)()
    find = (lambda self = None, dtype = None: pass)()
    find = (lambda self = None, dtype = None: pass)()
    
    def find(self = None, dtype = None):
        '''
        Parameters
        ----------
        dtype : ExtensionDtype class or instance or str or numpy dtype or python type

        Returns
        -------
        return the first matching dtype, otherwise return None
        '''
        if not isinstance(dtype, str):
            if not isinstance(dtype, type):
                dtype_type = type(dtype)
            else:
                dtype_type = dtype
            if issubclass(dtype_type, ExtensionDtype):
                return cast('ExtensionDtype | type_t[ExtensionDtype]', dtype)
            return None
        for dtype_type in None.dtypes:
            
            return None, dtype_type.construct_from_string(dtype)
            except TypeError:
                continue
            return None


_registry = Registry()
