# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: encoding.pyc (Python 3.11)

from __future__ import annotations
import base64
import string
import struct
import typing as t
from exc import BadData

def want_bytes(s = None, encoding = None, errors = None):
    if isinstance(s, str):
        s = s.encode(encoding, errors)
    return s


def base64_encode(string = None):
    '''Base64 encode a string of bytes or text. The resulting bytes are
    safe to use in URLs.
    '''
    string = want_bytes(string)
    return base64.urlsafe_b64encode(string).rstrip(b'=')


def base64_decode(string = None):
    '''Base64 decode a URL-safe string of bytes or text. The result is
    bytes.
    '''
    string = want_bytes(string, encoding = 'ascii', errors = 'ignore')
    string += b'=' * (-len(string) % 4)
    
    try:
        return base64.urlsafe_b64decode(string)
    except (TypeError, ValueError):
        e = None
        raise BadData('Invalid base64-encoded data'), e
        e = None
        del e


_base64_alphabet = f'''{string.ascii_letters}{string.digits}-_='''.encode('ascii')
_int64_struct = struct.Struct('>Q')
_int_to_bytes = _int64_struct.pack
_bytes_to_int = t.cast('t.Callable[[bytes], tuple[int]]', _int64_struct.unpack)

def int_to_bytes(num = None):
    return _int_to_bytes(num).lstrip(b'\x00')


def bytes_to_int(bytestr = None):
    return _bytes_to_int(bytestr.rjust(8, b'\x00'))[0]
