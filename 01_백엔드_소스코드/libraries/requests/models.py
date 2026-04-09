# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: models.pyc (Python 3.11)

'''
requests.models
~~~~~~~~~~~~~~~

This module contains the primary objects that power Requests.
'''
import datetime
import encodings.idna as encodings
from io import UnsupportedOperation
from urllib3.exceptions import DecodeError, LocationParseError, ProtocolError, ReadTimeoutError, SSLError
from urllib3.fields import RequestField
from urllib3.filepost import encode_multipart_formdata
from urllib3.util import parse_url
from _internal_utils import to_native_string, unicode_is_ascii
from auth import HTTPBasicAuth
from compat import Callable, JSONDecodeError, Mapping, basestring, builtin_str, chardet, cookielib
from compat import json as complexjson
from compat import urlencode, urlsplit, urlunparse
from cookies import _copy_cookie_jar, cookiejar_from_dict, get_cookie_header
from exceptions import ChunkedEncodingError, ConnectionError, ContentDecodingError, HTTPError, InvalidJSONError, InvalidURL
from exceptions import JSONDecodeError as RequestsJSONDecodeError
from exceptions import MissingSchema
from exceptions import SSLError as RequestsSSLError
from exceptions import StreamConsumedError
from hooks import default_hooks
from status_codes import codes
from structures import CaseInsensitiveDict
from utils import check_header_validity, get_auth_from_url, guess_filename, guess_json_utf, iter_slices, parse_header_links, requote_uri, stream_decode_response_unicode, super_len, to_key_val_list
REDIRECT_STATI = (codes.moved, codes.found, codes.other, codes.temporary_redirect, codes.permanent_redirect)
DEFAULT_REDIRECT_LIMIT = 30
CONTENT_CHUNK_SIZE = 10240
ITER_CHUNK_SIZE = 512

class RequestEncodingMixin:
    path_url = (lambda self: url = []p = urlsplit(self.url)path = p.pathif not path:
path = '/'url.append(path)query = p.queryif query:
url.append('?')url.append(query)''.join(url))()
    _encode_params = (lambda data: if isinstance(data, (str, bytes)):
dataif None(data, 'read'):
data# WARNING: Decompyle incomplete
)()
    _encode_files = (lambda files, data: if not files:
raise ValueError('Files must be provided.')if isinstance(data, basestring):
raise ValueError('Data must not be a string.')new_fields = []# WARNING: Decompyle incomplete
)()


class RequestHooksMixin:
    
    def register_hook(self, event, hook):
        '''Properly register a hook.'''
        if event not in self.hooks:
            raise ValueError(f'''Unsupported event specified, with event name "{event}"''')
        if isinstance(hook, Callable):
            self.hooks[event].append(hook)
            return None
        if None(hook, '__iter__'):
            (lambda .0: pass# WARNING: Decompyle incomplete
)(hook())
            return None

    
    def deregister_hook(self, event, hook):
        '''Deregister a previously registered hook.
        Returns True if the hook existed, False if not.
        '''
        
        try:
            self.hooks[event].remove(hook)
            return True
        except ValueError:
            return False




class Request(RequestHooksMixin):
    """A user-created :class:`Request <Request>` object.

    Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

    :param method: HTTP method to use.
    :param url: URL to send.
    :param headers: dictionary of headers to send.
    :param files: dictionary of {filename: fileobject} files to multipart upload.
    :param data: the body to attach to the request. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param json: json for the body to attach to the request (if files or data is not specified).
    :param params: URL parameters to append to the URL. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param auth: Auth handler or (user, pass) tuple.
    :param cookies: dictionary or CookieJar of cookies to attach to this request.
    :param hooks: dictionary of callback hooks, for internal usage.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> req.prepare()
      <PreparedRequest [GET]>
    """
    
    def __init__(self, method, url, headers, files, data, params, auth, cookies, hooks, json = (None, None, None, None, None, None, None, None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''<Request [{self.method}]>'''

    
    def prepare(self):
        '''Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it.'''
        p = PreparedRequest()
        p.prepare(method = self.method, url = self.url, headers = self.headers, files = self.files, data = self.data, json = self.json, params = self.params, auth = self.auth, cookies = self.cookies, hooks = self.hooks)
        return p



class PreparedRequest(RequestHooksMixin, RequestEncodingMixin):
    """The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
    containing the exact bytes that will be sent to the server.

    Instances are generated from a :class:`Request <Request>` object, and
    should not be instantiated manually; doing so may produce undesirable
    effects.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> r = req.prepare()
      >>> r
      <PreparedRequest [GET]>

      >>> s = requests.Session()
      >>> s.send(r)
      <Response [200]>
    """
    
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = None
        self._cookies = None
        self.body = None
        self.hooks = default_hooks()
        self._body_position = None

    
    def prepare(self, method, url, headers, files, data, params, auth, cookies, hooks, json = (None, None, None, None, None, None, None, None, None, None)):
        '''Prepares the entire request with the given parameters.'''
        self.prepare_method(method)
        self.prepare_url(url, params)
        self.prepare_headers(headers)
        self.prepare_cookies(cookies)
        self.prepare_body(data, files, json)
        self.prepare_auth(auth, url)
        self.prepare_hooks(hooks)

    
    def __repr__(self):
        return f'''<PreparedRequest [{self.method}]>'''

    
    def copy(self):
        p = PreparedRequest()
        p.method = self.method
        p.url = self.url
    # WARNING: Decompyle incomplete

    
    def prepare_method(self, method):
        '''Prepares the given HTTP method.'''
        self.method = method
    # WARNING: Decompyle incomplete

    _get_idna_encoded_host = (lambda host: import idnatry:
host = idna.encode(host, uts46 = True).decode('utf-8')except idna.IDNAError:
raise UnicodeErrorhost)()
    
    def prepare_url(self, url, params):
        '''Prepares the given HTTP URL.'''
        if isinstance(url, bytes):
            url = url.decode('utf8')
        else:
            url = str(url)
        url = url.lstrip()
        if not ':' in url and url.lower().startswith('http'):
            self.url = url
            return None
    # WARNING: Decompyle incomplete

    
    def prepare_headers(self, headers):
        '''Prepares the given HTTP headers.'''
        self.headers = CaseInsensitiveDict()
        if headers:
            for header in headers.items():
                check_header_validity(header)
                (name, value) = header
                self.headers[to_native_string(name)] = value
                return None
                return None

    
    def prepare_body(self, data, files, json = (None,)):
        '''Prepares the given HTTP body data.'''
        body = None
        content_type = None
    # WARNING: Decompyle incomplete

    
    def prepare_content_length(self, body):
        '''Prepare Content-Length header based on request method and body'''
        pass
    # WARNING: Decompyle incomplete

    
    def prepare_auth(self, auth, url = ('',)):
        '''Prepares the given HTTP auth data.'''
        pass
    # WARNING: Decompyle incomplete

    
    def prepare_cookies(self, cookies):
        '''Prepares the given HTTP cookie data.

        This function eventually generates a ``Cookie`` header from the
        given cookies using cookielib. Due to cookielib\'s design, the header
        will not be regenerated if it already exists, meaning this function
        can only be called once for the life of the
        :class:`PreparedRequest <PreparedRequest>` object. Any subsequent calls
        to ``prepare_cookies`` will have no actual effect, unless the "Cookie"
        header is removed beforehand.
        '''
        if isinstance(cookies, cookielib.CookieJar):
            self._cookies = cookies
        else:
            self._cookies = cookiejar_from_dict(cookies)
        cookie_header = get_cookie_header(self._cookies, self)
    # WARNING: Decompyle incomplete

    
    def prepare_hooks(self, hooks):
        '''Prepares the given hooks.'''
        if not hooks:
            hooks = []
            for event in hooks:
                self.register_hook(event, hooks[event])
                return None



class Response:
    """The :class:`Response <Response>` object, which contains a
    server's response to an HTTP request.
    """
    __attrs__ = [
        '_content',
        'status_code',
        'headers',
        'url',
        'history',
        'encoding',
        'reason',
        'cookies',
        'elapsed',
        'request']
    
    def __init__(self):
        self._content = False
        self._content_consumed = False
        self._next = None
        self.status_code = None
        self.headers = CaseInsensitiveDict()
        self.raw = None
        self.url = None
        self.encoding = None
        self.history = []
        self.reason = None
        self.cookies = cookiejar_from_dict({ })
        self.elapsed = datetime.timedelta(0)
        self.request = None

    
    def __enter__(self):
        return self

    
    def __exit__(self, *args):
        self.close()

    
    def __getstate__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __setstate__(self, state):
        for name, value in state.items():
            setattr(self, name, value)
            setattr(self, '_content_consumed', True)
            setattr(self, 'raw', None)
            return None

    
    def __repr__(self):
        return f'''<Response [{self.status_code}]>'''

    
    def __bool__(self):
        '''Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        '''
        return self.ok

    
    def __nonzero__(self):
        '''Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        '''
        return self.ok

    
    def __iter__(self):
        '''Allows you to use a response as an iterator.'''
        return self.iter_content(128)

    ok = (lambda self: try:
self.raise_for_status()except HTTPError:
FalseTrue)()
    is_redirect = (lambda self: if 'location' in self.headers:
passself.status_code in REDIRECT_STATI)()
    is_permanent_redirect = (lambda self: if 'location' in self.headers:
passself.status_code in (codes.moved_permanently, codes.permanent_redirect))()
    next = (lambda self: self._next)()
    apparent_encoding = (lambda self: chardet.detect(self.content)['encoding'])()
    
    def iter_content(self, chunk_size, decode_unicode = (1, False)):
        '''Iterates over the response data.  When stream=True is set on the
        request, this avoids reading the content at once into memory for
        large responses.  The chunk size is the number of bytes it should
        read into memory.  This is not necessarily the length of each item
        returned as decoding can take place.

        chunk_size must be of type int or None. A value of None will
        function differently depending on the value of `stream`.
        stream=True will read data as it arrives in whatever size the
        chunks are received. If stream=False, data is returned as
        a single chunk.

        If decode_unicode is True, content will be decoded using the best
        available encoding based on the response.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_lines(self, chunk_size, decode_unicode, delimiter = (ITER_CHUNK_SIZE, False, None)):
        '''Iterates over the response data, one line at a time.  When
        stream=True is set on the request, this avoids reading the
        content at once into memory for large responses.

        .. note:: This method is not reentrant safe.
        '''
        pass
    # WARNING: Decompyle incomplete

    content = (lambda self: pass# WARNING: Decompyle incomplete
)()
    text = (lambda self: content = Noneencoding = self.encodingif not self.content:
''# WARNING: Decompyle incomplete
)()
    
    def json(self, **kwargs):
        '''Returns the json-encoded content of a response, if any.

        :param \\*\\*kwargs: Optional arguments that ``json.loads`` takes.
        :raises requests.exceptions.JSONDecodeError: If the response body does not
            contain valid json.
        '''
        pass
    # WARNING: Decompyle incomplete

    links = (lambda self:
