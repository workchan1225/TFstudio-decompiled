# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: capture.pyc (Python 3.11)

'''Per-test stdout/stderr capturing mechanism.'''
from __future__ import annotations
import abc
import collections
from collections.abc import Generator
from collections.abc import Iterable
from collections.abc import Iterator
import contextlib
import io
from io import UnsupportedOperation
import os
import sys
from tempfile import TemporaryFile
from types import TracebackType
from typing import Any
from typing import AnyStr
from typing import BinaryIO
from typing import cast
from typing import Final
from typing import final
from typing import Generic
from typing import Literal
from typing import NamedTuple
from typing import TextIO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing_extensions import Self
from _pytest.config import Config
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.deprecated import check_ispytest
from _pytest.fixtures import fixture
from _pytest.fixtures import SubRequest
from _pytest.nodes import Collector
from _pytest.nodes import File
from _pytest.nodes import Item
from _pytest.reports import CollectReport
_CaptureMethod = Literal[('fd', 'sys', 'no', 'tee-sys')]

def pytest_addoption(parser = None):
    group = parser.getgroup('general')
    group.addoption('--capture', action = 'store', default = 'fd', metavar = 'method', choices = [
        'fd',
        'sys',
        'no',
        'tee-sys'], help = 'Per-test capturing method: one of fd|sys|no|tee-sys')
    group._addoption('-s', action = 'store_const', const = 'no', dest = 'capture', help = 'Shortcut for --capture=no')


def _colorama_workaround():
    '''Ensure colorama is imported so that it attaches to the correct stdio
    handles on Windows.

    colorama uses the terminal on import time. So if something does the
    first import of colorama while I/O capture is active, colorama will
    fail in various ways.
    '''
    if sys.platform.startswith('win32'):
        
        try:
            import colorama
            return None
        except ImportError:
            return None
            return None



def _readline_workaround():
    '''Ensure readline is imported early so it attaches to the correct stdio handles.

    This isn\'t a problem with the default GNU readline implementation, but in
    some configurations, Python uses libedit instead (on macOS, and for prebuilt
    binaries such as used by uv).

    In theory this is only needed if readline.backend == "libedit", but the
    workaround consists of importing readline here, so we already worked around
    the issue by the time we could check if we need to.
    '''
    
    try:
        import readline
        return None
    except ImportError:
        return None



def _windowsconsoleio_workaround(stream = None):
    '''Workaround for Windows Unicode console handling.

    Python 3.6 implemented Unicode console handling for Windows. This works
    by reading/writing to the raw console handle using
    ``{Read,Write}ConsoleW``.

    The problem is that we are going to ``dup2`` over the stdio file
    descriptors when doing ``FDCapture`` and this will ``CloseHandle`` the
    handles used by Python to write to the console. Though there is still some
    weirdness and the console handle seems to only be closed randomly and not
    on the first call to ``CloseHandle``, or maybe it gets reopened with the
    same handle value when we suspend capturing.

    The workaround in this case will reopen stdio with a different fd which
    also means a different handle by replicating the logic in
    "Py_lifecycle.c:initstdio/create_stdio".

    :param stream:
        In practice ``sys.stdout`` or ``sys.stderr``, but given
        here as parameter for unittesting purposes.

    See https://github.com/pytest-dev/py/issues/103.
    '''
    pass
# WARNING: Decompyle incomplete

pytest_load_initial_conftests = (lambda early_config = None: pass# WARNING: Decompyle incomplete
)()

class EncodedFile(io.TextIOWrapper):
    __slots__ = ()
    name = (lambda self = None: repr(self.buffer))()
    mode = (lambda self = None: pass# WARNING: Decompyle incomplete
)()


class CaptureIO(io.TextIOWrapper):
    pass
# WARNING: Decompyle incomplete


class TeeCaptureIO(CaptureIO):
    pass
# WARNING: Decompyle incomplete


class DontReadFromInput(TextIO):
    encoding = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def read(self = None, size = None):
        raise OSError('pytest: reading from stdin while output is captured!  Consider using `-s`.')

    readline = read
    
    def __next__(self = None):
        return self.readline()

    
    def readlines(self = None, hint = None):
        raise OSError('pytest: reading from stdin while output is captured!  Consider using `-s`.')

    
    def __iter__(self = None):
        return self

    
    def fileno(self = None):
        raise UnsupportedOperation('redirected stdin is pseudofile, has no fileno()')

    
    def flush(self = None):
        raise UnsupportedOperation('redirected stdin is pseudofile, has no flush()')

    
    def isatty(self = None):
        return False

    
    def close(self = None):
        pass

    
    def readable(self = None):
        return False

    
    def seek(self = None, offset = None, whence = None):
        raise UnsupportedOperation('redirected stdin is pseudofile, has no seek(int)')

    
    def seekable(self = None):
        return False

    
    def tell(self = None):
        raise UnsupportedOperation('redirected stdin is pseudofile, has no tell()')

    
    def truncate(self = None, size = None):
        raise UnsupportedOperation('cannot truncate stdin')

    
    def write(self = None, data = None):
        raise UnsupportedOperation('cannot write to stdin')

    
    def writelines(self = None, lines = None):
        raise UnsupportedOperation('Cannot write to stdin')

    
    def writable(self = None):
        return False

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, type = None, value = None, traceback = ('type', 'type[BaseException] | None', 'value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        pass

    buffer = (lambda self = None: self)()


def CaptureBase():
    '''CaptureBase'''
    EMPTY_BUFFER: 'AnyStr' = 'CaptureBase'
    __init__ = (lambda self = None, fd = None: raise NotImplementedError())()
    start = (lambda self = None: raise NotImplementedError())()
    done = (lambda self = None: raise NotImplementedError())()
    suspend = (lambda self = None: raise NotImplementedError())()
    resume = (lambda self = None: raise NotImplementedError())()
    writeorg = (lambda self = None, data = None: raise NotImplementedError())()
    snap = (lambda self = None: raise NotImplementedError())()

CaptureBase = <NODE:27>(CaptureBase, 'CaptureBase', abc.ABC, Generic[AnyStr])
patchsysdict = {
    0: 'stdin',
    1: 'stdout',
    2: 'stderr' }

def NoCapture():
    '''NoCapture'''
    EMPTY_BUFFER = ''
    
    def __init__(self = None, fd = None):
        pass

    
    def start(self = None):
        pass

    
    def done(self = None):
        pass

    
    def suspend(self = None):
        pass

    
    def resume(self = None):
        pass

    
    def snap(self = None):
        return ''

    
    def writeorg(self = None, data = None):
        pass


NoCapture = <NODE:27>(NoCapture, 'NoCapture', CaptureBase[str])

def SysCaptureBase():
    '''SysCaptureBase'''
    
    def __init__(self = None, fd = None, tmpfile = None, *, tee):
        name = patchsysdict[fd]
        self._old = getattr(sys, name)
        self.name = name
    # WARNING: Decompyle incomplete

    
    def repr(self = None, class_name = None):
