# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dbapi2.pyc (Python 3.11)

import datetime
import time
import collections.abc as collections
from _sqlite3 import *
paramstyle = 'qmark'
apilevel = '2.0'
Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime

def DateFromTicks(ticks):
    pass
# WARNING: Decompyle incomplete


def TimeFromTicks(ticks):
    pass
# WARNING: Decompyle incomplete


def TimestampFromTicks(ticks):
    pass
# WARNING: Decompyle incomplete

version_info = (lambda .0: [ int(x) for x in .0 ])(version.split('.')())
sqlite_version_info = (lambda .0: [ int(x) for x in .0 ])(sqlite_version.split('.')())
Binary = memoryview
collections.abc.Sequence.register(Row)

def register_adapters_and_converters():
    
    def adapt_date(val):
        return val.isoformat()

    
    def adapt_datetime(val):
        return val.isoformat(' ')

    
    def convert_date(val):
        pass
    # WARNING: Decompyle incomplete

    
    def convert_timestamp(val):
        (datepart, timepart) = val.split(b' ')
        (year, month, day) = map(int, datepart.split(b'-'))
        timepart_full = timepart.split(b'.')
        (hours, minutes, seconds) = map(int, timepart_full[0].split(b':'))
        if len(timepart_full) == 2:
            microseconds = int('{:0<6.6}'.format(timepart_full[1].decode()))
        else:
            microseconds = 0
        val = datetime.datetime(year, month, day, hours, minutes, seconds, microseconds)
        return val

    register_adapter(datetime.date, adapt_date)
    register_adapter(datetime.datetime, adapt_datetime)
    register_converter('date', convert_date)
    register_converter('timestamp', convert_timestamp)

register_adapters_and_converters()

def enable_shared_cache(enable):
    _old_enable_shared_cache = enable_shared_cache
    import _sqlite3
    import warnings
    msg = 'enable_shared_cache is deprecated and will be removed in Python 3.12. Shared cache is strongly discouraged by the SQLite 3 documentation. If shared cache must be used, open the database in URI mode usingthe cache=shared query parameter.'
    warnings.warn(msg, DeprecationWarning, stacklevel = 2)
    return _old_enable_shared_cache(enable)

del register_adapters_and_converters
