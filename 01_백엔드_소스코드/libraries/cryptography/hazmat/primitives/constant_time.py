# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: constant_time.pyc (Python 3.11)

from __future__ import annotations
import hmac

def bytes_eq(a = None, b = None):
    if not isinstance(a, bytes) or isinstance(b, bytes):
        raise TypeError('a and b must be bytes.')
    return hmac.compare_digest(a, b)
