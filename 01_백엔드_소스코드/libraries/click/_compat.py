# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _compat.pyc (Python 3.11)

import codecs
import io
import os
import re
import sys
import typing as t
from weakref import WeakKeyDictionary
CYGWIN = sys.platform.startswith('cygwin')
WIN = sys.platform.startswith('win')
auto_wrap_for_ansi: t.Optional[t.Callable[([
    t.TextIO], t.TextIO)]] = None
_ansi_re = re.compile('\\033\\[[;?0-9]*[a-zA-Z]')

def _make_text_stream(stream = None, encoding = None, errors = None, force_readable = (False, False), force_writable = ('stream', t.BinaryIO, 'encoding', t.Optional[str], 'errors', t.Optional[str], 'force_readable', bool, 'force_writable', bool, 'return', t.TextIO)):
    pass
# WARNING: Decompyle incomplete


def is_ascii_encoding(encoding = None):
    '''Checks if a given encoding is ascii.'''
    
    try:
        return codecs.lookup(encoding).name == 'ascii'
    except LookupError:
        return False



def get_best_encoding(stream = None):
    '''Returns the default stream encoding if not found.'''
    if not getattr(stream, 'encoding', None):
        pass
    rv = sys.getdefaultencoding()
    if is_ascii_encoding(rv):
        return 'utf-8'


class _NonClosingTextIOWrapper(io.TextIOWrapper):
    pass
# WARNING: Decompyle incomplete


class _FixupStream:
    '''The new io interface needs more from streams than streams
    traditionally implement.  As such, this fix-up code is necessary in
    some circumstances.

    The forcing of readable and writable flags are there because some tools
    put badly patched objects on sys (one such offender are certain version
    of jupyter notebook).
    '''
    
    def __init__(self = None, stream = None, force_readable = None, force_writable = (False, False)):
        self._stream = stream
        self._force_readable = force_readable
        self._force_writable = force_writable

    
    def __getattr__(self = None, name = None):
        return getattr(self._stream, name)

    
    def read1(self = None, size = None):
        f = getattr(self._stream, 'read1', None)
    # WARNING: Decompyle incomplete

    
    def readable(self = None):
        if self._force_readable:
            return True
        x = None(self._stream, 'readable', None)
    # WARNING: Decompyle incomplete

    
    def writable(self = None):
        if self._force_writable:
            return True
        x = None(self._stream, 'writable', None)
    # WARNING: Decompyle incomplete

    
    def seekable(self = None):
        x = getattr(self._stream, 'seekable', None)
    # WARNING: Decompyle incomplete



def _is_binary_reader(stream = None, default = None):
    
    try:
        return isinstance(stream.read(0), bytes)
    except Exception:
        return 



def _is_binary_writer(stream = None, default = None):
    
    try:
        stream.write(b'')
    except Exception:
        stream.write('')
        return False
        except Exception:
            pass
        return 

    return True


def _find_binary_reader(stream = None):
    if _is_binary_reader(stream, False):
        return t.cast(t.BinaryIO, stream)
    buf = None(stream, 'buffer', None)
# WARNING: Decompyle incomplete


def _find_binary_writer(stream = None):
    if _is_binary_writer(stream, False):
        return t.cast(t.BinaryIO, stream)
    buf = None(stream, 'buffer', None)
# WARNING: Decompyle incomplete


def _stream_is_misconfigured(stream = None):
