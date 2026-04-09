# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _util.pyc (Python 3.11)

'''Utility classes for Mutagen.

You should not rely on the interfaces here being stable. They are
intended for internal use in Mutagen only.
'''
import sys
import struct
import codecs
import errno
import decimal
from io import BytesIO
from typing import Tuple, List
from collections import namedtuple
from contextlib import contextmanager
from functools import wraps
from fnmatch import fnmatchcase
_DEFAULT_BUFFER_SIZE = 1048576

def endswith(text, end):
    if isinstance(text, str):
        if not isinstance(end, str):
            end = end.decode('ascii')
        elif not isinstance(end, bytes):
            end = end.encode('ascii')
    return text.endswith(end)


def reraise(tp, value, tb):
    raise tp(value).with_traceback(tb)


def bchr(x):
    return bytes([
        x])


def iterbytes(b):
    return b()


def intround(value = None):
    '''Given a float returns a rounded int. Should give the same result on
    both Py2/3
    '''
    return int(decimal.Decimal.from_float(value).to_integral_value(decimal.ROUND_HALF_EVEN))


def is_fileobj(fileobj = None):
