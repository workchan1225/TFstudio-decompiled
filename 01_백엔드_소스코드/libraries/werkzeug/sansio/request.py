# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: request.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from datetime import datetime
from urllib.parse import parse_qsl
from datastructures import Accept
from datastructures import Authorization
from datastructures import CharsetAccept
from datastructures import ETags
from datastructures import Headers
from datastructures import HeaderSet
from datastructures import IfRange
from datastructures import ImmutableList
from datastructures import ImmutableMultiDict
from datastructures import LanguageAccept
from datastructures import MIMEAccept
from datastructures import MultiDict
from datastructures import Range
from datastructures import RequestCacheControl
from http import parse_accept_header
from http import parse_cache_control_header
from http import parse_date
from http import parse_etags
from http import parse_if_range_header
from http import parse_list_header
from http import parse_options_header
from http import parse_range_header
from http import parse_set_header
from user_agent import UserAgent
from utils import cached_property
from utils import header_property
from http import parse_cookie
from utils import get_content_length
from utils import get_current_url
from utils import get_host

class Request:
    '''Represents the non-IO parts of a HTTP request, including the
    method, URL info, and headers.

    This class is not meant for general use. It should only be used when
    implementing WSGI, ASGI, or another HTTP application spec. Werkzeug
    provides a WSGI implementation at :cls:`werkzeug.wrappers.Request`.

    :param method: The method the request was made with, such as
        ``GET``.
    :param scheme: The URL scheme of the protocol the request used, such
        as ``https`` or ``wss``.
    :param server: The address of the server. ``(host, port)``,
        ``(path, None)`` for unix sockets, or ``None`` if not known.
    :param root_path: The prefix that the application is mounted under.
        This is prepended to generated URLs, but is not part of route
        matching.
    :param path: The path part of the URL after ``root_path``.
    :param query_string: The part of the URL after the "?".
    :param headers: The headers received with the request.
    :param remote_addr: The address of the client sending the request.

    .. versionchanged:: 3.0
        The ``charset``, ``url_charset``, and ``encoding_errors`` attributes
        were removed.

    .. versionadded:: 2.0
    '''
    parameter_storage_class: 'type[MultiDict[str, t.Any]]' = ImmutableMultiDict
    dict_storage_class: 'type[MultiDict[str, t.Any]]' = ImmutableMultiDict
    list_storage_class: 'type[list[t.Any]]' = ImmutableList
    user_agent_class: 'type[UserAgent]' = UserAgent
    trusted_hosts: 'list[str] | None' = None
    
    def __init__(self, method, scheme, server, root_path, path = None, query_string = None, headers = None, remote_addr = ('method', 'str', 'scheme', 'str', 'server', 'tuple[str, int | None] | None', 'root_path', 'str', 'path', 'str', 'query_string', 'bytes', 'headers', 'Headers', 'remote_addr', 'str | None', 'return', 'None')):
        self.method = method.upper()
        self.scheme = scheme
        self.server = server
        self.root_path = root_path.rstrip('/')
        self.path = '/' + path.lstrip('/')
        self.query_string = query_string
        self.headers = headers
        self.remote_addr = remote_addr

    
    def __repr__(self = None):
        
        try:
            url = self.url
        except Exception:
            e = None
            url = f'''(invalid URL: {e})'''
            e = None
            del e
        except:
            e = None
            del e

        return f'''<{type(self).__name__} {url!r} [{self.method}]>'''

    args = (lambda self = None: self.parameter_storage_class(parse_qsl(self.query_string.decode(), keep_blank_values = True, errors = 'werkzeug.url_quote')))()
    access_route = (lambda self = None: if 'X-Forwarded-For' in self.headers:
self.list_storage_class(parse_list_header(self.headers['X-Forwarded-For']))# WARNING: Decompyle incomplete
)()
    full_path = (lambda self = None: f'''{self.path}?{self.query_string.decode()}''')()
    is_secure = (lambda self = None: self.scheme in frozenset({'wss', 'https'}))()
    url = (lambda self = None: get_current_url(self.scheme, self.host, self.root_path, self.path, self.query_string))()
    base_url = (lambda self = None: get_current_url(self.scheme, self.host, self.root_path, self.path))()
    root_url = (lambda self = None: get_current_url(self.scheme, self.host, self.root_path))()
    host_url = (lambda self = None: get_current_url(self.scheme, self.host))()
    host = (lambda self = None: get_host(self.scheme, self.headers.get('host'), self.server, self.trusted_hosts))()
    cookies = (lambda self = None: wsgi_combined_cookie = ';'.join(self.headers.getlist('Cookie'))parse_cookie(wsgi_combined_cookie, cls = self.dict_storage_class))()
    content_type = header_property[str]('Content-Type', doc = 'The Content-Type entity-header field indicates the media\n        type of the entity-body sent to the recipient or, in the case of\n        the HEAD method, the media type that would have been sent had\n        the request been a GET.', read_only = True)
    content_length = (lambda self = None: get_content_length(http_content_length = self.headers.get('Content-Length'), http_transfer_encoding = self.headers.get('Transfer-Encoding')))()
    content_encoding = header_property[str]('Content-Encoding', doc = 'The Content-Encoding entity-header field is used as a\n        modifier to the media-type. When present, its value indicates\n        what additional content codings have been applied to the\n        entity-body, and thus what decoding mechanisms must be applied\n        in order to obtain the media-type referenced by the Content-Type\n        header field.\n\n        .. versionadded:: 0.9', read_only = True)
    content_md5 = header_property[str]('Content-MD5', doc = 'The Content-MD5 entity-header field, as defined in\n        RFC 1864, is an MD5 digest of the entity-body for the purpose of\n        providing an end-to-end message integrity check (MIC) of the\n        entity-body. (Note: a MIC is good for detecting accidental\n        modification of the entity-body in transit, but is not proof\n        against malicious attacks.)\n\n        .. versionadded:: 0.9', read_only = True)
    referrer = header_property[str]('Referer', doc = 'The Referer[sic] request-header field allows the client\n        to specify, for the server\'s benefit, the address (URI) of the\n        resource from which the Request-URI was obtained (the\n        "referrer", although the header field is misspelled).', read_only = True)
    date = header_property('Date', None, parse_date, doc = 'The Date general-header field represents the date and\n        time at which the message was originated, having the same\n        semantics as orig-date in RFC 822.\n\n        .. versionchanged:: 2.0\n            The datetime object is timezone-aware.\n        ', read_only = True)
    max_forwards = header_property('Max-Forwards', None, int, doc = 'The Max-Forwards request-header field provides a\n        mechanism with the TRACE and OPTIONS methods to limit the number\n        of proxies or gateways that can forward the request to the next\n        inbound server.', read_only = True)
    
    def _parse_content_type(self = None):
        if not hasattr(self, '_parsed_content_type'):
            self._parsed_content_type = parse_options_header(self.headers.get('Content-Type', ''))
            return None

    mimetype = (lambda self = None: self._parse_content_type()self._parsed_content_type[0].lower())()
    mimetype_params = (lambda self = None: self._parse_content_type()self._parsed_content_type[1])()
    pragma = (lambda self = None: parse_set_header(self.headers.get('Pragma', '')))()
    accept_mimetypes = (lambda self = None: parse_accept_header(self.headers.get('Accept'), MIMEAccept))()
    accept_charsets = (lambda self = None: parse_accept_header(self.headers.get('Accept-Charset'), CharsetAccept))()
    accept_encodings = (lambda self = None: parse_accept_header(self.headers.get('Accept-Encoding')))()
    accept_languages = (lambda self = None: parse_accept_header(self.headers.get('Accept-Language'), LanguageAccept))()
    cache_control = (lambda self = None: cache_control = self.headers.get('Cache-Control')parse_cache_control_header(cache_control, None, RequestCacheControl))()
    if_match = (lambda self = None: parse_etags(self.headers.get('If-Match')))()
    if_none_match = (lambda self = None: parse_etags(self.headers.get('If-None-Match')))()
    if_modified_since = (lambda self = None: parse_date(self.headers.get('If-Modified-Since')))()
    if_unmodified_since = (lambda self = None: parse_date(self.headers.get('If-Unmodified-Since')))()
    if_range = (lambda self = None: parse_if_range_header(self.headers.get('If-Range')))()
    range = (lambda self = None: parse_range_header(self.headers.get('Range')))()
    user_agent = (lambda self = None: self.user_agent_class(self.headers.get('User-Agent', '')))()
    authorization = (lambda self = None: Authorization.from_header(self.headers.get('Authorization')))()
    origin = header_property[str]('Origin', doc = 'The host that the request originated from. Set :attr:`~CORSResponseMixin.access_control_allow_origin` on the response to indicate which origins are allowed.', read_only = True)
    access_control_request_headers = header_property('Access-Control-Request-Headers', load_func = parse_set_header, doc = 'Sent with a preflight request to indicate which headers will be sent with the cross origin request. Set :attr:`~CORSResponseMixin.access_control_allow_headers` on the response to indicate which headers are allowed.', read_only = True)
    access_control_request_method = header_property[str]('Access-Control-Request-Method', doc = 'Sent with a preflight request to indicate which method will be used for the cross origin request. Set :attr:`~CORSResponseMixin.access_control_allow_methods` on the response to indicate which methods are allowed.', read_only = True)
    is_json = (lambda self = None:
