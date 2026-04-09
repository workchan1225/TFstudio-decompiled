# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: unicode.pyc (Python 3.11)

import sys
import operator
import numpy as np
from llvmlite.ir import IntType, Constant
from numba.core.cgutils import is_nonelike
from numba.core.extending import models, register_model, make_attribute_wrapper, unbox, box, NativeValue, overload, overload_method, intrinsic, register_jitable
from numba.core.imputils import lower_constant, lower_cast, lower_builtin, iternext_impl, impl_ret_new_ref, RefType
from numba.core.datamodel import register_default, StructModel
from numba.core import types, cgutils, config
from numba.core.utils import PYVERSION
from numba.core.pythonapi import PY_UNICODE_1BYTE_KIND, PY_UNICODE_2BYTE_KIND, PY_UNICODE_4BYTE_KIND
from numba._helperlib import c_helpers
from numba.cpython.hashing import _Py_hash_t
from numba.core.unsafe.bytes import memcpy_region
from numba.core.errors import TypingError
from numba.cpython.unicode_support import _Py_TOUPPER, _Py_TOLOWER, _Py_UCS4, _Py_ISALNUM, _PyUnicode_ToUpperFull, _PyUnicode_ToLowerFull, _PyUnicode_ToFoldedFull, _PyUnicode_ToTitleFull, _PyUnicode_IsPrintable, _PyUnicode_IsSpace, _Py_ISSPACE, _PyUnicode_IsXidStart, _PyUnicode_IsXidContinue, _PyUnicode_IsCased, _PyUnicode_IsCaseIgnorable, _PyUnicode_IsUppercase, _PyUnicode_IsLowercase, _PyUnicode_IsLineBreak, _Py_ISLINEBREAK, _Py_ISLINEFEED, _Py_ISCARRIAGERETURN, _PyUnicode_IsTitlecase, _Py_ISLOWER, _Py_ISUPPER, _Py_TAB, _Py_LINEFEED, _Py_CARRIAGE_RETURN, _Py_SPACE, _PyUnicode_IsAlpha, _PyUnicode_IsNumeric, _Py_ISALPHA, _PyUnicode_IsDigit, _PyUnicode_IsDecimalDigit
from numba.cpython import slicing
if PYVERSION in ((3, 10), (3, 11)):
    from numba.core.pythonapi import PY_UNICODE_WCHAR_KIND
_MAX_UNICODE = 1114111
if config.USE_LEGACY_TYPE_SYSTEM:
    _BLOOM_WIDTH = types.intp.bitwidth
else:
    _BLOOM_WIDTH = types.py_int.bitwidth
UnicodeModel = <NODE:12>()
make_attribute_wrapper(types.UnicodeType, 'data', '_data')
make_attribute_wrapper(types.UnicodeType, 'length', '_length')
make_attribute_wrapper(types.UnicodeType, 'kind', '_kind')
make_attribute_wrapper(types.UnicodeType, 'is_ascii', '_is_ascii')
make_attribute_wrapper(types.UnicodeType, 'hash', '_hash')
UnicodeIteratorModel = <NODE:12>()

def compile_time_get_string_data(obj):
    '''Get string data from a python string for use at compile-time to embed
    the string data into the LLVM module.
    '''
    CFUNCTYPE = CFUNCTYPE
    c_void_p = c_void_p
    c_int = c_int
    c_uint = c_uint
    c_ssize_t = c_ssize_t
    c_ubyte = c_ubyte
    py_object = py_object
    POINTER = POINTER
    byref = byref
    import ctypes
    extract_unicode_fn = c_helpers['extract_unicode']
    proto = CFUNCTYPE(c_void_p, py_object, POINTER(c_ssize_t), POINTER(c_int), POINTER(c_uint), POINTER(c_ssize_t))
    fn = proto(extract_unicode_fn)
    length = c_ssize_t()
    kind = c_int()
    is_ascii = c_uint()
    hashv = c_ssize_t()
    data = fn(obj, byref(length), byref(kind), byref(is_ascii), byref(hashv))
# WARNING: Decompyle incomplete


def make_string_from_constant(context, builder, typ, literal_string):
    '''
    Get string data by `compile_time_get_string_data()` and return a
    unicode_type LLVM value
    '''
    (databytes, length, kind, is_ascii, hashv) = compile_time_get_string_data(literal_string)
    mod = builder.module
    gv = context.insert_const_bytes(mod, databytes)
    uni_str = cgutils.create_struct_proxy(typ)(context, builder)
    uni_str.data = gv
    uni_str.length = uni_str.length.type(length)
    uni_str.kind = uni_str.kind.type(kind)
    uni_str.is_ascii = uni_str.is_ascii.type(is_ascii)
    uni_str.hash = uni_str.hash.type(-1)
    return uni_str._getvalue()

cast_from_literal = (lambda context, builder, fromty, toty, val: make_string_from_constant(context, builder, toty, fromty.literal_value))()
constant_unicode = (lambda context, builder, typ, pyval: make_string_from_constant(context, builder, typ, pyval))()
unbox_unicode_str = (lambda typ, obj, c: (ok, data, length, kind, is_ascii, hashv) = c.pyapi.string_as_string_size_and_kind(obj)uni_str = cgutils.create_struct_proxy(typ)(c.context, c.builder)uni_str.data = datauni_str.length = lengthuni_str.kind = kinduni_str.is_ascii = is_asciiuni_str.hash = hashvuni_str.meminfo = c.pyapi.nrt_meminfo_new_from_pyobject(data, obj)uni_str.parent = objis_error = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())NativeValue(uni_str._getvalue(), is_error = is_error))()
box_unicode_str = (lambda typ, val, c: uni_str = cgutils.create_struct_proxy(typ)(c.context, c.builder, value = val)res = c.pyapi.string_from_kind_and_data(uni_str.kind, uni_str.data, uni_str.length)c.pyapi.object_hash(res)c.context.nrt.decref(c.builder, typ, val)res)()

def make_deref_codegen(bitsize):
    pass
# WARNING: Decompyle incomplete

deref_uint8 = (lambda typingctx, data, offset: sig = types.uint32(types.voidptr, types.intp)(sig, make_deref_codegen(8)))()
deref_uint16 = (lambda typingctx, data, offset: sig = types.uint32(types.voidptr, types.intp)(sig, make_deref_codegen(16)))()
deref_uint32 = (lambda typingctx, data, offset: sig = types.uint32(types.voidptr, types.intp)(sig, make_deref_codegen(32)))()
_malloc_string = (lambda typingctx, kind, char_bytes, length, is_ascii: 
def details(context, builder, signature, args):
(kind_val, char_bytes_val, length_val, is_ascii_val) = argsuni_str_ctor = cgutils.create_struct_proxy(types.unicode_type)uni_str = uni_str_ctor(context, builder)nbytes_val = builder.mul(char_bytes_val, builder.add(length_val, Constant(length_val.type, 1)))uni_str.meminfo = context.nrt.meminfo_alloc(builder, nbytes_val)uni_str.kind = kind_valuni_str.is_ascii = is_ascii_valuni_str.length = length_valuni_str.hash = context.get_constant(_Py_hash_t, -1)uni_str.data = context.nrt.meminfo_data(builder, uni_str.meminfo)uni_str.parent = cgutils.get_null_value(uni_str.parent.type)uni_str._getvalue()sig = types.unicode_type(types.int32, types.intp, types.intp, types.uint32)(sig, details))()
_empty_string = (lambda kind, length, is_ascii = (0,): char_width = _kind_to_byte_width(kind)s = _malloc_string(kind, char_width, length, is_ascii)_set_code_point(s, length, np.uint32(0))s)()
_get_code_point = (lambda a, i: if a._kind == PY_UNICODE_1BYTE_KIND:
deref_uint8(a._data, i)if None._kind == PY_UNICODE_2BYTE_KIND:
deref_uint16(a._data, i)if None._kind == PY_UNICODE_4BYTE_KIND:
deref_uint32(a._data, i))()

def make_set_codegen(bitsize):
    pass
# WARNING: Decompyle incomplete

set_uint8 = (lambda typingctx, data, idx, ch: sig = types.void(types.voidptr, types.int64, types.uint32)(sig, make_set_codegen(8)))()
set_uint16 = (lambda typingctx, data, idx, ch: sig = types.void(types.voidptr, types.int64, types.uint32)(sig, make_set_codegen(16)))()
set_uint32 = (lambda typingctx, data, idx, ch: sig = types.void(types.voidptr, types.int64, types.uint32)(sig, make_set_codegen(32)))()
_set_code_point = (lambda a, i, ch: if a._kind == PY_UNICODE_1BYTE_KIND:
set_uint8(a._data, i, ch)Noneif None._kind == PY_UNICODE_2BYTE_KIND:
set_uint16(a._data, i, ch)Noneif None._kind == PY_UNICODE_4BYTE_KIND:
set_uint32(a._data, i, ch)Noneraise None('Unexpected unicode representation in _set_code_point'))()
if PYVERSION in ((3, 12), (3, 13), (3, 14)):
    _pick_kind = (lambda kind1, kind2: if kind1 == PY_UNICODE_1BYTE_KIND:
kind2if None == PY_UNICODE_2BYTE_KIND:
if kind2 == PY_UNICODE_4BYTE_KIND:
kind2Noneif None == PY_UNICODE_4BYTE_KIND:
kind1raise None('Unexpected unicode representation in _pick_kind'))()
elif PYVERSION in ((3, 10), (3, 11)):
    _pick_kind = (lambda kind1, kind2: if kind1 == PY_UNICODE_WCHAR_KIND or kind2 == PY_UNICODE_WCHAR_KIND:
raise AssertionError('PY_UNICODE_WCHAR_KIND unsupported')if kind1 == PY_UNICODE_1BYTE_KIND:
kind2if None == PY_UNICODE_2BYTE_KIND:
if kind2 == PY_UNICODE_4BYTE_KIND:
kind2Noneif None == PY_UNICODE_4BYTE_KIND:
kind1raise None('Unexpected unicode representation in _pick_kind'))()
else:
    raise NotImplementedError(PYVERSION)
_pick_ascii = (lambda is_ascii1, is_ascii2: if is_ascii1 == 1 and is_ascii2 == 1:
types.uint32(1)None.uint32(0))()
if PYVERSION in ((3, 12), (3, 13), (3, 14)):
    _kind_to_byte_width = (lambda kind: if kind == PY_UNICODE_1BYTE_KIND:
1if None == PY_UNICODE_2BYTE_KIND:
2if None == PY_UNICODE_4BYTE_KIND:
4raise None('Unexpected unicode encoding encountered'))()
elif PYVERSION in ((3, 10), (3, 11)):
    _kind_to_byte_width = (lambda kind: if kind == PY_UNICODE_1BYTE_KIND:
1if None == PY_UNICODE_2BYTE_KIND:
2if None == PY_UNICODE_4BYTE_KIND:
4if None == PY_UNICODE_WCHAR_KIND:
raise AssertionError('PY_UNICODE_WCHAR_KIND unsupported')raise AssertionError('Unexpected unicode encoding encountered'))()
else:
    raise NotImplementedError(PYVERSION)
_cmp_region = (lambda a, a_offset, b, b_offset, n: if n == 0:
0if None + n > a._length:
-1if None + n > b._length:
1for i in None(n):
a_chr = _get_code_point(a, a_offset + i)b_chr = _get_code_point(b, b_offset + i)if a_chr < b_chr:
-1if None > b_chr:
10)()
_codepoint_to_kind = (lambda cp: if cp < 256:
PY_UNICODE_1BYTE_KINDif None < 65536:
PY_UNICODE_2BYTE_KINDMAX_UNICODE = Noneif cp > MAX_UNICODE:
msg = 'Invalid codepoint. Found value greater than Unicode maximum'raise ValueError(msg)PY_UNICODE_4BYTE_KIND)()
_codepoint_is_ascii = (lambda ch: ch < 128)()
unicode_len = (lambda s: if isinstance(s, types.UnicodeType):

def len_impl(s):
s._lengthlen_impl)()
unicode_eq = (lambda a, b: if not a.is_internal or b.is_internal:
Noneif None(a, types.Optional):
check_a = a.typeelse:
check_a = aif isinstance(b, types.Optional):
check_b = b.typeelse:
check_b = baccept = (types.UnicodeType, types.StringLiteral, types.UnicodeCharSeq)a_unicode = isinstance(check_a, accept)b_unicode = isinstance(check_b, accept)if a_unicode and b_unicode:

def eq_impl(a, b):
a_none = a is Noneb_none = b is Noneif a_none or b_none:
if a_none and b_none:
TrueNonea = None(a)b = str(b)if len(a) != len(b):
FalseNone(a, 0, b, 0, len(a)) == 0eq_implif None ^ b_unicode:

def eq_impl(a, b):
Falseeq_impl)()
unicode_ne = (lambda a, b: if not a.is_internal or b.is_internal:
Noneaccept = (None.UnicodeType, types.StringLiteral, types.UnicodeCharSeq)a_unicode = isinstance(a, accept)b_unicode = isinstance(b, accept)if a_unicode and b_unicode:

def ne_impl(a, b):
not (a == b)ne_implif None ^ b_unicode:

def eq_impl(a, b):
Trueeq_impl)()
unicode_lt = (lambda a, b: a_unicode = isinstance(a, (types.UnicodeType, types.StringLiteral))b_unicode = isinstance(b, (types.UnicodeType, types.StringLiteral))if a_unicode or b_unicode:

def lt_impl(a, b):
minlen = min(len(a), len(b))eqcode = _cmp_region(a, 0, b, 0, minlen)if eqcode == -1:
Trueif None == 0:
len(a) < len(b)lt_implNone)()
unicode_gt = (lambda a, b: a_unicode = isinstance(a, (types.UnicodeType, types.StringLiteral))b_unicode = isinstance(b, (types.UnicodeType, types.StringLiteral))if a_unicode or b_unicode:

def gt_impl(a, b):
minlen = min(len(a), len(b))eqcode = _cmp_region(a, 0, b, 0, minlen)if eqcode == 1:
Trueif None == 0:
len(a) > len(b)gt_implNone)()
unicode_le = (lambda a, b: a_unicode = isinstance(a, (types.UnicodeType, types.StringLiteral))b_unicode = isinstance(b, (types.UnicodeType, types.StringLiteral))if a_unicode or b_unicode:

def le_impl(a, b):
not (a > b)le_implNone)()
unicode_ge = (lambda a, b: a_unicode = isinstance(a, (types.UnicodeType, types.StringLiteral))b_unicode = isinstance(b, (types.UnicodeType, types.StringLiteral))if a_unicode or b_unicode:

def ge_impl(a, b):
not (a < b)ge_implNone)()
unicode_contains = (lambda a, b: if isinstance(a, types.UnicodeType) or isinstance(b, types.UnicodeType):

def contains_impl(a, b):
_find(a, b) > -1contains_implNone)()

def unicode_idx_check_type(ty, name):
    '''Check object belongs to one of specific types
    ty: type
        Type of the object
    name: str
        Name of the object
    '''
    thety = ty
    if isinstance(ty, types.Omitted):
        thety = ty.value
    elif isinstance(ty, types.Optional):
        thety = ty.type
    accepted = (types.Integer, types.NoneType)
# WARNING: Decompyle incomplete


def unicode_sub_check_type(ty, name):
    '''Check object belongs to unicode type'''
    if not isinstance(ty, types.UnicodeType):
        msg = '"{}" must be {}, not {}'.format(name, types.UnicodeType, ty)
        raise TypingError(msg)

_bloom_add = (lambda mask, ch: mask |= 1 << (ch & _BLOOM_WIDTH - 1)mask)()
_bloom_check = (lambda mask, ch: mask & 1 << (ch & _BLOOM_WIDTH - 1))()
_default_find = (lambda data, substr, start, end: m = len(substr)if m == 0:
startgap = None - 1mlast = None - 1last = _get_code_point(substr, mlast)zero = types.intp(0)mask = _bloom_add(zero, last)# WARNING: Decompyle incomplete
)()
_default_rfind = (lambda data, substr, start, end: m = len(substr)if m == 0:
endskip = None - 1mlast = None - 1mfirst = _get_code_point(substr, 0)mask = _bloom_add(0, mfirst)i = mlast# WARNING: Decompyle incomplete
)()

def generate_finder(find_func):
    '''Generate finder either left or right.'''
    pass
# WARNING: Decompyle incomplete

_find = register_jitable(generate_finder(_default_find))
_rfind = register_jitable(generate_finder(_default_rfind))
unicode_find = (lambda data, substr, start, end = (None, None): if isinstance(substr, types.UnicodeCharSeq):

def find_impl(data, substr, start, end = (None, None)):
data.find(str(substr))find_implNone(start, 'start')unicode_idx_check_type(end, 'end')unicode_sub_check_type(substr, 'substr')_find)()
unicode_rfind = (lambda data, substr, start, end = (None, None): if isinstance(substr, types.UnicodeCharSeq):

def rfind_impl(data, substr, start, end = (None, None)):
data.rfind(str(substr))rfind_implNone(start, 'start')unicode_idx_check_type(end, 'end')unicode_sub_check_type(substr, 'substr')_rfind)()
unicode_rindex = (lambda s, sub, start, end = (None, None): unicode_idx_check_type(start, 'start')unicode_idx_check_type(end, 'end')unicode_sub_check_type(sub, 'sub')
def rindex_impl(s, sub, start, end = (None, None)):
result = s.rfind(sub, start, end)if result < 0:
raise ValueError('substring not found')resultrindex_impl)()
unicode_index = (lambda s, sub, start, end = (None, None): unicode_idx_check_type(start, 'start')unicode_idx_check_type(end, 'end')unicode_sub_check_type(sub, 'sub')
def index_impl(s, sub, start, end = (None, None)):
result = s.find(sub, start, end)if result < 0:
raise ValueError('substring not found')resultindex_impl)()
unicode_partition = (lambda data, sep: thety = sepif isinstance(sep, types.Omitted):
thety = sep.valueelif isinstance(sep, types.Optional):
thety = sep.typeaccepted = (types.UnicodeType, types.UnicodeCharSeq)# WARNING: Decompyle incomplete
)()
unicode_count = (lambda src, sub, start, end = (None, None): _count_args_types_check(start)_count_args_types_check(end)if isinstance(sub, types.UnicodeType):

def count_impl(src, sub, start, end = (None, None)):
count = 0src_len = len(src)sub_len = len(sub)start = _normalize_slice_idx_count(start, src_len, 0)end = _normalize_slice_idx_count(end, src_len, src_len)if end - start < 0 or start > src_len:
0src = None[start:end]src_len = len(src)end = src_lenstart = 0if sub_len == 0:
src_len + 1# WARNING: Decompyle incomplete
count_implerror_msg = Noneraise TypingError(error_msg.format(type(sub))))()
unicode_rpartition = (lambda data, sep: thety = sepif isinstance(sep, types.Omitted):
thety = sep.valueelif isinstance(sep, types.Optional):
thety = sep.typeaccepted = (types.UnicodeType, types.UnicodeCharSeq)# WARNING: Decompyle incomplete
)()
_adjust_indices = (lambda length, start, end: if end > length:
end = lengthif end < 0:
end += lengthif end < 0:
end = 0if start < 0:
start += lengthif start < 0:
start = 0(start, end))()
unicode_startswith = (lambda s, prefix, start, end = (None, None): if not is_nonelike(start) and isinstance(start, types.Integer):
raise TypingError("When specified, the arg 'start' must be an Integer or None")if not is_nonelike(end) and isinstance(end, types.Integer):
raise TypingError("When specified, the arg 'end' must be an Integer or None")if isinstance(prefix, types.UniTuple) and isinstance(prefix.dtype, types.UnicodeType):

def startswith_tuple_impl(s, prefix, start, end = (None, None)):
for item in prefix:
if s.startswith(item, start, end):
TrueFalsestartswith_tuple_implif None(prefix, types.UnicodeCharSeq):

def startswith_char_seq_impl(s, prefix, start, end = (None, None)):
s.startswith(str(prefix), start, end)startswith_char_seq_implif None(prefix, types.UnicodeType):

def startswith_unicode_impl(s, prefix, start, end = (None, None)):
prefix_length = len(prefix)length = len(s)# WARNING: Decompyle incomplete
startswith_unicode_implraise None("The arg 'prefix' should be a string or a tuple of strings"))()
unicode_endswith = (lambda s, substr, start, end = (None, None): pass# WARNING: Decompyle incomplete
)()
unicode_expandtabs = (lambda data, tabsize = (8,): thety = tabsizeif isinstance(tabsize, types.Omitted):
thety = tabsize.valueelif isinstance(tabsize, types.Optional):
thety = tabsize.typeaccepted = (types.Integer, int)# WARNING: Decompyle incomplete
)()
unicode_split = (lambda a, sep, maxsplit = (None, -1): if not maxsplit == -1 and isinstance(maxsplit, (types.Omitted, types.Integer, types.IntegerLiteral)):
Noneif None(sep, types.UnicodeCharSeq):

def split_impl(a, sep, maxsplit = (None, -1)):
a.split(str(sep), maxsplit = maxsplit)split_implif None(sep, types.UnicodeType):

def split_impl(a, sep, maxsplit = (None, -1)):
a_len = len(a)sep_len = len(sep)if sep_len == 0:
raise ValueError('empty separator')parts = []last = 0idx = 0if sep_len == 1 and maxsplit == -1:
sep_code_point = _get_code_point(sep, 0)for idx in range(a_len):
if _get_code_point(a, idx) == sep_code_point:
parts.append(a[last:idx])last = idx + 1split_count = 0# WARNING: Decompyle incomplete
split_impl# WARNING: Decompyle incomplete
)()

def generate_rsplit_whitespace_impl(isspace_func):
    '''Generate whitespace rsplit func based on either ascii or unicode'''
    pass
# WARNING: Decompyle incomplete

unicode_rsplit_whitespace_impl = register_jitable(generate_rsplit_whitespace_impl(_PyUnicode_IsSpace))
ascii_rsplit_whitespace_impl = register_jitable(generate_rsplit_whitespace_impl(_Py_ISSPACE))
unicode_rsplit = (lambda data, sep, maxsplit = (None, -1): 
def _unicode_rsplit_check_type(ty, name, accepted):
'''Check object belongs to one of specified types'''
thety = tyif isinstance(ty, types.Omitted):
thety = ty.valueelif isinstance(ty, types.Optional):
thety = ty.type# WARNING: Decompyle incomplete
_unicode_rsplit_check_type(sep, 'sep', (types.UnicodeType, types.UnicodeCharSeq, types.NoneType))_unicode_rsplit_check_type(maxsplit, 'maxsplit', (types.Integer, int))# WARNING: Decompyle incomplete
)()
unicode_center = (lambda string, width, fillchar = (' ',): if not isinstance(width, types.Integer):
raise TypingError('The width must be an Integer')if isinstance(fillchar, types.UnicodeCharSeq):

def center_impl(string, width, fillchar = (' ',)):
string.center(width, str(fillchar))center_implif not None == ' ' and isinstance(fillchar, (types.Omitted, types.UnicodeType)):
raise TypingError('The fillchar must be a UnicodeType')
def center_impl(string, width, fillchar = (' ',)):
str_len = len(string)fillchar_len = len(fillchar)if fillchar_len != 1:
raise ValueError('The fill character must be exactly one character long')if width <= str_len:
stringallmargin = None - str_lenlmargin = allmargin // 2 + (allmargin & width & 1)rmargin = allmargin - lmarginl_string = fillchar * lmarginif lmargin == rmargin:
l_string + string + l_stringNone + string + fillchar * rmargincenter_impl)()

def gen_unicode_Xjust(STRING_FIRST):
    pass
# WARNING: Decompyle incomplete

overload_method(types.UnicodeType, 'rjust')(gen_unicode_Xjust(False))
overload_method(types.UnicodeType, 'ljust')(gen_unicode_Xjust(True))

def generate_splitlines_func(is_line_break_func):
    '''Generate splitlines performer based on ascii or unicode line breaks.'''
    pass
# WARNING: Decompyle incomplete

_ascii_splitlines = register_jitable(generate_splitlines_func(_Py_ISLINEBREAK))
_unicode_splitlines = register_jitable(generate_splitlines_func(_PyUnicode_IsLineBreak))
unicode_splitlines = (lambda data, keepends = (False,): thety = keependsif isinstance(keepends, types.Omitted):
thety = keepends.valueelif isinstance(keepends, types.Optional):
thety = keepends.typeaccepted = (types.Integer, int, types.Boolean, bool)# WARNING: Decompyle incomplete
)()
join_list = (lambda sep, parts: parts_len = len(parts)if parts_len == 0:
''sep_len = None(sep)length = (parts_len - 1) * sep_lenkind = sep._kindis_ascii = sep._is_asciifor p in parts:
length += len(p)kind = _pick_kind(kind, p._kind)is_ascii = _pick_ascii(is_ascii, p._is_ascii)result = _empty_string(kind, length, is_ascii)part = parts[0]_strncpy(result, 0, part, 0, len(part))dst_offset = len(part)for idx in range(1, parts_len):
_strncpy(result, dst_offset, sep, 0, sep_len)dst_offset += sep_lenpart = parts[idx]_strncpy(result, dst_offset, part, 0, len(part))dst_offset += len(part)result)()
unicode_join = (lambda sep, parts: if isinstance(parts, types.List):
if isinstance(parts.dtype, types.UnicodeType):

def join_list_impl(sep, parts):
join_list(sep, parts)join_list_implif None(parts.dtype, types.UnicodeCharSeq):

def join_list_impl(sep, parts):
_parts = parts()join_list(sep, _parts)join_list_implNoneif None(parts, types.IterableType):

def join_iter_impl(sep, parts):
parts_list = parts()sep.join(parts_list)join_iter_implif None(parts, types.UnicodeType):

def join_str_impl(sep, parts):
pass# WARNING: Decompyle incomplete
join_str_impl)()
unicode_zfill = (lambda string, width: if not isinstance(width, types.Integer):
raise TypingError('<width> must be an Integer')
def zfill_impl(string, width):
str_len = len(string)if width <= str_len:
stringfirst_char = string[0] if None else ''padding = '0' * (width - str_len)if first_char in ('+', '-'):
newstr = first_char + padding + string[1:]else:
newstr = padding + stringnewstrzfill_impl)()
unicode_strip_left_bound = (lambda string, chars: str_len = len(string)i = 0# WARNING: Decompyle incomplete
)()
unicode_strip_right_bound = (lambda string, chars: str_len = len(string)i = 0# WARNING: Decompyle incomplete
)()

def unicode_strip_types_check(chars):
    if isinstance(chars, types.Optional):
        chars = chars.type
# WARNING: Decompyle incomplete


def _count_args_types_check(arg):
    if isinstance(arg, types.Optional):
        arg = arg.type
# WARNING: Decompyle incomplete

unicode_lstrip = (lambda string, chars = (None,): if isinstance(chars, types.UnicodeCharSeq):

def lstrip_impl(string, chars = (None,)):
string.lstrip(str(chars))lstrip_implNone(chars)
def lstrip_impl(string, chars = (None,)):
string[unicode_strip_left_bound(string, chars):]lstrip_impl)()
unicode_rstrip = (lambda string, chars = (None,): if isinstance(chars, types.UnicodeCharSeq):

def rstrip_impl(string, chars = (None,)):
string.rstrip(str(chars))rstrip_implNone(chars)
def rstrip_impl(string, chars = (None,)):
string[:unicode_strip_right_bound(string, chars)]rstrip_impl)()
unicode_strip = (lambda string, chars = (None,): if isinstance(chars, types.UnicodeCharSeq):

def strip_impl(string, chars = (None,)):
string.strip(str(chars))strip_implNone(chars)
def strip_impl(string, chars = (None,)):
lb = unicode_strip_left_bound(string, chars)rb = unicode_strip_right_bound(string, chars)string[lb:rb]strip_impl)()
normalize_str_idx = (lambda idx, length, is_start = (True,): pass# WARNING: Decompyle incomplete
)()
_normalize_slice_idx_count = (lambda arg, slice_len, default: pass# WARNING: Decompyle incomplete
)()
_normalize_slice = (lambda typingctx, sliceobj, length: sig = sliceobj(sliceobj, length)
def codegen(context, builder, sig, args):
(slicetype, lengthtype) = sig.args(sliceobj, length) = argsslice = context.make_helper(builder, slicetype, sliceobj)slicing.guard_invalid_slice(context, builder, slicetype, slice)slicing.fix_slice(builder, slice, length)slice._getvalue()(sig, codegen))()
_slice_span = (lambda typingctx, sliceobj: sig = types.intp(sliceobj)
def codegen(context, builder, sig, args):
(slicetype,) = sig.args(sliceobj,) = argsslice = context.make_helper(builder, slicetype, sliceobj)result_size = slicing.get_slice_length(builder, slice)result_size(sig, codegen))()
_strncpy = (lambda dst, dst_offset, src, src_offset, n: if src._kind == dst._kind:
byte_width = _kind_to_byte_width(src._kind)src_byte_offset = byte_width * src_offsetdst_byte_offset = byte_width * dst_offsetnbytes = n * byte_widthmemcpy_region(dst._data, dst_byte_offset, src._data, src_byte_offset, nbytes, align = 1)Nonefor i in None(n):
_set_code_point(dst, dst_offset + i, _get_code_point(src, src_offset + i))None)()
_get_str_slice_view = (lambda typingctx, src_t, start_t, length_t: pass# WARNING: Decompyle incomplete
)()
unicode_getitem = (lambda s, idx: if isinstance(s, types.UnicodeType):
if isinstance(idx, types.Integer):

def getitem_char(s, idx):
idx = normalize_str_idx(idx, len(s))cp = _get_code_point(s, idx)kind = _codepoint_to_kind(cp)if kind == s._kind:
_get_str_slice_view(s, idx, 1)is_ascii = None(cp)ret = _empty_string(kind, 1, is_ascii)_set_code_point(ret, 0, cp)retgetitem_charif None(idx, types.SliceType):

def getitem_slice(s, idx):
slice_idx = _normalize_slice(idx, len(s))span = _slice_span(slice_idx)cp = _get_code_point(s, slice_idx.start)kind = _codepoint_to_kind(cp)is_ascii = _codepoint_is_ascii(cp)for i in range(slice_idx.start + slice_idx.step, slice_idx.stop, slice_idx.step):
cp = _get_code_point(s, i)is_ascii &= _codepoint_is_ascii(cp)new_kind = _codepoint_to_kind(cp)if kind != new_kind:
kind = _pick_kind(kind, new_kind)if slice_idx.step == 1 and kind == s._kind:
_get_str_slice_view(s, slice_idx.start, span)ret = None(kind, span, is_ascii)cur = slice_idx.startfor i in range(span):
_set_code_point(ret, i, _get_code_point(s, cur))cur += slice_idx.stepretgetitem_sliceNone)()
unicode_concat = (lambda a, b: if isinstance(a, types.UnicodeType) and isinstance(b, types.UnicodeType):

def concat_impl(a, b):
new_length = a._length + b._lengthnew_kind = _pick_kind(a._kind, b._kind)new_ascii = _pick_ascii(a._is_ascii, b._is_ascii)result = _empty_string(new_kind, new_length, new_ascii)for i in range(len(a)):
_set_code_point(result, i, _get_code_point(a, i))for j in range(len(b)):
_set_code_point(result, len(a) + j, _get_code_point(b, j))resultconcat_implif None(a, types.UnicodeType) or isinstance(b, types.UnicodeCharSeq):

def concat_impl(a, b):
a + str(b)concat_implNone)()()
_repeat_impl = (lambda str_arg, mult_arg: if str_arg == '' or mult_arg < 1:
''if None == 1:
str_argnew_length = None._length * mult_argnew_kind = str_arg._kindresult = _empty_string(new_kind, new_length, str_arg._is_ascii)len_a = len(str_arg)_strncpy(result, 0, str_arg, 0, len_a)copy_size = len_a# WARNING: Decompyle incomplete
)()
unicode_repeat = (lambda a, b: if isinstance(a, types.UnicodeType) and isinstance(b, types.Integer):

def wrap(a, b):
_repeat_impl(a, b)wrapif None(a, types.Integer) or isinstance(b, types.UnicodeType):

def wrap(a, b):
_repeat_impl(b, a)wrapNone)()
unicode_not = (lambda a: if isinstance(a, types.UnicodeType):

def impl(a):
len(a) == 0impl)()
unicode_replace = (lambda s, old_str, new_str, count = (-1,): thety = countif isinstance(count, types.Omitted):
thety = count.valueelif isinstance(count, types.Optional):
thety = count.typeif not isinstance(thety, (int, types.Integer)):
raise TypingError('Unsupported parameters. The parameters must be Integer. Given count: {}'.format(count))if not isinstance(old_str, (types.UnicodeType, types.NoneType)):
raise TypingError('The object must be a UnicodeType. Given: {}'.format(old_str))if not isinstance(new_str, types.UnicodeType):
raise TypingError('The object must be a UnicodeType. Given: {}'.format(new_str))
def impl(s, old_str, new_str, count = (-1,)):
if count == 0:
sif None == '':
schars = list(s)if count == -1:
new_str + new_str.join(schars) + new_strsplit_result = [
None]min_count = min(len(schars), count)for i in range(min_count):
split_result.append(schars[i])if i + 1 != min_count:
split_result.append(new_str)continuesplit_result.append(''.join(schars[i + 1:]))if count > len(schars):
split_result.append(new_str)''.join(split_result)schars = s.split(old_str, count)result = new_str.join(schars)resultimpl)()

def gen_isAlX(ascii_func, unicode_func):
    pass
# WARNING: Decompyle incomplete

overload_method(types.UnicodeType, 'isalpha')(gen_isAlX(_Py_ISALPHA, _PyUnicode_IsAlpha))
_unicode_is_alnum = register_jitable((lambda x:
