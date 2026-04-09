# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sasreader.pyc (Python 3.11)

'''
Read SAS sas7bdat or xport files.
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import TYPE_CHECKING, Self, overload
from pandas.util._decorators import set_module
from pandas.io.common import stringify_path
if TYPE_CHECKING:
    from collections.abc import Hashable
    from types import TracebackType
    from pandas._typing import CompressionOptions, FilePath, ReadBuffer
    from pandas import DataFrame

def SASReader():
    '''SASReader'''
    __doc__ = '\n    Abstract class for XportReader and SAS7BDATReader.\n    '
    read = (lambda self = None, nrows = None: pass)()
    close = (lambda self = None: pass)()
    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        self.close()


SASReader = <NODE:27>(SASReader, 'SASReader', Iterator['DataFrame'], ABC)()
read_sas = (lambda filepath_or_buffer = None, *, format: pass)()
read_sas = (lambda filepath_or_buffer = None, *, format: pass)()
read_sas = (lambda filepath_or_buffer = None, *, format: pass# WARNING: Decompyle incomplete
)()
