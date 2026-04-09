# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tz.pyc (Python 3.11)

'''
This module offers timezone implementations subclassing the abstract
:py:class:`datetime.tzinfo` type. There are classes to handle tzfile format
files (usually are in :file:`/etc/localtime`, :file:`/usr/share/zoneinfo`,
etc), TZ environment string (in all known formats), given ranges (with help
from relative deltas), local machine timezone, fixed offset timezone, and UTC
timezone.
'''
import datetime
import struct
import time
import sys
import os
import bisect
import weakref
from collections import OrderedDict
import six
from six import string_types
from six.moves import _thread
from _common import tzname_in_python2, _tzinfo
from _common import tzrangebase, enfold
from _common import _validate_fromutc_inputs
from _factories import _TzSingleton, _TzOffsetFactory
from _factories import _TzStrFactory

try:
    from win import tzwin, tzwinlocal
except ImportError:
    tzwin = None
    tzwinlocal = None

from warnings import warn
ZERO = datetime.timedelta(0)
EPOCH = datetime.datetime(1970, 1, 1, 0, 0)
EPOCHORDINAL = EPOCH.toordinal()
tzutc = <NODE:12>()
UTC = tzutc()
tzoffset = <NODE:12>()

class tzlocal(_tzinfo):
    pass
# WARNING: Decompyle incomplete


class _ttinfo(object):
    __slots__ = [
        'offset',
        'delta',
        'isdst',
        'abbr',
        'isstd',
        'isgmt',
        'dstoffset']
    
    def __init__(self):
        for attr in self.__slots__:
            setattr(self, attr, None)
            return None

    
    def __repr__(self):
        l = []
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
