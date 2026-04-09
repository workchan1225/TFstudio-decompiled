# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mock.pyc (Python 3.11)

from __future__ import annotations
import typing
from _models import Request, Response
from base import AsyncBaseTransport, BaseTransport
SyncHandler = typing.Callable[([
    Request], Response)]
AsyncHandler = typing.Callable[([
    Request], typing.Coroutine[(None, None, Response)])]
__all__ = [
    'MockTransport']

class MockTransport(BaseTransport, AsyncBaseTransport):
    
    def __init__(self = None, handler = None):
        self.handler = handler

    
    def handle_request(self = None, request = None):
        request.read()
        response = self.handler(request)
        if not isinstance(response, Response):
            raise TypeError('Cannot use an async handler in a sync Client')
        return response

    
    async def handle_async_request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete
