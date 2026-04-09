# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _common.pyc (Python 3.11)

from six import PY2
from functools import wraps
from datetime import datetime, timedelta, tzinfo
ZERO = timedelta(0)
__all__ = [
    'tzname_in_python2',
    'enfold']

def tzname_in_python2(namefunc):
    '''Change unicode output into bytestrings in Python 2

    tzname() API changed in Python 3. It used to return bytes, but was changed
    to unicode strings
    '''
    pass
# WARNING: Decompyle incomplete


def _validate_fromutc_inputs(f):
    '''
    The CPython version of ``fromutc`` checks that the input is a ``datetime``
    object and that ``self`` is attached as its ``tzinfo``.
    '''
    pass
# WARNING: Decompyle incomplete


class _tzinfo(tzinfo):
    '''
    Base class for all ``dateutil`` ``tzinfo`` objects.
    '''
    
    def is_ambiguous(self, dt):
