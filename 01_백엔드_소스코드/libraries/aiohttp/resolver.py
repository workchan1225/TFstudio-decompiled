# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: resolver.pyc (Python 3.11)

import asyncio
import socket
import weakref
from typing import Any, Dict, Final, List, Optional, Tuple, Type, Union
from abc import AbstractResolver, ResolveResult
__all__ = ('ThreadedResolver', 'AsyncResolver', 'DefaultResolver')

try:
    import aiodns
    aiodns_default = hasattr(aiodns.DNSResolver, 'getaddrinfo')
except ImportError:
    aiodns = None
    aiodns_default = False

_NUMERIC_SOCKET_FLAGS = socket.AI_NUMERICHOST | socket.AI_NUMERICSERV
_NAME_SOCKET_FLAGS = socket.NI_NUMERICHOST | socket.NI_NUMERICSERV
_AI_ADDRCONFIG = socket.AI_ADDRCONFIG
if hasattr(socket, 'AI_MASK'):
    _AI_ADDRCONFIG &= socket.AI_MASK

class ThreadedResolver(AbstractResolver):
    '''Threaded resolver.

    Uses an Executor for synchronous getaddrinfo() calls.
    concurrent.futures.ThreadPoolExecutor is used by default.
    '''
    
    def __init__(self = None, loop = None):
        if not loop:
            pass
        self._loop = asyncio.get_running_loop()

    
    async def resolve(self = None, host = None, port = None, family = (0, socket.AF_INET)):
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        pass
    # WARNING: Decompyle incomplete



class AsyncResolver(AbstractResolver):
    '''Use the `aiodns` package to make asynchronous DNS lookups'''
    
    def __init__(self = None, loop = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    async def resolve(self = None, host = None, port = None, family = (0, socket.AF_INET)):
        pass
    # WARNING: Decompyle incomplete

    
    async def _resolve_with_query(self = None, host = None, port = None, family = (0, socket.AF_INET)):
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        pass
    # WARNING: Decompyle incomplete



class _DNSResolverManager:
    pass
# WARNING: Decompyle incomplete

_DefaultType = Type[Union[(AsyncResolver, ThreadedResolver)]]
DefaultResolver: _DefaultType = AsyncResolver if aiodns_default else ThreadedResolver
