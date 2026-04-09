# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: melt.pyc (Python 3.11)

from __future__ import annotations
import re
from typing import TYPE_CHECKING
import numpy as np
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import is_iterator, is_list_like
from pandas.core.dtypes.concat import concat_compat
from pandas.core.dtypes.missing import notna

algorithms
from pandas.core.indexes.api import MultiIndex
import pandas.core.algorithms, core
from pandas.core.reshape.concat import concat
from pandas.core.tools.numeric import to_numeric
if TYPE_CHECKING:
    from collections.abc import Hashable
    from pandas._typing import AnyArrayLike
    from pandas import DataFrame

def ensure_list_vars(arg_vars = None, variable = None, columns = None):
    pass
# WARNING: Decompyle incomplete

melt = (lambda frame, id_vars, value_vars = None, var_name = None, value_name = set_module('pandas'), col_level = (None, None, None, 'value', None, True), ignore_index = ('frame', 'DataFrame', 'value_name', 'Hashable', 'ignore_index', 'bool', 'return', 'DataFrame'): pass# WARNING: Decompyle incomplete
)()
lreshape = (lambda data = None, groups = None, dropna = set_module('pandas'): pass# WARNING: Decompyle incomplete
)()
wide_to_long = (lambda df, stubnames = None, i = None, j = set_module('pandas'), sep = ('', '\\d+'), suffix = ('df', 'DataFrame', 'sep', 'str', 'suffix', 'str', 'return', 'DataFrame'): 
def get_var_names(df = None, stub = None, sep = None, suffix = ('stub', 'str', 'sep', 'str', 'suffix', 'str')):
regex = f'''^{re.escape(stub)}{re.escape(sep)}{suffix}$'''df.columns[df.columns.str.match(regex)]
def melt_stub(df, stub, i = None, j = None, value_vars = None, sep = ('stub', 'str', 'sep', 'str')):
newdf = melt(df, id_vars = i, value_vars = value_vars, value_name = stub.rstrip(sep), var_name = j)newdf[j] = newdf[j].str.replace(re.escape(stub + sep), '', regex = True)try:
newdf[j] = to_numeric(newdf[j])except (TypeError, ValueError, OverflowError):
passnewdf.set_index(newdf.set_index[j])if not is_list_like(stubnames):
stubnames = [
stubnames]else:
stubnames = list(stubnames)if df.columns.isin(stubnames).any():
raise ValueError("stubname can't be identical to a column name")if not is_list_like(i):
i = [
i]else:
i = list(i)if df[i].duplicated().any():
raise ValueError('the id variables need to uniquely identify each row')_melted = []value_vars_flattened = []for stub in stubnames:
value_var = get_var_names(df, stub, sep, suffix)value_vars_flattened.extend(value_var)_melted.append(melt_stub(df, stub, i, j, value_var, sep))melted = concat(_melted, axis = 1)id_vars = df.columns.difference(value_vars_flattened)new = df[id_vars]if len(i) == 1:
new.set_index(i).join(melted)None.merge(melted.reset_index(), on = i).set_index(None.merge(melted.reset_index(), on = i).set_index[j]))()
