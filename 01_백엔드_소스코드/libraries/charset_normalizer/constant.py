# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: constant.pyc (Python 3.11)

from __future__ import annotations
from codecs import BOM_UTF8, BOM_UTF16_BE, BOM_UTF16_LE, BOM_UTF32_BE, BOM_UTF32_LE
from encodings.aliases import aliases
from re import IGNORECASE
from re import compile as re_compile
ENCODING_MARKS: 'dict[str, bytes | list[bytes]]' = {
    'utf_8': BOM_UTF8,
    'utf_7': [
        b'+/v8',
        b'+/v9',
        b'+/v+',
        b'+/v/',
        b'+/v8-'],
    'gb18030': b'\x841\x953',
    'utf_32': [
        BOM_UTF32_BE,
        BOM_UTF32_LE],
    'utf_16': [
        BOM_UTF16_BE,
        BOM_UTF16_LE] }
TOO_SMALL_SEQUENCE: 'int' = 32
TOO_BIG_SEQUENCE: 'int' = int(1e+07)
UTF8_MAXIMAL_ALLOCATION: 'int' = 1112064
# WARNING: Decompyle incomplete
