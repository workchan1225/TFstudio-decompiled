# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: timedeltas.pyc (Python 3.11)

'''
timedelta support tools
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any, overload
import numpy as np
from pandas._libs import lib
from pandas._libs.tslibs import NaT, NaTType
from pandas._libs.tslibs.timedeltas import Timedelta, disallow_ambiguous_unit, parse_timedelta_unit
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import is_list_like
from pandas.core.dtypes.dtypes import ArrowDtype
from pandas.core.dtypes.generic import ABCIndex, ABCSeries
from pandas.core.arrays.timedeltas import sequence_to_td64ns
if TYPE_CHECKING:
    from collections.abc import Hashable
    from datetime import timedelta
    from pandas._libs.tslibs.timedeltas import UnitChoices
    from pandas._typing import ArrayLike, DateTimeErrorChoices
    from pandas import Index, Series, TimedeltaIndex
to_timedelta = (lambda arg = None, unit = None, errors = overload: pass)()
to_timedelta = (lambda arg = None, unit = None, errors = overload: pass)()
to_timedelta = (lambda arg = None, unit = None, errors = overload: pass)()
to_timedelta = (lambda arg = None, unit = None, errors = set_module('pandas'): pass# WARNING: Decompyle incomplete
)()

def _coerce_scalar_to_timedelta_type(r = None, unit = None, errors = None):
    """Convert string 'r' to a timedelta object."""
    
    try:
        result = Timedelta(r, unit)
    except ValueError:
        if errors == 'raise':
            raise 
        result = NaT

    return result


def _convert_listlike(arg = None, unit = None, errors = None, name = (None, 'raise', None)):
    '''Convert a list of objects to a timedelta index object.'''
    arg_dtype = getattr(arg, 'dtype', None)
# WARNING: Decompyle incomplete
