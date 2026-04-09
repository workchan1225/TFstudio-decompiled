# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Transport - Asynchronous HTTP client library support.

:mod:`google.auth.aio` is designed to work with various asynchronous client libraries such
as aiohttp. In order to work across these libraries with different
interfaces some abstraction is needed.

This module provides two interfaces that are implemented by transport adapters
to support HTTP libraries. :class:`Request` defines the interface expected by
:mod:`google.auth` to make asynchronous requests. :class:`Response` defines the interface
for the return value of :class:`Request`.
'''
import abc
from typing import AsyncGenerator, Mapping, Optional
import google.auth.transport as google
_DEFAULT_TIMEOUT_SECONDS = 180
DEFAULT_RETRYABLE_STATUS_CODES = google.auth.transport.DEFAULT_RETRYABLE_STATUS_CODES
DEFAULT_MAX_RETRY_ATTEMPTS = 3

def Response():
    '''Response'''
    __doc__ = 'Asynchronous HTTP Response Interface.'
    status_code = (lambda self = None: raise NotImplementedError('status_code must be implemented.'))()()
    headers = (lambda self = None: raise NotImplementedError('headers must be implemented.'))()()
    content = (lambda self = None, chunk_size = None: pass# WARNING: Decompyle incomplete
)()
    read = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    close = (lambda self: pass# WARNING: Decompyle incomplete
)()

Response = <NODE:27>(Response, 'Response', metaclass = abc.ABCMeta)

def Request():
    '''Request'''
    __doc__ = 'Interface for a callable that makes HTTP requests.\n\n    Specific transport implementations should provide an implementation of\n    this that adapts their specific request / response API.\n\n    .. automethod:: __call__\n    '
    __call__ = (lambda self, url, method = None, body = None, headers = abc.abstractmethod, timeout = ('url', str, 'method', str, 'body', Optional[bytes], 'headers', Optional[Mapping[(str, str)]], 'timeout', float, 'return', Response): pass# WARNING: Decompyle incomplete
)()
    
    async def close(self = None):
        '''
        Close the underlying session.
        '''
        pass
    # WARNING: Decompyle incomplete


Request = <NODE:27>(Request, 'Request', metaclass = abc.ABCMeta)
