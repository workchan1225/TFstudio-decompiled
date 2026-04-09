# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _trace.pyc (Python 3.11)

from __future__ import annotations
import inspect
import logging
import types
import typing
from _models import Request

class Trace:
    
    def __init__(self = None, name = None, logger = None, request = (None, None), kwargs = ('name', 'str', 'logger', 'logging.Logger', 'request', 'Request | None', 'kwargs', 'dict[str, typing.Any] | None', 'return', 'None')):
        self.name = name
        self.logger = logger
    # WARNING: Decompyle incomplete

    
    def trace(self = None, name = None, info = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        if self.should_trace:
            info = self.kwargs
            self.trace(f'''{self.name}.started''', info)
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def atrace(self = None, name = None, info = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete
