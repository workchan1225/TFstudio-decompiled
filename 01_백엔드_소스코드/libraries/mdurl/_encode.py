# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _encode.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Sequence
from string import ascii_letters, digits, hexdigits
from urllib.parse import quote as encode_uri_component
ASCII_LETTERS_AND_DIGITS = ascii_letters + digits
ENCODE_DEFAULT_CHARS = ";/?:@&=+$,-_.!~*'()#"
ENCODE_COMPONENT_CHARS = "-_.!~*'()"
encode_cache: 'dict[str, list[str]]' = { }

def get_encode_cache(exclude = None):
    if exclude in encode_cache:
        return encode_cache[exclude]
    cache = None
    encode_cache[exclude] = cache
    for i in range(128):
        ch = chr(i)
        if ch in ASCII_LETTERS_AND_DIGITS:
            cache.append(ch)
            continue
        cache.append('%' + '0' + hex(i)[2:].upper()[-2:])
        for i in range(len(exclude)):
            cache[ord(exclude[i])] = exclude[i]
            return cache


def encode(string = None, exclude = None, *, keep_escaped):
    result = ''
    cache = get_encode_cache(exclude)
    l = len(string)
    i = 0
# WARNING: Decompyle incomplete
