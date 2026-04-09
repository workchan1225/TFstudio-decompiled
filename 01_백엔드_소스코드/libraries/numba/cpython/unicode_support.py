# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: unicode_support.pyc (Python 3.11)

'''
This module contains support functions for more advanced unicode operations.
This is not a public API and is for Numba internal use only. Most of the
functions are relatively straightforward translations of the functions with the
same name in CPython.
'''
from collections import namedtuple
from enum import IntEnum
import llvmlite.ir as llvmlite
import numpy as np
from numba.core import types, cgutils, config
from numba.core.imputils import impl_ret_untracked
from numba.core.extending import overload, intrinsic, register_jitable
from numba.core.errors import TypingError
typerecord = namedtuple('typerecord', 'upper lower title decimal digit flags')
if config.USE_LEGACY_TYPE_SYSTEM:
    _Py_UCS4 = types.uint32
else:
    _Py_UCS4 = types.c_uint32
_Py_TAB = 9
_Py_LINEFEED = 10
_Py_CARRIAGE_RETURN = 13
_Py_SPACE = 32

class _PyUnicode_TyperecordMasks(IntEnum):
    ALPHA_MASK = 1
    DECIMAL_MASK = 2
    DIGIT_MASK = 4
    LOWER_MASK = 8
    LINEBREAK_MASK = 16
    SPACE_MASK = 32
    TITLE_MASK = 64
    UPPER_MASK = 128
    XID_START_MASK = 256
    XID_CONTINUE_MASK = 512
    PRINTABLE_MASK = 1024
    NUMERIC_MASK = 2048
    CASE_IGNORABLE_MASK = 4096
    CASED_MASK = 8192
    EXTENDED_CASE_MASK = 16384


def _PyUnicode_gettyperecord(a):
    raise RuntimeError('Calling the Python definition is invalid')

_gettyperecord_impl = (lambda typingctx, codepoint: if not isinstance(codepoint, types.Integer):
raise TypingError('codepoint must be an integer')
def details(context, builder, signature, args):
ll_void = context.get_value_type(types.void)ll_Py_UCS4 = context.get_value_type(_Py_UCS4)ll_intc = context.get_value_type(types.intc)ll_intc_ptr = ll_intc.as_pointer()ll_uchar = context.get_value_type(types.uchar)ll_uchar_ptr = ll_uchar.as_pointer()ll_ushort = context.get_value_type(types.ushort)ll_ushort_ptr = ll_ushort.as_pointer()fnty = llvmlite.ir.FunctionType(ll_void, [
ll_Py_UCS4,
ll_intc_ptr,
ll_intc_ptr,
ll_intc_ptr,
ll_uchar_ptr,
ll_uchar_ptr,
ll_ushort_ptr])fn = cgutils.get_or_insert_function(builder.module, fnty, name = 'numba_gettyperecord')upper = cgutils.alloca_once(builder, ll_intc, name = 'upper')lower = cgutils.alloca_once(builder, ll_intc, name = 'lower')title = cgutils.alloca_once(builder, ll_intc, name = 'title')decimal = cgutils.alloca_once(builder, ll_uchar, name = 'decimal')digit = cgutils.alloca_once(builder, ll_uchar, name = 'digit')flags = cgutils.alloca_once(builder, ll_ushort, name = 'flags')byref = [
upper,
lower,
title,
decimal,
digit,
flags]builder.call(fn, [
args[0]] + byref)buf = []for x in byref:
buf.append(builder.load(x))res = context.make_tuple(builder, signature.return_type, tuple(buf))impl_ret_untracked(context, builder, signature.return_type, res)tupty = types.NamedTuple([
types.intc,
types.intc,
types.intc,
types.uchar,
types.uchar,
types.ushort], typerecord)sig = tupty(_Py_UCS4)(sig, details))()
gettyperecord_impl = (lambda a: pass# WARNING: Decompyle incomplete
)()
_PyUnicode_ExtendedCase = (lambda typingctx, index: if not isinstance(index, types.Integer):
raise TypingError('Expected an index')
def details(context, builder, signature, args):
ll_Py_UCS4 = context.get_value_type(_Py_UCS4)ll_intc = context.get_value_type(types.intc)fnty = llvmlite.ir.FunctionType(ll_Py_UCS4, [
ll_intc])fn = cgutils.get_or_insert_function(builder.module, fnty, name = 'numba_get_PyUnicode_ExtendedCase')builder.call(fn, [
args[0]])sig = _Py_UCS4(types.intc)(sig, details))()
_PyUnicode_ToTitlecase = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)if ctype.flags & _PyUnicode_TyperecordMasks.EXTENDED_CASE_MASK:
_PyUnicode_ExtendedCase(ctype.title & 65535)None + ctype.title)()
_PyUnicode_IsTitlecase = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.TITLE_MASK != 0)()
_PyUnicode_IsXidStart = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.XID_START_MASK != 0)()
_PyUnicode_IsXidContinue = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.XID_CONTINUE_MASK != 0)()
_PyUnicode_ToDecimalDigit = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)if ctype.flags & _PyUnicode_TyperecordMasks.DECIMAL_MASK:
ctype.decimal)()
_PyUnicode_ToDigit = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)if ctype.flags & _PyUnicode_TyperecordMasks.DIGIT_MASK:
ctype.digit)()
_PyUnicode_IsNumeric = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.NUMERIC_MASK != 0)()
_PyUnicode_IsPrintable = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.PRINTABLE_MASK != 0)()
_PyUnicode_IsLowercase = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.LOWER_MASK != 0)()
_PyUnicode_IsUppercase = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.UPPER_MASK != 0)()
_PyUnicode_IsLineBreak = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.LINEBREAK_MASK != 0)()
_PyUnicode_ToUppercase = (lambda ch: raise NotImplementedError)()
_PyUnicode_ToLowercase = (lambda ch: raise NotImplementedError)()
_PyUnicode_ToLowerFull = (lambda ch, res: ctype = _PyUnicode_gettyperecord(ch)if ctype.flags & _PyUnicode_TyperecordMasks.EXTENDED_CASE_MASK:
index = ctype.lower & 65535n = ctype.lower >> 24for i in range(n):
res[i] = _PyUnicode_ExtendedCase(index + i)nres[0] = ch + ctype.lower1)()
_PyUnicode_ToTitleFull = (lambda ch, res: ctype = _PyUnicode_gettyperecord(ch)if ctype.flags & _PyUnicode_TyperecordMasks.EXTENDED_CASE_MASK:
index = ctype.title & 65535n = ctype.title >> 24for i in range(n):
res[i] = _PyUnicode_ExtendedCase(index + i)nres[0] = ch + ctype.title1)()
_PyUnicode_ToUpperFull = (lambda ch, res: ctype = _PyUnicode_gettyperecord(ch)if ctype.flags & _PyUnicode_TyperecordMasks.EXTENDED_CASE_MASK:
index = ctype.upper & 65535n = ctype.upper >> 24for i in range(n):
res[i] = _PyUnicode_ExtendedCase(index + i)nres[0] = ch + ctype.upper1)()
_PyUnicode_ToFoldedFull = (lambda ch, res: ctype = _PyUnicode_gettyperecord(ch)extended_case_mask = _PyUnicode_TyperecordMasks.EXTENDED_CASE_MASKif ctype.flags & extended_case_mask and ctype.lower >> 20 & 7:
index = (ctype.lower & 65535) + (ctype.lower >> 24)n = ctype.lower >> 20 & 7for i in range(n):
res[i] = _PyUnicode_ExtendedCase(index + i)n_PyUnicode_ToLowerFull(ch, res))()
_PyUnicode_IsCased = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.CASED_MASK != 0)()
_PyUnicode_IsCaseIgnorable = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.CASE_IGNORABLE_MASK != 0)()
_PyUnicode_IsDigit = (lambda ch: if _PyUnicode_ToDigit(ch) < 0:
0)()
_PyUnicode_IsDecimalDigit = (lambda ch: if _PyUnicode_ToDecimalDigit(ch) < 0:
0)()
_PyUnicode_IsSpace = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.SPACE_MASK != 0)()
_PyUnicode_IsAlpha = (lambda ch: ctype = _PyUnicode_gettyperecord(ch)ctype.flags & _PyUnicode_TyperecordMasks.ALPHA_MASK != 0)()

class _PY_CTF(IntEnum):
    LOWER = 1
    UPPER = 2
    ALPHA = 3
    DIGIT = 4
    ALNUM = 7
    SPACE = 8
    XDIGIT = 16

_Py_ctype_table = [][0][0][0][0][0][0][0][0][0][_PY_CTF.SPACE][_PY_CTF.SPACE][_PY_CTF.SPACE][_PY_CTF.SPACE][_PY_CTF.SPACE][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][_PY_CTF.SPACE][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][0][0][0][0][0][0][0][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][0][0][0][0][0][0][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0]([][0][0][0][0][0][0][0][0][0][_PY_CTF.SPACE][_PY_CTF.SPACE][_PY_CTF.SPACE][_PY_CTF.SPACE][_PY_CTF.SPACE][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][_PY_CTF.SPACE][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][_PY_CTF.DIGIT | _PY_CTF.XDIGIT][0][0][0][0][0][0][0][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER | _PY_CTF.XDIGIT][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][_PY_CTF.UPPER][0][0][0][0][0][0][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER | _PY_CTF.XDIGIT][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][_PY_CTF.LOWER][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0], dtype = np.intc)
_Py_ctype_tolower = np.array([
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    121,
    122,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    121,
    122,
    123,
    124,
    125,
    126,
    127,
    128,
    129,
    130,
    131,
    132,
    133,
    134,
    135,
    136,
    137,
    138,
    139,
    140,
    141,
    142,
    143,
    144,
    145,
    146,
    147,
    148,
    149,
    150,
    151,
    152,
    153,
    154,
    155,
    156,
    157,
    158,
    159,
    160,
    161,
    162,
    163,
    164,
    165,
    166,
    167,
    168,
    169,
    170,
    171,
    172,
    173,
    174,
    175,
    176,
    177,
    178,
    179,
    180,
    181,
    182,
    183,
    184,
    185,
    186,
    187,
    188,
    189,
    190,
    191,
    192,
    193,
    194,
    195,
    196,
    197,
    198,
    199,
    200,
    201,
    202,
    203,
    204,
    205,
    206,
    207,
    208,
    209,
    210,
    211,
    212,
    213,
    214,
    215,
    216,
    217,
    218,
    219,
    220,
    221,
    222,
    223,
    224,
    225,
    226,
    227,
    228,
    229,
    230,
    231,
    232,
    233,
    234,
    235,
    236,
    237,
    238,
    239,
    240,
    241,
    242,
    243,
    244,
    245,
    246,
    247,
    248,
    249,
    250,
    251,
    252,
    253,
    254,
    255], dtype = np.uint8)
_Py_ctype_toupper = np.array([
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    123,
    124,
    125,
    126,
    127,
    128,
    129,
    130,
    131,
    132,
    133,
    134,
    135,
    136,
    137,
    138,
    139,
    140,
    141,
    142,
    143,
    144,
    145,
    146,
    147,
    148,
    149,
    150,
    151,
    152,
    153,
    154,
    155,
    156,
    157,
    158,
    159,
    160,
    161,
    162,
    163,
    164,
    165,
    166,
    167,
    168,
    169,
    170,
    171,
    172,
    173,
    174,
    175,
    176,
    177,
    178,
    179,
    180,
    181,
    182,
    183,
    184,
    185,
    186,
    187,
    188,
    189,
    190,
    191,
    192,
    193,
    194,
    195,
    196,
    197,
    198,
    199,
    200,
    201,
    202,
    203,
    204,
    205,
    206,
    207,
    208,
    209,
    210,
    211,
    212,
    213,
    214,
    215,
    216,
    217,
    218,
    219,
    220,
    221,
    222,
    223,
    224,
    225,
    226,
    227,
    228,
    229,
    230,
    231,
    232,
    233,
    234,
    235,
    236,
    237,
    238,
    239,
    240,
    241,
    242,
    243,
    244,
    245,
    246,
    247,
    248,
    249,
    250,
    251,
    252,
    253,
    254,
    255], dtype = np.uint8)

class _PY_CTF_LB(IntEnum):
    LINE_BREAK = 1
    LINE_FEED = 2
    CARRIAGE_RETURN = 4

_Py_ctype_islinebreak = [][0][0][0][0][0][0][0][0][0][0][_PY_CTF_LB.LINE_BREAK | _PY_CTF_LB.LINE_FEED][_PY_CTF_LB.LINE_BREAK][_PY_CTF_LB.LINE_BREAK][_PY_CTF_LB.LINE_BREAK | _PY_CTF_LB.CARRIAGE_RETURN][0][0][0][0][0][0][0][0][0][0][0][0][0][0][_PY_CTF_LB.LINE_BREAK][_PY_CTF_LB.LINE_BREAK][_PY_CTF_LB.LINE_BREAK][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][_PY_CTF_LB.LINE_BREAK][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0]([][0][0][0][0][0][0][0][0][0][0][_PY_CTF_LB.LINE_BREAK | _PY_CTF_LB.LINE_FEED][_PY_CTF_LB.LINE_BREAK][_PY_CTF_LB.LINE_BREAK][_PY_CTF_LB.LINE_BREAK | _PY_CTF_LB.CARRIAGE_RETURN][0][0][0][0][0][0][0][0][0][0][0][0][0][0][_PY_CTF_LB.LINE_BREAK][_PY_CTF_LB.LINE_BREAK][_PY_CTF_LB.LINE_BREAK][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][_PY_CTF_LB.LINE_BREAK][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0], dtype = np.intc)
_Py_CHARMASK = (lambda ch: types.uint8(ch) & types.uint8(255))()
_Py_TOUPPER = (lambda ch: _Py_ctype_toupper[_Py_CHARMASK(ch)])()
_Py_TOLOWER = (lambda ch: _Py_ctype_tolower[_Py_CHARMASK(ch)])()
_Py_ISLOWER = (lambda ch: _Py_ctype_table[_Py_CHARMASK(ch)] & _PY_CTF.LOWER)()
_Py_ISUPPER = (lambda ch: _Py_ctype_table[_Py_CHARMASK(ch)] & _PY_CTF.UPPER)()
_Py_ISALPHA = (lambda ch: _Py_ctype_table[_Py_CHARMASK(ch)] & _PY_CTF.ALPHA)()
_Py_ISDIGIT = (lambda ch: _Py_ctype_table[_Py_CHARMASK(ch)] & _PY_CTF.DIGIT)()
_Py_ISXDIGIT = (lambda ch: _Py_ctype_table[_Py_CHARMASK(ch)] & _PY_CTF.XDIGIT)()
_Py_ISALNUM = (lambda ch: _Py_ctype_table[_Py_CHARMASK(ch)] & _PY_CTF.ALNUM)()
_Py_ISSPACE = (lambda ch: _Py_ctype_table[_Py_CHARMASK(ch)] & _PY_CTF.SPACE)()
_Py_ISLINEBREAK = (lambda ch: _Py_ctype_islinebreak[_Py_CHARMASK(ch)] & _PY_CTF_LB.LINE_BREAK)()
_Py_ISLINEFEED = (lambda ch: _Py_ctype_islinebreak[_Py_CHARMASK(ch)] & _PY_CTF_LB.LINE_FEED)()
_Py_ISCARRIAGERETURN = (lambda ch: _Py_ctype_islinebreak[_Py_CHARMASK(ch)] & _PY_CTF_LB.CARRIAGE_RETURN)()
