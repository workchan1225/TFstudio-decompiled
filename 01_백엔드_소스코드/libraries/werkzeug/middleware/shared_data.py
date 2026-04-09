# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shared_data.pyc (Python 3.11)

'''
Serve Shared Static Files
=========================

.. autoclass:: SharedDataMiddleware
    :members: is_allowed

:copyright: 2007 Pallets
:license: BSD-3-Clause
'''
from __future__ import annotations
from collections.abc import abc as cabc
import importlib.util as importlib
import mimetypes
import os
import posixpath
import typing as t
from datetime import datetime
from datetime import timezone
from io import BytesIO
from time import time
from zlib import adler32
from http import http_date
from http import is_resource_modified
from security import safe_join
from utils import get_content_type
from wsgi import get_path_info
from wsgi import wrap_file
_TOpener = t.Callable[([], tuple[(t.IO[bytes], datetime, int)])]
_TLoader = t.Callable[([
    t.Optional[str]], tuple[(t.Optional[str], t.Optional[_TOpener])])]
if t.TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse
    from _typeshed.wsgi import WSGIApplication
    from _typeshed.wsgi import WSGIEnvironment

class SharedDataMiddleware:
    """A WSGI middleware which provides static content for development
    environments or simple server setups. Its usage is quite simple::

        import os
        from werkzeug.middleware.shared_data import SharedDataMiddleware

        app = SharedDataMiddleware(app, {
            '/shared': os.path.join(os.path.dirname(__file__), 'shared')
        })

    The contents of the folder ``./shared`` will now be available on
    ``http://example.com/shared/``.  This is pretty useful during development
    because a standalone media server is not required. Files can also be
    mounted on the root folder and still continue to use the application because
    the shared data middleware forwards all unhandled requests to the
    application, even if the requests are below one of the shared folders.

    If `pkg_resources` is available you can also tell the middleware to serve
    files from package data::

        app = SharedDataMiddleware(app, {
            '/static': ('myapplication', 'static')
        })

    This will then serve the ``static`` folder in the `myapplication`
    Python package.

    The optional `disallow` parameter can be a list of :func:`~fnmatch.fnmatch`
    rules for files that are not accessible from the web.  If `cache` is set to
    `False` no caching headers are sent.

    Currently the middleware does not support non-ASCII filenames. If the
    encoding on the file system happens to match the encoding of the URI it may
    work but this could also be by accident. We strongly suggest using ASCII
    only file names for static files.

    The middleware will guess the mimetype using the Python `mimetype`
    module.  If it's unable to figure out the charset it will fall back
    to `fallback_mimetype`.

    :param app: the application to wrap.  If you don't want to wrap an
                application you can pass it :exc:`NotFound`.
    :param exports: a list or dict of exported files and folders.
    :param disallow: a list of :func:`~fnmatch.fnmatch` rules.
    :param cache: enable or disable caching headers.
    :param cache_timeout: the cache timeout in seconds for the headers.
    :param fallback_mimetype: The fallback mimetype for unknown files.

    .. versionchanged:: 1.0
        The default ``fallback_mimetype`` is
        ``application/octet-stream``. If a filename looks like a text
        mimetype, the ``utf-8`` charset is added to it.

    .. versionadded:: 0.6
        Added ``fallback_mimetype``.

    .. versionchanged:: 0.5
        Added ``cache_timeout``.
    """
    
    def __init__(self, app, exports = None, disallow = None, cache = None, cache_timeout = (None, True, 43200, 'application/octet-stream'), fallback_mimetype = ('app', 'WSGIApplication', 'exports', 'cabc.Mapping[str, str | tuple[str, str]] | t.Iterable[tuple[str, str | tuple[str, str]]]', 'disallow', 'None', 'cache', 'bool', 'cache_timeout', 'int', 'fallback_mimetype', 'str', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def is_allowed(self = None, filename = None):
        '''Subclasses can override this method to disallow the access to
        certain files.  However by providing `disallow` in the constructor
        this method is overwritten.
        '''
        return True

    
    def _opener(self = None, filename = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_file_loader(self = None, filename = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_package_loader(self = None, package = None, package_path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_directory_loader(self = None, directory = None):
        pass
    # WARNING: Decompyle incomplete

    
    def generate_etag(self = None, mtime = None, file_size = None, real_filename = ('mtime', 'datetime', 'file_size', 'int', 'real_filename', 'str', 'return', 'str')):
        fn_str = os.fsencode(real_filename)
        timestamp = mtime.timestamp()
        checksum = adler32(fn_str) & 0xFFFFFFFF
        return f'''wzsdm-{timestamp}-{file_size}-{checksum}'''

    
    def __call__(self = None, environ = None, start_response = None):
        path = get_path_info(environ)
        file_loader = None
    # WARNING: Decompyle incomplete
