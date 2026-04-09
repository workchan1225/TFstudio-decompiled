# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: to_dict.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Literal, overload
import warnings
import numpy as np
from pandas._libs import lib, missing as libmissing
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.cast import maybe_box_native
from pandas.core.dtypes.dtypes import BaseMaskedDtype, ExtensionDtype
from pandas.core import common as com
if TYPE_CHECKING:
    from collections.abc import Generator
    from pandas._typing import MutableMappingT
    from pandas import DataFrame

def create_data_for_split(df = None, are_all_object_dtype_cols = None, object_dtype_indices = None):
    '''
    Simple helper method to create data for to ``to_dict(orient="split")``
    to create the main output data
    '''
    pass
# WARNING: Decompyle incomplete

to_dict = (lambda df = None, orient = None, *, into, index: pass)()
to_dict = (lambda df = None, orient = None, *, into, index: pass)()
to_dict = (lambda df = None, orient = None, *, into, index: pass)()
to_dict = (lambda df = None, orient = None, *, into, index: pass)()

def to_dict(df = None, orient = None, *, into, index):
    """
    Convert the DataFrame to a dictionary.

    The type of the key-value pairs can be customized with the parameters
    (see below).

    Parameters
    ----------
    orient : str {'dict', 'list', 'series', 'split', 'tight', 'records', 'index'}
        Determines the type of the values of the dictionary.

        - 'dict' (default) : dict like {column -> {index -> value}}
        - 'list' : dict like {column -> [values]}
        - 'series' : dict like {column -> Series(values)}
        - 'split' : dict like
          {'index' -> [index], 'columns' -> [columns], 'data' -> [values]}
        - 'tight' : dict like
          {'index' -> [index], 'columns' -> [columns], 'data' -> [values],
          'index_names' -> [index.names], 'column_names' -> [column.names]}
        - 'records' : list like
          [{column -> value}, ... , {column -> value}]
        - 'index' : dict like {index -> {column -> value}}

    into : class, default dict
        The collections.abc.MutableMapping subclass used for all Mappings
        in the return value.  Can be the actual class or an empty
        instance of the mapping type you want.  If you want a
        collections.defaultdict, you must pass it initialized.

    index : bool, default True
        Whether to include the index item (and index_names item if `orient`
        is 'tight') in the returned dictionary. Can only be ``False``
        when `orient` is 'split' or 'tight'.

        .. versionadded:: 2.0.0

    Returns
    -------
    dict, list or collections.abc.Mapping
        Return a collections.abc.MutableMapping object representing the
        DataFrame. The resulting transformation depends on the `orient` parameter.
    """
    pass
# WARNING: Decompyle incomplete
