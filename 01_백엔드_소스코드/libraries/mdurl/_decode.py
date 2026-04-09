# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _decode.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Sequence
import functools
import re
DECODE_DEFAULT_CHARS = ';/?:@&=+$,#'
DECODE_COMPONENT_CHARS = ''
decode_cache: 'dict[str, list[str]]' = { }

def get_decode_cache(exclude = None):
    if exclude in decode_cache:
        return decode_cache[exclude]
    cache = None
    decode_cache[exclude] = cache
    for i in range(128):
        ch = chr(i)
        cache.append(ch)
        for i in range(len(exclude)):
            ch_code = ord(exclude[i])
            cache[ch_code] = '%' + '0' + hex(ch_code)[2:].upper()[-2:]
            return cache


def decode(string = None, exclude = None):
    cache = get_decode_cache(exclude)
    repl_func = functools.partial(repl_func_with_cache, cache = cache)
    return re.sub('(%[a-f0-9]{2})+', repl_func, string, flags = re.IGNORECASE)


def repl_func_with_cache(match = None, cache = None):
    seq = match.group()
    result = ''
    i = 0
    l = len(seq)
# WARNING: Decompyle incomplete
