# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: test.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
import mimetypes
import sys
import typing as t
from collections import defaultdict
from datetime import datetime
from io import BytesIO
from itertools import chain
from random import random
from tempfile import TemporaryFile
from time import time
from urllib.parse import unquote
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from _internal import _get_environ
from _internal import _wsgi_decoding_dance
from _internal import _wsgi_encoding_dance
from datastructures import Authorization
from datastructures import CallbackDict
from datastructures import CombinedMultiDict
from datastructures import EnvironHeaders
from datastructures import FileMultiDict
from datastructures import Headers
from datastructures import MultiDict
from http import dump_cookie
from http import dump_options_header
from http import parse_cookie
from http import parse_date
from http import parse_options_header
from sansio.multipart import Data
from sansio.multipart import Epilogue
from sansio.multipart import Field
from sansio.multipart import File
from sansio.multipart import MultipartEncoder
from sansio.multipart import Preamble
from urls import _urlencode
from urls import iri_to_uri
from utils import cached_property
from utils import get_content_type
from wrappers.request import Request
from wrappers.response import Response
from wsgi import ClosingIterator
from wsgi import get_current_url
if t.TYPE_CHECKING:
    import typing_extensions as te
    from _typeshed.wsgi import WSGIApplication
    from _typeshed.wsgi import WSGIEnvironment

def stream_encode_multipart(data = None, use_tempfile = None, threshold = None, boundary = (True, 512000, None)):
    '''Encode a dict of values (either strings or file descriptors or
    :class:`FileStorage` objects.) into a multipart encoded string stored
    in a file descriptor.

    .. versionchanged:: 3.0
        The ``charset`` parameter was removed.
    '''
    pass
# WARNING: Decompyle incomplete


def encode_multipart(values = None, boundary = None):
    '''Like `stream_encode_multipart` but returns a tuple in the form
    (``boundary``, ``data``) where data is bytes.

    .. versionchanged:: 3.0
        The ``charset`` parameter was removed.
    '''
    (stream, length, boundary) = stream_encode_multipart(values, use_tempfile = False, boundary = boundary)
    return (boundary, stream.read())


def _iter_data(data = None):
    '''Iterate over a mapping that might have a list of values, yielding
    all key, value pairs. Almost like iter_multi_items but only allows
    lists, not tuples, of values so tuples can be used for files.
    '''
    pass
# WARNING: Decompyle incomplete

_TAnyMultiDict = t.TypeVar('_TAnyMultiDict', bound = 'MultiDict[t.Any, t.Any]')

class EnvironBuilder:
    '''This class can be used to conveniently create a WSGI environment
    for testing purposes.  It can be used to quickly create WSGI environments
    or request objects from arbitrary data.

    The signature of this class is also used in some other places as of
    Werkzeug 0.5 (:func:`create_environ`, :meth:`Response.from_values`,
    :meth:`Client.open`).  Because of this most of the functionality is
    available through the constructor alone.

    Files and regular form data can be manipulated independently of each
    other with the :attr:`form` and :attr:`files` attributes, but are
    passed with the same argument to the constructor: `data`.

    `data` can be any of these values:

    -   a `str` or `bytes` object: The object is converted into an
        :attr:`input_stream`, the :attr:`content_length` is set and you have to
        provide a :attr:`content_type`.
    -   a `dict` or :class:`MultiDict`: The keys have to be strings. The values
        have to be either any of the following objects, or a list of any of the
        following objects:

        -   a :class:`file`-like object:  These are converted into
            :class:`FileStorage` objects automatically.
        -   a `tuple`:  The :meth:`~FileMultiDict.add_file` method is called
            with the key and the unpacked `tuple` items as positional
            arguments.
        -   a `str`:  The string is set as form data for the associated key.
    -   a file-like object: The object content is loaded in memory and then
        handled like a regular `str` or a `bytes`.

    :param path: the path of the request.  In the WSGI environment this will
                 end up as `PATH_INFO`.  If the `query_string` is not defined
                 and there is a question mark in the `path` everything after
                 it is used as query string.
    :param base_url: the base URL is a URL that is used to extract the WSGI
                     URL scheme, host (server name + server port) and the
                     script root (`SCRIPT_NAME`).
    :param query_string: an optional string or dict with URL parameters.
    :param method: the HTTP method to use, defaults to `GET`.
    :param input_stream: an optional input stream.  Do not specify this and
                         `data`.  As soon as an input stream is set you can\'t
                         modify :attr:`args` and :attr:`files` unless you
                         set the :attr:`input_stream` to `None` again.
    :param content_type: The content type for the request.  As of 0.5 you
                         don\'t have to provide this when specifying files
                         and form data via `data`.
    :param content_length: The content length for the request.  You don\'t
                           have to specify this when providing data via
                           `data`.
    :param errors_stream: an optional error stream that is used for
                          `wsgi.errors`.  Defaults to :data:`stderr`.
    :param multithread: controls `wsgi.multithread`.  Defaults to `False`.
    :param multiprocess: controls `wsgi.multiprocess`.  Defaults to `False`.
    :param run_once: controls `wsgi.run_once`.  Defaults to `False`.
    :param headers: an optional list or :class:`Headers` object of headers.
    :param data: a string or dict of form data or a file-object.
                 See explanation above.
    :param json: An object to be serialized and assigned to ``data``.
        Defaults the content type to ``"application/json"``.
        Serialized with the function assigned to :attr:`json_dumps`.
    :param environ_base: an optional dict of environment defaults.
    :param environ_overrides: an optional dict of environment overrides.
    :param auth: An authorization object to use for the
        ``Authorization`` header value. A ``(username, password)`` tuple
        is a shortcut for ``Basic`` authorization.

    .. versionchanged:: 3.0
        The ``charset`` parameter was removed.

    .. versionchanged:: 2.1
        ``CONTENT_TYPE`` and ``CONTENT_LENGTH`` are not duplicated as
        header keys in the environ.

    .. versionchanged:: 2.0
        ``REQUEST_URI`` and ``RAW_URI`` is the full raw URI including
        the query string, not only the path.

    .. versionchanged:: 2.0
        The default :attr:`request_class` is ``Request`` instead of
        ``BaseRequest``.

    .. versionadded:: 2.0
       Added the ``auth`` parameter.

    .. versionadded:: 0.15
        The ``json`` param and :meth:`json_dumps` method.

    .. versionadded:: 0.15
        The environ has keys ``REQUEST_URI`` and ``RAW_URI`` containing
        the path before percent-decoding. This is not part of the WSGI
        PEP, but many WSGI servers include it.

    .. versionchanged:: 0.6
       ``path`` and ``base_url`` can now be unicode strings that are
       encoded with :func:`iri_to_uri`.
    '''
    server_protocol = 'HTTP/1.1'
    wsgi_version = (1, 0)
    request_class = Request
    import json
    json_dumps = staticmethod(json.dumps)
    del json
    _args: 'MultiDict[str, str] | None'
    _query_string: 'str | None'
    _input_stream: 't.IO[bytes] | None'
    _form: 'MultiDict[str, str] | None'
    _files: 'FileMultiDict | None'
    
    def __init__(self, path, base_url, query_string, method, input_stream, content_type, content_length, errors_stream, multithread, multiprocess, run_once, headers, data, environ_base = None, environ_overrides = None, mimetype = None, json = ('/', None, None, 'GET', None, None, None, None, False, False, False, None, None, None, None, None, None, None), auth = ('path', 'str', 'base_url', 'str | None', 'query_string', 't.Mapping[str, str] | str | None', 'method', 'str', 'input_stream', 't.IO[bytes] | None', 'content_type', 'str | None', 'content_length', 'int | None', 'errors_stream', 't.IO[str] | None', 'multithread', 'bool', 'multiprocess', 'bool', 'run_once', 'bool', 'headers', 'Headers | t.Iterable[tuple[str, str]] | None', 'data', 'None | (t.IO[bytes] | str | bytes | t.Mapping[str, t.Any])', 'environ_base', 't.Mapping[str, t.Any] | None', 'environ_overrides', 't.Mapping[str, t.Any] | None', 'mimetype', 'str | None', 'json', 't.Mapping[str, t.Any] | None', 'auth', 'Authorization | tuple[str, str] | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    from_environ = (lambda cls = None, environ = None: headers = Headers(EnvironHeaders(environ))out = {
'path': _wsgi_decoding_dance(environ['PATH_INFO']),
'base_url': cls._make_base_url(environ['wsgi.url_scheme'], headers.pop('Host'), _wsgi_decoding_dance(environ['SCRIPT_NAME'])),
'query_string': _wsgi_decoding_dance(environ['QUERY_STRING']),
'method': environ['REQUEST_METHOD'],
'input_stream': environ['wsgi.input'],
'content_type': headers.pop('Content-Type', None),
'content_length': headers.pop('Content-Length', None),
'errors_stream': environ['wsgi.errors'],
'multithread': environ['wsgi.multithread'],
'multiprocess': environ['wsgi.multiprocess'],
'run_once': environ['wsgi.run_once'],
'headers': headers }out.update(kwargs)# WARNING: Decompyle incomplete
)()
    
    def _add_file_from_data(self = None, key = None, value = None):
        '''Called in the EnvironBuilder to add files from the data dict.'''
        pass
    # WARNING: Decompyle incomplete

    _make_base_url = (lambda scheme = None, host = None, script_root = staticmethod: urlunsplit((scheme, host, script_root, '', '')).rstrip('/') + '/')()
    base_url = (lambda self = None: self._make_base_url(self.url_scheme, self.host, self.script_root))()
    base_url = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
    content_type = (lambda self = None: ct = self.headers.get('Content-Type')# WARNING: Decompyle incomplete
)()
    content_type = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
    mimetype = (lambda self = None: ct = self.content_typect.split(';')[0].strip() if ct else None)()
    mimetype = (lambda self = None, value = None: self.content_type = get_content_type(value, 'utf-8'))()
    mimetype_params = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    content_length = (lambda self = None: self.headers.get('Content-Length', type = int))()
    content_length = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
    
    def _get_form(self = None, name = None, storage = None):
        '''Common behavior for getting the :attr:`form` and
        :attr:`files` properties.

        :param name: Name of the internal cached attribute.
        :param storage: Storage class used for the data.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _set_form(self = None, name = None, value = None):
        '''Common behavior for setting the :attr:`form` and
        :attr:`files` properties.

        :param name: Name of the internal cached attribute.
        :param value: Value to assign to the attribute.
        '''
        self._input_stream = None
        setattr(self, name, value)

    form = (lambda self = None: self._get_form('_form', MultiDict))()
    form = (lambda self = None, value = None: self._set_form('_form', value))()
    files = (lambda self = None: self._get_form('_files', FileMultiDict))()
    files = (lambda self = None, value = None: self._set_form('_files', value))()
    input_stream = (lambda self = None: self._input_stream)()
    input_stream = (lambda self = None, value = None: self._input_stream = valueself._form = Noneself._files = None)()
    query_string = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    query_string = (lambda self = None, value = None: self._query_string = valueself._args = None)()
    args = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    args = (lambda self = None, value = None: self._query_string = Noneself._args = value)()
    server_name = (lambda self = None: self.host.split(':', 1)[0])()
    server_port = (lambda self = None:
