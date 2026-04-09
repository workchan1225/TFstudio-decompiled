# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exc.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from datetime import datetime

class BadData(Exception):
    pass
# WARNING: Decompyle incomplete


class BadSignature(BadData):
    pass
# WARNING: Decompyle incomplete


class BadTimeSignature(BadSignature):
    pass
# WARNING: Decompyle incomplete


class SignatureExpired(BadTimeSignature):
    '''Raised if a signature timestamp is older than ``max_age``. This
    is a subclass of :exc:`BadTimeSignature`.
    '''
    pass


class BadHeader(BadSignature):
    pass
# WARNING: Decompyle incomplete


class BadPayload(BadData):
    pass
# WARNING: Decompyle incomplete
