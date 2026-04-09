# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from __future__ import annotations
import enum
import sys
import types
import typing
import warnings
from collections.abc import Callable, Sequence

class CryptographyDeprecationWarning(UserWarning):
    pass

DeprecatedIn36 = CryptographyDeprecationWarning
DeprecatedIn40 = CryptographyDeprecationWarning
DeprecatedIn41 = CryptographyDeprecationWarning
DeprecatedIn42 = CryptographyDeprecationWarning
DeprecatedIn43 = CryptographyDeprecationWarning

def _check_bytes(name = None, value = None):
    if not isinstance(value, bytes):
        raise TypeError(f'''{name} must be bytes''')


def _check_byteslike(name = None, value = None):
    
    try:
        memoryview(value)
        return None
    except TypeError:
        raise TypeError(f'''{name} must be bytes-like''')



def int_to_bytes(integer = None, length = None):
