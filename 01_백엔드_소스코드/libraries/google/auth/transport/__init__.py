# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Transport - HTTP client library support.

:mod:`google.auth` is designed to work with various HTTP client libraries such
as urllib3 and requests. In order to work across these libraries with different
interfaces some abstraction is needed.

This module provides two interfaces that are implemented by transport adapters
to support HTTP libraries. :class:`Request` defines the interface expected by
:mod:`google.auth` to make requests. :class:`Response` defines the interface
for the return value of :class:`Request`.
'''
import abc
from http.client import client as http_client
DEFAULT_RETRYABLE_STATUS_CODES = (http_client.INTERNAL_SERVER_ERROR, http_client.SERVICE_UNAVAILABLE, http_client.GATEWAY_TIMEOUT, http_client.REQUEST_TIMEOUT, http_client.TOO_MANY_REQUESTS)
DEFAULT_REFRESH_STATUS_CODES = (http_client.UNAUTHORIZED,)
DEFAULT_MAX_REFRESH_ATTEMPTS = 2

def Response():
    '''Response'''
    __doc__ = 'HTTP Response data.'
    status = (lambda self: raise NotImplementedError('status must be implemented.'))()
    headers = (lambda self: raise NotImplementedError('headers must be implemented.'))()
    data = (lambda self: raise NotImplementedError('data must be implemented.'))()

Response = <NODE:27>(Response, 'Response', metaclass = abc.ABCMeta)

def Request():
    '''Request'''
    __doc__ = 'Interface for a callable that makes HTTP requests.\n\n    Specific transport implementations should provide an implementation of\n    this that adapts their specific request / response API.\n\n    .. automethod:: __call__\n    '
    __call__ = (lambda self, url, method, body, headers, timeout = ('GET', None, None, None): raise NotImplementedError('__call__ must be implemented.'))()

Request = <NODE:27>(Request, 'Request', metaclass = abc.ABCMeta)
