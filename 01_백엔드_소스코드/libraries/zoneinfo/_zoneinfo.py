# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _zoneinfo.pyc (Python 3.11)

import bisect
import calendar
import collections
import functools
import re
import weakref
from datetime import datetime, timedelta, tzinfo
from  import _common, _tzpath
EPOCH = datetime(1970, 1, 1)
EPOCHORDINAL = datetime(1970, 1, 1).toordinal()
_load_timedelta = (lambda seconds: timedelta(seconds = seconds))()

class ZoneInfo(tzinfo):
    pass
# WARNING: Decompyle incomplete


class _ttinfo:
    __slots__ = [
        'utcoff',
        'dstoff',
        'tzname']
    
    def __init__(self, utcoff, dstoff, tzname):
        self.utcoff = utcoff
        self.dstoff = dstoff
        self.tzname = tzname

    
    def __eq__(self, other):
