# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''
An interface for extending pandas with custom arrays.

.. warning::

   This is an experimental API and subject to breaking changes
   without warning.
'''
from __future__ import annotations
import operator
from typing import TYPE_CHECKING, Any, ClassVar, Literal, Self, cast, overload
import warnings
import numpy as np
from pandas._libs import algos as libalgos, lib
from pandas.compat import set_function_name
from pandas.compat.numpy import function as nv
from pandas.errors import AbstractMethodError
from pandas.util._decorators import cache_readonly, set_module
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import validate_bool_kwarg, validate_insert_loc
from pandas.core.dtypes.astype import astype_is_view
from pandas.core.dtypes.common import is_list_like, is_scalar, pandas_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCIndex, ABCSeries
from pandas.core.dtypes.missing import isna
from pandas.core import arraylike, missing, roperator
from pandas.core.algorithms import duplicated, factorize_array, isin, map_array, mode, rank, unique
from pandas.core.array_algos.quantile import quantile_with_mask
from pandas.core.missing import _fill_limit_area_1d
from pandas.core.sorting import nargminmax, nargsort
if TYPE_CHECKING:
    from collections.abc import Callable, Iterator, Sequence
    from pandas._libs.missing import NAType
    from pandas._typing import ArrayLike, AstypeArg, AxisInt, Dtype, DtypeObj, FillnaOptions, InterpolateOptions, NumpySorter, NumpyValueArrayLike, PositionalIndexer, ScalarIndexer, SequenceIndexer, Shape, SortKind, TakeIndexer, npt
    from pandas import Index, Series
_extension_array_shared_docs: 'dict[str, str]' = { }
ExtensionArray = <NODE:12>()

class ExtensionArraySupportsAnyAll(ExtensionArray):
    any = (lambda self = None, *, skipna: pass)()
    any = (lambda self = None, *, skipna: pass)()
    
    def any(self = None, *, skipna):
        raise AbstractMethodError(self)

    all = (lambda self = None, *, skipna: pass)()
    all = (lambda self = None, *, skipna: pass)()
    
    def all(self = None, *, skipna):
        raise AbstractMethodError(self)



class ExtensionOpsMixin:
    '''
    A base class for linking the operators to their dunder names.

    .. note::

       You may want to set ``__array_priority__`` if you want your
       implementation to be called when involved in binary operations
       with NumPy arrays.
    '''
    _create_arithmetic_method = (lambda cls, op: raise AbstractMethodError(cls))()
    _add_arithmetic_ops = (lambda cls = None: setattr(cls, '__add__', cls._create_arithmetic_method(operator.add))setattr(cls, '__radd__', cls._create_arithmetic_method(roperator.radd))setattr(cls, '__sub__', cls._create_arithmetic_method(operator.sub))setattr(cls, '__rsub__', cls._create_arithmetic_method(roperator.rsub))setattr(cls, '__mul__', cls._create_arithmetic_method(operator.mul))setattr(cls, '__rmul__', cls._create_arithmetic_method(roperator.rmul))setattr(cls, '__pow__', cls._create_arithmetic_method(operator.pow))setattr(cls, '__rpow__', cls._create_arithmetic_method(roperator.rpow))setattr(cls, '__mod__', cls._create_arithmetic_method(operator.mod))setattr(cls, '__rmod__', cls._create_arithmetic_method(roperator.rmod))setattr(cls, '__floordiv__', cls._create_arithmetic_method(operator.floordiv))setattr(cls, '__rfloordiv__', cls._create_arithmetic_method(roperator.rfloordiv))setattr(cls, '__truediv__', cls._create_arithmetic_method(operator.truediv))setattr(cls, '__rtruediv__', cls._create_arithmetic_method(roperator.rtruediv))setattr(cls, '__divmod__', cls._create_arithmetic_method(divmod))setattr(cls, '__rdivmod__', cls._create_arithmetic_method(roperator.rdivmod)))()
    _create_comparison_method = (lambda cls, op: raise AbstractMethodError(cls))()
    _add_comparison_ops = (lambda cls = None: setattr(cls, '__eq__', cls._create_comparison_method(operator.eq))setattr(cls, '__ne__', cls._create_comparison_method(operator.ne))setattr(cls, '__lt__', cls._create_comparison_method(operator.lt))setattr(cls, '__gt__', cls._create_comparison_method(operator.gt))setattr(cls, '__le__', cls._create_comparison_method(operator.le))setattr(cls, '__ge__', cls._create_comparison_method(operator.ge)))()
    _create_logical_method = (lambda cls, op: raise AbstractMethodError(cls))()
    _add_logical_ops = (lambda cls = None: setattr(cls, '__and__', cls._create_logical_method(operator.and_))setattr(cls, '__rand__', cls._create_logical_method(roperator.rand_))setattr(cls, '__or__', cls._create_logical_method(operator.or_))setattr(cls, '__ror__', cls._create_logical_method(roperator.ror_))setattr(cls, '__xor__', cls._create_logical_method(operator.xor))setattr(cls, '__rxor__', cls._create_logical_method(roperator.rxor)))()

ExtensionScalarOpsMixin = <NODE:12>()
