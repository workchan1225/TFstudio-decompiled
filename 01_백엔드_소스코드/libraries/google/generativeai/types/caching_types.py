# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: caching_types.pyc (Python 3.11)

from __future__ import annotations
import datetime
from typing import Union
from typing_extensions import TypedDict
__all__ = [
    'ExpireTime',
    'TTL',
    'TTLTypes',
    'ExpireTimeTypes']

class TTL(TypedDict):
    nanos: 'int' = 'TTL'


class ExpireTime(TypedDict):
    nanos: 'int' = 'ExpireTime'

TTLTypes = Union[(TTL, int, datetime.timedelta)]
ExpireTimeTypes = Union[(ExpireTime, int, datetime.datetime)]

def to_optional_ttl(ttl = None):
    pass
# WARNING: Decompyle incomplete


def to_optional_expire_time(expire_time = None):
    pass
# WARNING: Decompyle incomplete
