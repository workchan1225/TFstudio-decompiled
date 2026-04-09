# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: object_array.pyc (Python 3.11)

from __future__ import annotations
import functools
import re
import textwrap
from typing import TYPE_CHECKING, Literal, cast
import unicodedata
import numpy as np
from pandas._libs import lib

missing

ops
from pandas.util._validators import validate_na_arg
import pandas._libs.ops, _libs
from pandas.core.dtypes.common import pandas_dtype
from pandas.core.dtypes.missing import isna
if TYPE_CHECKING:
    from collections.abc import Callable, Sequence
    from pandas._typing import NpDtype, Scalar

class ObjectStringArrayMixin:
    '''
    String Methods operating on object-dtype ndarrays.
    '''
    
    def __len__(self = None):
        raise NotImplementedError

    
    def _str_getitem(self, key):
        if isinstance(key, slice):
            return self._str_slice(start = key.start, stop = key.stop, step = key.step)
        return None._str_get(key)

    
    def _str_map(self = None, f = None, na_value = None, dtype = (lib.no_default, None, True), convert = ('dtype', 'NpDtype | None', 'convert', 'bool')):
        '''
        Map a callable over valid elements of the array.

        Parameters
        ----------
        f : Callable
            A function to call on each non-NA element.
        na_value : Scalar, optional
            The value to set for NA values. Might also be used for the
            fill value if the callable `f` raises an exception.
            This defaults to ``self.dtype.na_value`` which is ``np.nan``
            for object-dtype and Categorical and ``pd.NA`` for StringArray.
        dtype : Dtype, optional
            The dtype of the result array.
        convert : bool, default True
            Whether to call `maybe_convert_objects` on the resulting ndarray
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _str_count(self = None, pat = None, flags = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_pad(self = None, width = None, side = None, fillchar = ('left', ' ')):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_contains(self, pat = None, case = None, flags = None, na = (True, 0, lib.no_default, True), regex = ('case', 'bool', 'flags', 'int', 'regex', 'bool')):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_startswith(self, pat, na = (lib.no_default,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_endswith(self, pat, na = (lib.no_default,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_replace(self, pat, repl = None, n = None, case = None, flags = (-1, True, 0, True), regex = ('pat', 'str | re.Pattern', 'repl', 'str | Callable', 'n', 'int', 'case', 'bool', 'flags', 'int', 'regex', 'bool')):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_repeat(self = None, repeats = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_match(self = None, pat = None, case = None, flags = (True, 0, lib.no_default), na = ('pat', 'str | re.Pattern', 'case', 'bool', 'flags', 'int', 'na', 'Scalar | lib.NoDefault')):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_fullmatch(self = None, pat = None, case = None, flags = (True, 0, lib.no_default), na = ('pat', 'str | re.Pattern', 'case', 'bool', 'flags', 'int', 'na', 'Scalar | lib.NoDefault')):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_encode(self = None, encoding = None, errors = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_find(self = None, sub = None, start = None, end = (0, None)):
        return self._str_find_(sub, start, end, side = 'left')

    
    def _str_rfind(self = None, sub = None, start = None, end = (0, None)):
        return self._str_find_(sub, start, end, side = 'right')

    
    def _str_find_(self, sub, start, end, side):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_findall(self = None, pat = None, flags = None):
        regex = re.compile(pat, flags = flags)
        return self._str_map(regex.findall, dtype = 'object')

    
    def _str_get(self, i):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_index(self = None, sub = None, start = None, end = (0, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_rindex(self = None, sub = None, start = None, end = (0, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_join(self = None, sep = None):
        return self._str_map(sep.join)

    
    def _str_partition(self = None, sep = None, expand = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_rpartition(self = None, sep = None, expand = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_len(self):
        return self._str_map(len, dtype = 'int64')

    
    def _str_slice(self, start, stop, step = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_slice_replace(self, start, stop, repl = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_split(self = None, pat = None, n = None, expand = (None, -1, False, None), regex = ('pat', 'str | re.Pattern | None', 'expand', 'bool', 'regex', 'bool | None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_rsplit(self, pat, n = (None, -1)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_translate(self, table):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_wrap(self = None, width = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_get_dummies(self = None, sep = None, dtype = None):
        Series = Series
        import pandas
    # WARNING: Decompyle incomplete

    
    def _str_upper(self):
        return self._str_map((lambda x: x.upper()))

    
    def _str_isalnum(self):
        return self._str_map(str.isalnum, dtype = 'bool')

    
    def _str_isalpha(self):
        return self._str_map(str.isalpha, dtype = 'bool')

    
    def _str_isascii(self):
        return self._str_map(str.isascii, dtype = 'bool')

    
    def _str_isdecimal(self):
        return self._str_map(str.isdecimal, dtype = 'bool')

    
    def _str_isdigit(self):
        return self._str_map(str.isdigit, dtype = 'bool')

    
    def _str_islower(self):
        return self._str_map(str.islower, dtype = 'bool')

    
    def _str_isnumeric(self):
        return self._str_map(str.isnumeric, dtype = 'bool')

    
    def _str_isspace(self):
        return self._str_map(str.isspace, dtype = 'bool')

    
    def _str_istitle(self):
        return self._str_map(str.istitle, dtype = 'bool')

    
    def _str_isupper(self):
        return self._str_map(str.isupper, dtype = 'bool')

    
    def _str_capitalize(self):
        return self._str_map(str.capitalize)

    
    def _str_casefold(self):
        return self._str_map(str.casefold)

    
    def _str_title(self):
        return self._str_map(str.title)

    
    def _str_swapcase(self):
        return self._str_map(str.swapcase)

    
    def _str_lower(self):
        return self._str_map(str.lower)

    
    def _str_normalize(self, form):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_strip(self, to_strip = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_lstrip(self, to_strip = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_rstrip(self, to_strip = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_removeprefix(self = None, prefix = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_removesuffix(self = None, suffix = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_extract(self = None, pat = None, flags = None, expand = (0, True)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_zfill(self = None, width = None):
        pass
    # WARNING: Decompyle incomplete
