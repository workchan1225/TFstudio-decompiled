# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _internal.pyc (Python 3.11)

from __future__ import annotations
import logging
import re
import sys
import typing as t
from datetime import datetime
from datetime import timezone
if t.TYPE_CHECKING:
    from _typeshed.wsgi import WSGIEnvironment
    from wrappers.request import Request
_logger: 'logging.Logger | None' = None

class _Missing:
    
    def __repr__(self = None):
        return 'no value'

    
    def __reduce__(self = None):
        return '_missing'


_missing = _Missing()

def _wsgi_decoding_dance(s = None):
    return s.encode('latin1').decode(errors = 'replace')


def _wsgi_encoding_dance(s = None):
    return s.encode().decode('latin1')


def _get_environ(obj = None):
    env = getattr(obj, 'environ', obj)
# WARNING: Decompyle incomplete


def _has_level_handler(logger = None):
    """Check if there is a handler in the logging chain that will handle
    the given logger's effective level.
    """
    pass
# WARNING: Decompyle incomplete


class _ColorStreamHandler(logging.StreamHandler):
    pass
# WARNING: Decompyle incomplete


def _log(type = None, message = None, *args, **kwargs):
    """Log a message to the 'werkzeug' logger.

    The logger is created the first time it is needed. If there is no
    level set, it is set to :data:`logging.INFO`. If there is no handler
    for the logger's effective level, a :class:`logging.StreamHandler`
    is added.
    """
    pass
# WARNING: Decompyle incomplete

_dt_as_utc = (lambda dt = None: pass)()
_dt_as_utc = (lambda dt = None: pass)()

def _dt_as_utc(dt = None):
    pass
# WARNING: Decompyle incomplete

_TAccessorValue = t.TypeVar('_TAccessorValue')

def _DictAccessorProperty():
    '''_DictAccessorProperty'''
    __doc__ = 'Baseclass for `environ_property` and `header_property`.'
    read_only = False
    
    def __init__(self, name, default = None, load_func = None, dump_func = None, read_only = (None, None, None, None, None), doc = ('name', 'str', 'default', '_TAccessorValue | None', 'load_func', 't.Callable[[str], _TAccessorValue] | None', 'dump_func', 't.Callable[[_TAccessorValue], str] | None', 'read_only', 'bool | None', 'doc', 'str | None', 'return', 'None')):
        self.name = name
        self.default = default
        self.load_func = load_func
        self.dump_func = dump_func
    # WARNING: Decompyle incomplete

    
    def lookup(self = None, instance = None):
        raise NotImplementedError

    __get__ = (lambda self = None, instance = None, owner = t.overload: pass)()
    __get__ = (lambda self = None, instance = None, owner = t.overload: pass)()
    
    def __get__(self = None, instance = None, owner = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __set__(self = None, instance = None, value = None):
        if self.read_only:
            raise AttributeError('read only property')
    # WARNING: Decompyle incomplete

    
    def __delete__(self = None, instance = None):
        if self.read_only:
            raise AttributeError('read only property')
        self.lookup(instance).pop(self.name, None)

    
    def __repr__(self = None):
        return f'''<{type(self).__name__} {self.name}>'''


_DictAccessorProperty = <NODE:27>(_DictAccessorProperty, '_DictAccessorProperty', t.Generic[_TAccessorValue])
_plain_int_re = re.compile('-?\\d+', re.ASCII)

def _plain_int(value = None):
    '''Parse an int only if it is only ASCII digits and ``-``.

    This disallows ``+``, ``_``, and non-ASCII digits, which are accepted by ``int`` but
    are not allowed in HTTP header values.

    Any leading or trailing whitespace is stripped
    '''
    value = value.strip()
# WARNING: Decompyle incomplete
