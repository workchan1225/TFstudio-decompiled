# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datetime.pyc (Python 3.11)

__doc__ = 'Concrete date/time and related types.\n\nSee http://www.iana.org/time-zones/repository/tz-link.html for\ntime zone and DST data sources.\n'
__all__ = ('date', 'datetime', 'time', 'timedelta', 'timezone', 'tzinfo', 'MINYEAR', 'MAXYEAR', 'UTC')
import time as _time
import math as _math
import sys
from operator import index as _index

def _cmp(x, y):
    if x == y:
        pass
    elif x > y:
        pass
    
    return -1

MINYEAR = 1
MAXYEAR = 9999
_MAXORDINAL = 3652059
_DAYS_IN_MONTH = [
    -1,
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31]
_DAYS_BEFORE_MONTH = [
    -1]
dbm = 0
# WARNING: Decompyle incomplete
