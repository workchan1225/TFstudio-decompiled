# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extensions.pyc (Python 3.11)

'''
Utility classes/functions to let numba recognize
pandas Index/Series/DataFrame

Mostly vendored from https://github.com/numba/numba/blob/main/numba/tests/pdlike_usecase.py
'''
from __future__ import annotations
from contextlib import contextmanager
import operator
from typing import Self
import numba
from numba import types
from numba.core import cgutils
from numba.core.datamodel import models
from numba.core.extending import NativeValue, box, lower_builtin, make_attribute_wrapper, overload, overload_attribute, overload_method, register_model, type_callable, typeof_impl, unbox
from numba.core.imputils import impl_ret_borrowed
import numpy as np
from pandas._libs import lib
from pandas.core.indexes.base import Index
from pandas.core.indexing import _iLocIndexer
from pandas.core.internals import SingleBlockManager
from pandas.core.series import Series
set_numba_data = (lambda index = None: pass# WARNING: Decompyle incomplete
)()

class IndexType(types.Type):
    pass
# WARNING: Decompyle incomplete


class SeriesType(types.Type):
    pass
# WARNING: Decompyle incomplete

typeof_index = (lambda val = None, c = None: arrty = typeof_impl(val._numba_data, c)# WARNING: Decompyle incomplete
)()
typeof_series = (lambda val = None, c = None: index = typeof_impl(val.index, c)arrty = typeof_impl(val.values, c)namety = typeof_impl(val.name, c)# WARNING: Decompyle incomplete
)()
type_series_constructor = (lambda context: 
def typer(data, index, name = (None,)):
pass# WARNING: Decompyle incomplete
typer)()
type_index_constructor = (lambda context: 
def typer(data, hashmap = (None,)):
pass# WARNING: Decompyle incomplete
typer)()
IndexModel = <NODE:12>()
SeriesModel = <NODE:12>()
make_attribute_wrapper(IndexType, 'data', '_data')
make_attribute_wrapper(IndexType, 'hashmap', 'hashmap')
make_attribute_wrapper(SeriesType, 'index', 'index')
make_attribute_wrapper(SeriesType, 'values', 'values')
make_attribute_wrapper(SeriesType, 'name', 'name')
pdseries_constructor = (lambda context, builder, sig, args: (data, index) = argsseries = cgutils.create_struct_proxy(sig.return_type)(context, builder)series.index = indexseries.values = dataseries.name = context.get_constant(types.intp, 0)impl_ret_borrowed(context, builder, sig.return_type, series._getvalue()))()
pdseries_constructor_with_name = (lambda context, builder, sig, args: (data, index, name) = argsseries = cgutils.create_struct_proxy(sig.return_type)(context, builder)series.index = indexseries.values = dataseries.name = nameimpl_ret_borrowed(context, builder, sig.return_type, series._getvalue()))()()()
index_constructor_2arg = (lambda context, builder, sig, args: (data, hashmap, parent) = argsindex = cgutils.create_struct_proxy(sig.return_type)(context, builder)index.data = dataindex.hashmap = hashmapindex.parent = parentimpl_ret_borrowed(context, builder, sig.return_type, index._getvalue()))()
index_constructor_2arg_parent = (lambda context, builder, sig, args: (data, hashmap) = argsindex = cgutils.create_struct_proxy(sig.return_type)(context, builder)index.data = dataindex.hashmap = hashmapimpl_ret_borrowed(context, builder, sig.return_type, index._getvalue()))()
index_constructor_1arg = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()

def maybe_cast_str(x):
    pass

maybe_cast_str_impl = (lambda x:
