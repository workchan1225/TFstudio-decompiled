# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _arrow_string_mixins.pyc (Python 3.11)

from __future__ import annotations
from functools import partial
import re
from typing import TYPE_CHECKING, Any, Literal, Self
import numpy as np
from pandas._libs import lib
from pandas.compat import HAS_PYARROW, pa_version_under17p0, pa_version_under21p0
if HAS_PYARROW:
    import pyarrow as pa
    from pyarrow.compute import compute as pc
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import Scalar

class ArrowStringArrayMixin:
    _pa_array: 'pa.ChunkedArray' = 'ArrowStringArrayMixin'
    
    def __init__(self = None, *args, **kwargs):
        raise NotImplementedError

    
    def _from_pyarrow_array(self = None, pa_array = None):
        raise NotImplementedError

    
    def _convert_bool_result(self, result, na, method_name = (lib.no_default, None)):
        raise NotImplementedError

    
    def _convert_int_result(self, result):
        raise NotImplementedError

    
    def _apply_elementwise(self = None, func = None):
        raise NotImplementedError

    _has_unsupported_regex = (lambda pat = None: pass# WARNING: Decompyle incomplete
)()
    
    def _str_len(self):
        result = pc.utf8_length(self._pa_array)
        return self._convert_int_result(result)

    
    def _str_lower(self = None):
        return self._from_pyarrow_array(pc.utf8_lower(self._pa_array))

    
    def _str_upper(self = None):
        return self._from_pyarrow_array(pc.utf8_upper(self._pa_array))

    
    def _str_strip(self = None, to_strip = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_lstrip(self = None, to_strip = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_rstrip(self = None, to_strip = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_pad(self = None, width = None, side = None, fillchar = ('left', ' ')):
        if side == 'left':
            pa_pad = pc.utf8_lpad
        elif side == 'right':
            pa_pad = pc.utf8_rpad
        elif side == 'both':
            if pa_version_under17p0:
                array = array
                import pandas
                obj_arr = self.astype(object, copy = False)
                obj = array(obj_arr, dtype = object)
                result = obj._str_pad(width, side, fillchar)
                return type(self)._from_sequence(result, dtype = self.dtype)
            lean_left = None % 2 == 0
            pa_pad = partial(pc.utf8_center, lean_left_on_odd_padding = lean_left)
        else:
            raise ValueError(f'''Invalid side: {side}. Side must be one of \'left\', \'right\', \'both\'''')
        return self._from_pyarrow_array(pa_pad(self._pa_array, width = width, padding = fillchar))

    
    def _str_get(self = None, i = None):
        lengths = pc.utf8_length(self._pa_array)
        if i >= 0:
            out_of_bounds = pc.greater_equal(i, lengths)
            start = i
            stop = i + 1
            step = 1
        else:
            out_of_bounds = pc.greater(-i, lengths)
            start = i
            stop = i - 1
            step = -1
        not_out_of_bounds = pc.invert(out_of_bounds.fill_null(True))
        selected = pc.utf8_slice_codeunits(self._pa_array, start = start, stop = stop, step = step)
        null_value = pa.scalar(None, type = self._pa_array.type)
        result = pc.if_else(not_out_of_bounds, selected, null_value)
        return self._from_pyarrow_array(result)

    
    def _str_slice(self = None, start = None, stop = None, step = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_slice_replace(self = None, start = None, stop = None, repl = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def _str_replace(self, pat, repl = None, n = None, case = None, flags = (-1, True, 0, True), regex = ('pat', 'str | re.Pattern', 'repl', 'str | Callable', 'n', 'int', 'case', 'bool', 'flags', 'int', 'regex', 'bool', 'return', 'Self')):
        if (isinstance(pat, re.Pattern) and callable(repl) and case and flags or isinstance(repl, str)) and '\\g<' in repl:
            raise NotImplementedError('replace is not supported with a re.Pattern, callable repl, case=False, flags!=0, or when the replacement string contains named group references (\\g<...>)')
        func = pc.replace_substring_regex if regex else pc.replace_substring
        pa_max_replacements = None if n < 0 else n
        result = func(self._pa_array, pattern = pat, replacement = repl, max_replacements = pa_max_replacements)
        return self._from_pyarrow_array(result)

    
    def _str_capitalize(self = None):
        return self._from_pyarrow_array(pc.utf8_capitalize(self._pa_array))

    
    def _str_title(self = None):
        return self._from_pyarrow_array(pc.utf8_title(self._pa_array))

    
    def _str_swapcase(self = None):
        return self._from_pyarrow_array(pc.utf8_swapcase(self._pa_array))

    
    def _str_removeprefix(self = None, prefix = None):
        if prefix == '':
            return self._from_pyarrow_array(self._pa_array)
        starts_with = None.starts_with(self._pa_array, pattern = prefix)
        removed = pc.utf8_slice_codeunits(self._pa_array, len(prefix))
        result = pc.if_else(starts_with, removed, self._pa_array)
        return self._from_pyarrow_array(result)

    
    def _str_removesuffix(self = None, suffix = None):
        if suffix == '':
            return self._from_pyarrow_array(self._pa_array)
        ends_with = None.ends_with(self._pa_array, pattern = suffix)
        removed = pc.utf8_slice_codeunits(self._pa_array, 0, stop = -len(suffix))
        result = pc.if_else(ends_with, removed, self._pa_array)
        return self._from_pyarrow_array(result)

    
    def _str_startswith(self = None, pat = None, na = None):
        if isinstance(pat, str):
            result = pc.starts_with(self._pa_array, pattern = pat)
        elif len(pat) == 0:
            result = pc.if_else(pc.is_null(self._pa_array), None, False)
        else:
            result = pc.starts_with(self._pa_array, pattern = pat[0])
            for p in pat[1:]:
                result = pc.or_(result, pc.starts_with(self._pa_array, pattern = p))
                return self._convert_bool_result(result, na = na, method_name = 'startswith')

    
    def _str_endswith(self = None, pat = None, na = None):
        if isinstance(pat, str):
            result = pc.ends_with(self._pa_array, pattern = pat)
        elif len(pat) == 0:
            result = pc.if_else(pc.is_null(self._pa_array), None, False)
        else:
            result = pc.ends_with(self._pa_array, pattern = pat[0])
            for p in pat[1:]:
                result = pc.or_(result, pc.ends_with(self._pa_array, pattern = p))
                return self._convert_bool_result(result, na = na, method_name = 'endswith')

    
    def _str_isalnum(self):
        result = pc.utf8_is_alnum(self._pa_array)
        return self._convert_bool_result(result)

    
    def _str_isalpha(self):
        result = pc.utf8_is_alpha(self._pa_array)
        return self._convert_bool_result(result)

    
    def _str_isascii(self):
        result = pc.string_is_ascii(self._pa_array)
        return self._convert_bool_result(result)

    
    def _str_isdecimal(self):
        result = pc.utf8_is_decimal(self._pa_array)
        return self._convert_bool_result(result)

    
    def _str_isdigit(self):
        if pa_version_under21p0:
            res_list = self._apply_elementwise(str.isdigit)
            return self._convert_bool_result(pa.chunked_array(res_list, type = pa.bool_()))
        result = None.utf8_is_digit(self._pa_array)
        return self._convert_bool_result(result)

    
    def _str_islower(self):
        result = pc.utf8_is_lower(self._pa_array)
        return self._convert_bool_result(result)

    
    def _str_isnumeric(self):
        result = pc.utf8_is_numeric(self._pa_array)
        return self._convert_bool_result(result)

    
    def _str_isspace(self):
        result = pc.utf8_is_space(self._pa_array)
        return self._convert_bool_result(result)

    
    def _str_istitle(self):
        result = pc.utf8_is_title(self._pa_array)
        return self._convert_bool_result(result)

    
    def _str_isupper(self):
        result = pc.utf8_is_upper(self._pa_array)
        return self._convert_bool_result(result)

    
    def _str_contains(self, pat = None, case = None, flags = None, na = (True, 0, lib.no_default, True), regex = ('case', 'bool', 'flags', 'int', 'na', 'Scalar | lib.NoDefault', 'regex', 'bool')):
        if flags:
            raise NotImplementedError(f'''contains not implemented with flags={flags!r}''')
        if regex:
            pa_contains = pc.match_substring_regex
        else:
            pa_contains = pc.match_substring
        result = pa_contains(self._pa_array, pat, ignore_case = not case)
        return self._convert_bool_result(result, na = na, method_name = 'contains')

    
    def _str_match(self = None, pat = None, case = None, flags = (True, 0, lib.no_default), na = ('pat', 'str', 'case', 'bool', 'flags', 'int', 'na', 'Scalar | lib.NoDefault')):
        if not pat.startswith('^'):
            pat = f'''^({pat})'''
        return ArrowStringArrayMixin._str_contains(self, pat, case, flags, na, regex = True)

    
    def _str_fullmatch(self = None, pat = None, case = None, flags = (True, 0, lib.no_default), na = ('pat', 'str', 'case', 'bool', 'flags', 'int', 'na', 'Scalar | lib.NoDefault')):
        if not (pat.endswith('$') or pat.endswith('\\$')) and pat.startswith('^'):
            pat = f'''^({pat})$'''
        elif pat.endswith('$') or pat.endswith('\\$'):
            pat = f'''^({pat[1:]})$'''
        elif not pat.startswith('^'):
            pat = f'''^({pat[0:-1]})$'''
        return ArrowStringArrayMixin._str_match(self, pat, case, flags, na)

    
    def _str_find(self = None, sub = None, start = None, end = (0, None)):
        pass
    # WARNING: Decompyle incomplete
