# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from http import HTTPStatus
from datastructures import CallbackDict
from datastructures import ContentRange
from datastructures import ContentSecurityPolicy
from datastructures import Headers
from datastructures import HeaderSet
from datastructures import ResponseCacheControl
from datastructures import WWWAuthenticate
from http import COEP
from http import COOP
from http import dump_age
from http import dump_cookie
from http import dump_header
from http import dump_options_header
from http import http_date
from http import HTTP_STATUS_CODES
from http import parse_age
from http import parse_cache_control_header
from http import parse_content_range_header
from http import parse_csp_header
from http import parse_date
from http import parse_options_header
from http import parse_set_header
from http import quote_etag
from http import unquote_etag
from utils import get_content_type
from utils import header_property
if t.TYPE_CHECKING:
    from datastructures.cache_control import _CacheControl

def _set_property(name = None, doc = None):
    pass
# WARNING: Decompyle incomplete


class Response:
    '''Represents the non-IO parts of an HTTP response, specifically the
    status and headers but not the body.

    This class is not meant for general use. It should only be used when
    implementing WSGI, ASGI, or another HTTP application spec. Werkzeug
    provides a WSGI implementation at :cls:`werkzeug.wrappers.Response`.

    :param status: The status code for the response. Either an int, in
        which case the default status message is added, or a string in
        the form ``{code} {message}``, like ``404 Not Found``. Defaults
        to 200.
    :param headers: A :class:`~werkzeug.datastructures.Headers` object,
        or a list of ``(key, value)`` tuples that will be converted to a
        ``Headers`` object.
    :param mimetype: The mime type (content type without charset or
        other parameters) of the response. If the value starts with
        ``text/`` (or matches some other special cases), the charset
        will be added to create the ``content_type``.
    :param content_type: The full content type of the response.
        Overrides building the value from ``mimetype``.

    .. versionchanged:: 3.0
        The ``charset`` attribute was removed.

    .. versionadded:: 2.0
    '''
    default_status = 200
    default_mimetype: 'str | None' = 'text/plain'
    headers: 'Headers' = 4093
    
    def __init__(self = None, status = None, headers = None, mimetype = (None, None, None, None), content_type = ('status', 'int | str | HTTPStatus | None', 'headers', 't.Mapping[str, str | t.Iterable[str]] | t.Iterable[tuple[str, str]] | None', 'mimetype', 'str | None', 'content_type', 'str | None', 'return', 'None')):
        if isinstance(headers, Headers):
            self.headers = headers
        elif not headers:
            self.headers = Headers()
        else:
            self.headers = Headers(headers)
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<{type(self).__name__} [{self.status}]>'''

    status_code = (lambda self = None: self._status_code)()
    status_code = (lambda self = None, code = None: self.status = code)()
    status = (lambda self = None: self._status)()
    status = (lambda self = None, value = None: (self._status, self._status_code) = self._clean_status(value))()
    
    def _clean_status(self = None, value = None):
        if isinstance(value, (int, HTTPStatus)):
            status_code = int(value)
        else:
            value = value.strip()
            if not value:
                raise ValueError('Empty status argument')
            (code_str, sep, _) = value.partition(' ')
            
            try:
                status_code = int(code_str)
            except ValueError:
                return 

            if sep:
                return (value, status_code)
            
            try:
                pass
            except KeyError:
                f'''{status_code} UNKNOWN''' = None

            return (status, status_code)

    
    def set_cookie(self, key, value, max_age, expires, path, domain = None, secure = None, httponly = None, samesite = ('', None, None, '/', None, False, False, None, False), partitioned = ('key', 'str', 'value', 'str', 'max_age', 'timedelta | int | None', 'expires', 'str | datetime | int | float | None', 'path', 'str | None', 'domain', 'str | None', 'secure', 'bool', 'httponly', 'bool', 'samesite', 'str | None', 'partitioned', 'bool', 'return', 'None')):
        '''Sets a cookie.

        A warning is raised if the size of the cookie header exceeds
        :attr:`max_cookie_size`, but the header will still be set.

        :param key: the key (name) of the cookie to be set.
        :param value: the value of the cookie.
        :param max_age: should be a number of seconds, or `None` (default) if
                        the cookie should last only as long as the client\'s
                        browser session.
        :param expires: should be a `datetime` object or UNIX timestamp.
        :param path: limits the cookie to a given path, per default it will
                     span the whole domain.
        :param domain: if you want to set a cross-domain cookie.  For example,
                       ``domain="example.com"`` will set a cookie that is
                       readable by the domain ``www.example.com``,
                       ``foo.example.com`` etc.  Otherwise, a cookie will only
                       be readable by the domain that set it.
        :param secure: If ``True``, the cookie will only be available
            via HTTPS.
        :param httponly: Disallow JavaScript access to the cookie.
        :param samesite: Limit the scope of the cookie to only be
            attached to requests that are "same-site".
        :param partitioned: If ``True``, the cookie will be partitioned.

        .. versionchanged:: 3.1
            The ``partitioned`` parameter was added.
        '''
        self.headers.add('Set-Cookie', dump_cookie(key, value = value, max_age = max_age, expires = expires, path = path, domain = domain, secure = secure, httponly = httponly, max_size = self.max_cookie_size, samesite = samesite, partitioned = partitioned))

    
    def delete_cookie(self, key, path, domain = None, secure = None, httponly = None, samesite = ('/', None, False, False, None, False), partitioned = ('key', 'str', 'path', 'str | None', 'domain', 'str | None', 'secure', 'bool', 'httponly', 'bool', 'samesite', 'str | None', 'partitioned', 'bool', 'return', 'None')):
        '''Delete a cookie.  Fails silently if key doesn\'t exist.

        :param key: the key (name) of the cookie to be deleted.
        :param path: if the cookie that should be deleted was limited to a
                     path, the path has to be defined here.
        :param domain: if the cookie that should be deleted was limited to a
                       domain, that domain has to be defined here.
        :param secure: If ``True``, the cookie will only be available
            via HTTPS.
        :param httponly: Disallow JavaScript access to the cookie.
        :param samesite: Limit the scope of the cookie to only be
            attached to requests that are "same-site".
        :param partitioned: If ``True``, the cookie will be partitioned.
        '''
        self.set_cookie(key, expires = 0, max_age = 0, path = path, domain = domain, secure = secure, httponly = httponly, samesite = samesite, partitioned = partitioned)

    is_json = (lambda self = None:
