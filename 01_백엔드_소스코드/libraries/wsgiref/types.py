# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

'''WSGI-related types for static type checking'''
from collections.abc import Callable, Iterable, Iterator
from types import TracebackType
from typing import Any, Protocol, TypeAlias
__all__ = [
    'StartResponse',
    'WSGIEnvironment',
    'WSGIApplication',
    'InputStream',
    'ErrorStream',
    'FileWrapper']
_ExcInfo: TypeAlias = tuple[(type[BaseException], BaseException, TracebackType)]
_OptExcInfo: TypeAlias = _ExcInfo | tuple[(None, None, None)]

class StartResponse(Protocol):
    '''start_response() callable as defined in PEP 3333'''
    
    def __call__(self = None, status = None, headers = None, exc_info = (...,)):
        pass


WSGIEnvironment: TypeAlias = dict[(str, Any)]
WSGIApplication: TypeAlias = Callable[([
    WSGIEnvironment,
    StartResponse], Iterable[bytes])]

class InputStream(Protocol):
    '''WSGI input stream as defined in PEP 3333'''
    
    def read(self = None, size = None):
        pass

    
    def readline(self = None, size = None):
        pass

    
    def readlines(self = None, hint = None):
        pass

    
    def __iter__(self = None):
        pass



class ErrorStream(Protocol):
    '''WSGI error stream as defined in PEP 3333'''
    
    def flush(self = None):
        pass

    
    def write(self = None, s = None):
        pass

    
    def writelines(self = None, seq = None):
        pass



class _Readable(Protocol):
    
    def read(self = None, size = None):
        pass



class FileWrapper(Protocol):
    '''WSGI file wrapper as defined in PEP 3333'''
    
    def __call__(self = None, file = None, block_size = None):
        pass
