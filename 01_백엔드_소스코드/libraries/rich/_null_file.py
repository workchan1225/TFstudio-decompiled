# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _null_file.pyc (Python 3.11)

from types import TracebackType
from typing import IO, Iterable, Iterator, List, Optional, Type

def NullFile():
    '''NullFile'''
    
    def close(self = None):
        pass

    
    def isatty(self = None):
        return False

    
    def read(self = None, _NullFile__n = None):
        return ''

    
    def readable(self = None):
        return False

    
    def readline(self = None, _NullFile__limit = None):
        return ''

    
    def readlines(self = None, _NullFile__hint = None):
        return []

    
    def seek(self = None, _NullFile__offset = None, _NullFile__whence = None):
        return 0

    
    def seekable(self = None):
        return False

    
    def tell(self = None):
        return 0

    
    def truncate(self = None, _NullFile__size = None):
        return 0

    
    def writable(self = None):
        return False

    
    def writelines(self = None, _NullFile__lines = None):
        pass

    
    def __next__(self = None):
        return ''

    
    def __iter__(self = None):
        return iter([
            ''])

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, _NullFile__t = None, _NullFile__value = None, _NullFile__traceback = ('_NullFile__t', Optional[Type[BaseException]], '_NullFile__value', Optional[BaseException], '_NullFile__traceback', Optional[TracebackType], 'return', None)):
        pass

    
    def write(self = None, text = None):
        return 0

    
    def flush(self = None):
        pass

    
    def fileno(self = None):
        return -1


NullFile = <NODE:27>(NullFile, 'NullFile', IO[str])
NULL_FILE = NullFile()
