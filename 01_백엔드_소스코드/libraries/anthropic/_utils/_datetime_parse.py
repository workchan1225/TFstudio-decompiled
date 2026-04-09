# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _datetime_parse.pyc (Python 3.11)

'''
This file contains code from https://github.com/pydantic/pydantic/blob/main/pydantic/v1/datetime_parse.py
without the Pydantic v1 specific errors.
'''
from __future__ import annotations
import re
from typing import Dict, Union, Optional
from datetime import date, datetime, timezone, timedelta
from _types import StrBytesIntFloat
date_expr = '(?P<year>\\d{4})-(?P<month>\\d{1,2})-(?P<day>\\d{1,2})'
time_expr = '(?P<hour>\\d{1,2}):(?P<minute>\\d{1,2})(?::(?P<second>\\d{1,2})(?:\\.(?P<microsecond>\\d{1,6})\\d{0,6})?)?(?P<tzinfo>Z|[+-]\\d{2}(?::?\\d{2})?)?$'
date_re = re.compile(f'''{date_expr}$''')
datetime_re = re.compile(f'''{date_expr}[T ]{time_expr}''')
EPOCH = datetime(1970, 1, 1)
MS_WATERSHED = int(2e+10)
MAX_NUMBER = int(3e+20)

def _get_numeric(value = None, native_expected_type = None):
    if isinstance(value, (int, float)):
        return value
    
    try:
        return float(value)
    except ValueError:
        return None
        except TypeError:
            raise TypeError(f'''invalid type; expected {native_expected_type}, string, bytes, int or float'''), None



def _from_unix_seconds(seconds = None):
    if seconds > MAX_NUMBER:
        return datetime.max
    if None < -MAX_NUMBER:
        return datetime.min
# WARNING: Decompyle incomplete


def _parse_timezone(value = None):
    if value == 'Z':
        return timezone.utc
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
