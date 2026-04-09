# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: retry.pyc (Python 3.11)

from __future__ import annotations
import email
import logging
import random
import re
import time
import typing
from itertools import takewhile
from types import TracebackType
from exceptions import ConnectTimeoutError, InvalidHeader, MaxRetryError, ProtocolError, ProxyError, ReadTimeoutError, ResponseError
from util import reraise
if typing.TYPE_CHECKING:
    from typing_extensions import Self
    from connectionpool import ConnectionPool
    from response import BaseHTTPResponse
log = logging.getLogger(__name__)

class RequestHistory(typing.NamedTuple):
    redirect_location: 'str | None' = 'RequestHistory'


class Retry:
    '''Retry configuration.

    Each retry attempt will create a new Retry object with updated values, so
    they can be safely reused.

    Retries can be defined as a default for a pool:

    .. code-block:: python

        retries = Retry(connect=5, read=2, redirect=5)
        http = PoolManager(retries=retries)
        response = http.request("GET", "https://example.com/")

    Or per-request (which overrides the default for the pool):

    .. code-block:: python

        response = http.request("GET", "https://example.com/", retries=Retry(10))

    Retries can be disabled by passing ``False``:

    .. code-block:: python

        response = http.request("GET", "https://example.com/", retries=False)

    Errors will be wrapped in :class:`~urllib3.exceptions.MaxRetryError` unless
    retries are disabled, in which case the causing exception will be raised.

    :param int total:
        Total number of retries to allow. Takes precedence over other counts.

        Set to ``None`` to remove this constraint and fall back on other
        counts.

        Set to ``0`` to fail on the first retry.

        Set to ``False`` to disable and imply ``raise_on_redirect=False``.

    :param int connect:
        How many connection-related errors to retry on.

        These are errors raised before the request is sent to the remote server,
        which we assume has not triggered the server to process the request.

        Set to ``0`` to fail on the first retry of this type.

    :param int read:
        How many times to retry on read errors.

        These errors are raised after the request was sent to the server, so the
        request may have side-effects.

        Set to ``0`` to fail on the first retry of this type.

    :param int redirect:
        How many redirects to perform. Limit this to avoid infinite redirect
        loops.

        A redirect is a HTTP response with a status code 301, 302, 303, 307 or
        308.

        Set to ``0`` to fail on the first retry of this type.

        Set to ``False`` to disable and imply ``raise_on_redirect=False``.

    :param int status:
        How many times to retry on bad status codes.

        These are retries made on responses, where status code matches
        ``status_forcelist``.

        Set to ``0`` to fail on the first retry of this type.

    :param int other:
        How many times to retry on other errors.

        Other errors are errors that are not connect, read, redirect or status errors.
        These errors might be raised after the request was sent to the server, so the
        request might have side-effects.

        Set to ``0`` to fail on the first retry of this type.

        If ``total`` is not set, it\'s a good idea to set this to 0 to account
        for unexpected edge cases and avoid infinite retry loops.

    :param Collection allowed_methods:
        Set of uppercased HTTP method verbs that we should retry on.

        By default, we only retry on methods which are considered to be
        idempotent (multiple requests with the same parameters end with the
        same state). See :attr:`Retry.DEFAULT_ALLOWED_METHODS`.

        Set to a ``None`` value to retry on any verb.

    :param Collection status_forcelist:
        A set of integer HTTP status codes that we should force a retry on.
        A retry is initiated if the request method is in ``allowed_methods``
        and the response status code is in ``status_forcelist``.

        By default, this is disabled with ``None``.

    :param float backoff_factor:
        A backoff factor to apply between attempts after the second try
        (most errors are resolved immediately by a second try without a
        delay). urllib3 will sleep for::

            {backoff factor} * (2 ** ({number of previous retries}))

        seconds. If `backoff_jitter` is non-zero, this sleep is extended by::

            random.uniform(0, {backoff jitter})

        seconds. For example, if the backoff_factor is 0.1, then :func:`Retry.sleep` will
        sleep for [0.0s, 0.2s, 0.4s, 0.8s, ...] between retries. No backoff will ever
        be longer than `backoff_max`.

        By default, backoff is disabled (factor set to 0).

    :param bool raise_on_redirect: Whether, if the number of redirects is
        exhausted, to raise a MaxRetryError, or to return a response with a
        response code in the 3xx range.

    :param bool raise_on_status: Similar meaning to ``raise_on_redirect``:
        whether we should raise an exception, or return a response,
        if status falls in ``status_forcelist`` range and retries have
        been exhausted.

    :param tuple history: The history of the request encountered during
        each call to :meth:`~Retry.increment`. The list is in the order
        the requests occurred. Each list item is of class :class:`RequestHistory`.

    :param bool respect_retry_after_header:
        Whether to respect Retry-After header on status codes defined as
        :attr:`Retry.RETRY_AFTER_STATUS_CODES` or not.

    :param Collection remove_headers_on_redirect:
        Sequence of headers to remove from the request when a response
        indicating a redirect is returned before firing off the redirected
        request.

    :param int retry_after_max: Number of seconds to allow as the maximum for
        Retry-After headers. Defaults to :attr:`Retry.DEFAULT_RETRY_AFTER_MAX`.
        Any Retry-After headers larger than this value will be limited to this
        value.
    '''
    DEFAULT_ALLOWED_METHODS = frozenset([
        'HEAD',
        'GET',
        'PUT',
        'DELETE',
        'OPTIONS',
        'TRACE'])
    RETRY_AFTER_STATUS_CODES = frozenset([
        413,
        429,
        503])
    DEFAULT_REMOVE_HEADERS_ON_REDIRECT = frozenset([
        'Cookie',
        'Authorization',
        'Proxy-Authorization'])
    DEFAULT_BACKOFF_MAX = 120
    DEFAULT: 'typing.ClassVar[Retry]' = 21600
    
    def __init__(self, total, connect, read, redirect, status, other, allowed_methods, status_forcelist, backoff_factor, backoff_max, raise_on_redirect, raise_on_status, history = None, respect_retry_after_header = None, remove_headers_on_redirect = None, backoff_jitter = (10, None, None, None, None, None, DEFAULT_ALLOWED_METHODS, None, 0, DEFAULT_BACKOFF_MAX, True, True, None, True, DEFAULT_REMOVE_HEADERS_ON_REDIRECT, 0, DEFAULT_RETRY_AFTER_MAX), retry_after_max = ('total', 'bool | int | None', 'connect', 'int | None', 'read', 'int | None', 'redirect', 'bool | int | None', 'status', 'int | None', 'other', 'int | None', 'allowed_methods', 'typing.Collection[str] | None', 'status_forcelist', 'typing.Collection[int] | None', 'backoff_factor', 'float', 'backoff_max', 'float', 'raise_on_redirect', 'bool', 'raise_on_status', 'bool', 'history', 'tuple[RequestHistory, ...] | None', 'respect_retry_after_header', 'bool', 'remove_headers_on_redirect', 'typing.Collection[str]', 'backoff_jitter', 'float', 'retry_after_max', 'int', 'return', 'None')):
