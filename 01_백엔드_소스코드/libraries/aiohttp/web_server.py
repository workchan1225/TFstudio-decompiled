# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_server.pyc (Python 3.11)

'''Low level HTTP server.'''
import asyncio
from typing import Any, Awaitable, Callable, Dict, List, Optional
from abc import AbstractStreamWriter
from http_parser import RawRequestMessage
from streams import StreamReader
from web_protocol import RequestHandler, _RequestFactory, _RequestHandler
from web_request import BaseRequest
__all__ = ('Server',)

class Server:
    
    def __init__(self = None, handler = None, *, request_factory, handler_cancellation, loop, **kwargs):
