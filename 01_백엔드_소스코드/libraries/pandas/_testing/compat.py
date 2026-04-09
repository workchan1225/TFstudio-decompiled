# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compat.pyc (Python 3.11)

'''
Helpers for sharing tests between DataFrame/Series
'''
from __future__ import annotations
from typing import TYPE_CHECKING
from pandas import DataFrame
if TYPE_CHECKING:
    from pandas._typing import DtypeObj

def get_dtype(obj = None):
    if isinstance(obj, DataFrame):
        return obj.dtypes.iat[0]
    return None.dtype


def get_obj(df = None, klass = None):
    """
    For sharing tests using frame_or_series, either return the DataFrame
    unchanged or return it's first column as a Series.
    """
    if klass is DataFrame:
        return df
    return None._ixs(0, axis = 1)
