# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datetime_parse.pyc (Python 3.11)

"""
Functions to parse datetime objects.

We're using regular expressions rather than time.strptime because:
- They provide both validation and parsing.
- They're more flexible for datetimes.
- The date/datetime/time constructors produce friendlier error messages.

Stolen from https://raw.githubusercontent.com/django/django/main/django/utils/dateparse.py at
9718fa2e8abe430c3526a9278dd976443d4ae3c6

Changed to:
* use standard python datetime types not django.utils.timezone
* raise ValueError when regex doesn't match rather than returning None
* support parsing unix timestamps for dates and datetimes
"""
import re
from datetime import date, datetime, time, timedelta, timezone
from typing import Dict, Optional, Type, Union
from pydantic.v1 import errors
date_expr = '(?P<year>\\d{4})-(?P<month>\\d{1,2})-(?P<day>\\d{1,2})'
time_expr = '(?P<hour>\\d{1,2}):(?P<minute>\\d{1,2})(?::(?P<second>\\d{1,2})(?:\\.(?P<microsecond>\\d{1,6})\\d{0,6})?)?(?P<tzinfo>Z|[+-]\\d{2}(?::?\\d{2})?)?$'
date_re = re.compile(f'''{date_expr}$''')
time_re = re.compile(time_expr)
datetime_re = re.compile(f'''{date_expr}[T ]{time_expr}''')
standard_duration_re = re.compile('^(?:(?P<days>-?\\d+) (days?, )?)?((?:(?P<hours>-?\\d+):)(?=\\d+:\\d+))?(?:(?P<minutes>-?\\d+):)?(?P<seconds>-?\\d+)(?:\\.(?P<microseconds>\\d{1,6})\\d{0,6})?$')
iso8601_duration_re = re.compile('^(?P<sign>[-+]?)P(?:(?P<days>\\d+(.\\d+)?)D)?(?:T(?:(?P<hours>\\d+(.\\d+)?)H)?(?:(?P<minutes>\\d+(.\\d+)?)M)?(?:(?P<seconds>\\d+(.\\d+)?)S)?)?$')
EPOCH = datetime(1970, 1, 1)
MS_WATERSHED = int(2e+10)
MAX_NUMBER = int(3e+20)
StrBytesIntFloat = Union[(str, bytes, int, float)]

def get_numeric(value = None, native_expected_type = None):
    if isinstance(value, (int, float)):
        return value
    
    try:
        return float(value)
    except ValueError:
        return None
        except TypeError:
            raise TypeError(f'''invalid type; expected {native_expected_type}, string, bytes, int or float''')



def from_unix_seconds(seconds = None):
    if seconds > MAX_NUMBER:
        return datetime.max
    if None < -MAX_NUMBER:
        return datetime.min
# WARNING: Decompyle incomplete


def _parse_timezone(value = None, error = None):
    if value == 'Z':
        return timezone.utc
# WARNING: Decompyle incomplete


def parse_date(value = None):
    """
    Parse a date/int/float/string and return a datetime.date.

    Raise ValueError if the input is well formatted but not a valid date.
    Raise ValueError if the input isn't well formatted.
    """
    if isinstance(value, date):
        if isinstance(value, datetime):
            return value.date()
        return None
    number = None(value, 'date')
# WARNING: Decompyle incomplete


def parse_time(value = None):
    """
    Parse a time/string and return a datetime.time.

    Raise ValueError if the input is well formatted but not a valid time.
    Raise ValueError if the input isn't well formatted, in particular if it contains an offset.
    """
    if isinstance(value, time):
        return value
    number = None(value, 'time')
# WARNING: Decompyle incomplete


def parse_datetime(value = None):
    """
    Parse a datetime/int/float/string and return a datetime.datetime.

    This function supports time zone offsets. When the input contains one,
    the output uses a timezone with a fixed offset from UTC.

    Raise ValueError if the input is well formatted but not a valid datetime.
    Raise ValueError if the input isn't well formatted.
    """
    if isinstance(value, datetime):
        return value
    number = None(value, 'datetime')
# WARNING: Decompyle incomplete


def parse_duration(value = None):
    """
    Parse a duration int/float/string and return a datetime.timedelta.

    The preferred format for durations in Django is '%d %H:%M:%S.%f'.

    Also supports ISO 8601 representation.
    """
    if isinstance(value, timedelta):
        return value
    if None(value, (int, float)):
        value = f'''{value:f}'''
    elif isinstance(value, bytes):
        value = value.decode()
    
    try:
        pass

    if not match:
        raise errors.DurationError()
    kw = match.groupdict()
    sign = -1 if kw.pop('sign', '+') == '-' else 1
    if kw.get('microseconds'):
        kw['microseconds'] = kw['microseconds'].ljust(6, '0')
    if kw.get('seconds') and kw.get('microseconds') and kw['seconds'].startswith('-'):
        kw['microseconds'] = '-' + kw['microseconds']
    kw_ = kw.items()()
# WARNING: Decompyle incomplete
