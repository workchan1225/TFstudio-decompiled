# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http_sync.pyc (Python 3.11)

'''This file is largely copied from http.py'''
import io
import logging
import re
import urllib.error as urllib
import urllib.parse as urllib
from copy import copy
from json import dumps, loads
from urllib.parse import urlparse

try:
    import yarl
except (ImportError, ModuleNotFoundError, OSError):
    yarl = False

from fsspec.callbacks import _DEFAULT_CALLBACK
from fsspec.registry import register_implementation
from fsspec.spec import AbstractBufferedFile, AbstractFileSystem
from fsspec.utils import DEFAULT_BLOCK_SIZE, isfilelike, nullcontext, tokenize
from caching import AllBytes
ex = re.compile('<(a|A)\\s+(?:[^>]*?\\s+)?(href|HREF)=["\'](?P<url>[^"\']+)')
ex2 = re.compile('(?P<url>http[s]?://[-a-zA-Z0-9@:%_+.~#?&/=]+)')
logger = logging.getLogger('fsspec.http')

class JsHttpException(urllib.error.HTTPError):
    pass


class StreamIO(io.BytesIO):
    pass


class ResponseProxy:
    '''Looks like a requests response'''
    
    def __init__(self, req, stream = (False,)):
        self.request = req
        self.stream = stream
        self._data = None
        self._headers = None

    raw = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def close(self):
        if hasattr(self, '_data'):
            del self._data
            return None

    headers = (lambda self: pass# WARNING: Decompyle incomplete
)()
    status_code = (lambda self: int(self.request.status))()
    
    def raise_for_status(self):
        if not self.ok:
            raise JsHttpException(self.url, self.status_code, self.reason, self.headers, None)

    
    def iter_content(self, chunksize, *_, **__):
        pass
    # WARNING: Decompyle incomplete

    reason = (lambda self: self.request.statusText)()
    ok = (lambda self: self.status_code < 400)()
    url = (lambda self: self.request.response.responseURL)()
    text = (lambda self: self.content.decode())()
    content = (lambda self: self.stream = Falseself.raw)()
    
    def json(self):
        return loads(self.text)



class RequestsSessionShim:
    
    def __init__(self):
        self.headers = { }

    
    def request(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json = (None, None, None, None, None, None, None, None, None, None, None, None, None, None)):
        Blob = Blob
        XMLHttpRequest = XMLHttpRequest
        import js
        logger.debug('JS request: %s %s', method, url)
        if cert and verify and proxies and files and cookies or hooks:
            raise NotImplementedError
        if data and json:
            raise ValueError('Use json= or data=, not both')
        req = XMLHttpRequest.new()
        extra = auth if auth else ()
        if params:
            url = f'''{url}?{urllib.parse.urlencode(params)}'''
    # WARNING: Decompyle incomplete

    
    def get(self, url, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def head(self, url, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def post(self, url, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def put(self, url, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def patch(self, url, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def delete(self, url, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class HTTPFileSystem(AbstractFileSystem):
    pass
# WARNING: Decompyle incomplete


class HTTPFile(AbstractBufferedFile):
    pass
# WARNING: Decompyle incomplete

magic_check = re.compile('([*[])')

def has_magic(s):
    match = magic_check.search(s)
    return match is not None


class HTTPStreamFile(AbstractBufferedFile):
    pass
# WARNING: Decompyle incomplete


def get_range(session, url, start, end, **kwargs):
    kwargs = kwargs.copy()
    headers = kwargs.pop('headers', { }).copy()
    headers['Range'] = f'''bytes={start}-{end - 1}'''
# WARNING: Decompyle incomplete


def _file_info(url, session, size_policy = ('head',), **kwargs):
    """Call HEAD on the server to get details about the file (size/checksum etc.)

    Default operation is to explicitly allow redirects and use encoding
    'identity' (no compression) to get the true size of the target.
    """
    logger.debug('Retrieve file size for %s', url)
    kwargs = kwargs.copy()
    ar = kwargs.pop('allow_redirects', True)
    head = kwargs.get('headers', { }).copy()
    kwargs['headers'] = head
    info = { }
# WARNING: Decompyle incomplete


def register():
    register_implementation('http', HTTPFileSystem, clobber = True)
    register_implementation('https', HTTPFileSystem, clobber = True)
    register_implementation('sync-http', HTTPFileSystem, clobber = True)
    register_implementation('sync-https', HTTPFileSystem, clobber = True)

register()

def unregister():
    HTTPFileSystem = HTTPFileSystem
    import fsspec.implementations.http
    register_implementation('http', HTTPFileSystem, clobber = True)
    register_implementation('https', HTTPFileSystem, clobber = True)
