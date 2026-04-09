# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _resources.pyc (Python 3.11)

from __future__ import annotations
from abc import ABCMeta, abstractmethod
from types import TracebackType
from typing import TypeVar
T = TypeVar('T')

def AsyncResource():
    '''AsyncResource'''
    __doc__ = '\n    Abstract base class for all closeable asynchronous resources.\n\n    Works as an asynchronous context manager which returns the instance itself on enter,\n    and calls :meth:`aclose` on exit.\n    '
    __slots__ = ()
    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    aclose = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

AsyncResource = <NODE:27>(AsyncResource, 'AsyncResource', metaclass = ABCMeta)
