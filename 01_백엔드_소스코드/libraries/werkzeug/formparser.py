# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: formparser.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from io import BytesIO
from urllib.parse import parse_qsl
from _internal import _plain_int
from datastructures import FileStorage
from datastructures import Headers
from datastructures import MultiDict
from exceptions import RequestEntityTooLarge
from http import parse_options_header
from sansio.multipart import Data
from sansio.multipart import Epilogue
from sansio.multipart import Field
from sansio.multipart import File
from sansio.multipart import MultipartDecoder
from sansio.multipart import NeedData
from wsgi import get_content_length
from wsgi import get_input_stream

try:
    from tempfile import SpooledTemporaryFile
except ImportError:
    from tempfile import TemporaryFile
    SpooledTemporaryFile = None

if t.TYPE_CHECKING:
    import typing as te
    from _typeshed.wsgi import WSGIEnvironment
    t_parse_result = tuple[(t.IO[bytes], MultiDict[(str, str)], MultiDict[(str, FileStorage)])]
    
    class TStreamFactory(te.Protocol):
        
        def __call__(self = None, total_content_length = None, content_type = None, filename = (None,), content_length = ('total_content_length', 'int | None', 'content_type', 'str | None', 'filename', 'str | None', 'content_length', 'int | None', 'return', 't.IO[bytes]')):
            pass


F = t.TypeVar('F', bound = t.Callable[(..., t.Any)])

def default_stream_factory(total_content_length = None, content_type = None, filename = None, content_length = (None,)):
    max_size = 512000
# WARNING: Decompyle incomplete


def parse_form_data(environ = None, stream_factory = None, max_form_memory_size = None, max_content_length = None, cls = (None, None, None, None, True), silent = {
    'max_form_parts': None }, *, max_form_parts):
    '''Parse the form data in the environ and return it as tuple in the form
    ``(stream, form, files)``.  You should only call this method if the
    transport method is `POST`, `PUT`, or `PATCH`.

    If the mimetype of the data transmitted is `multipart/form-data` the
    files multidict will be filled with `FileStorage` objects.  If the
    mimetype is unknown the input stream is wrapped and returned as first
    argument, else the stream is empty.

    This is a shortcut for the common usage of :class:`FormDataParser`.

    :param environ: the WSGI environment to be used for parsing.
    :param stream_factory: An optional callable that returns a new read and
                           writeable file descriptor.  This callable works
                           the same as :meth:`Response._get_file_stream`.
    :param max_form_memory_size: the maximum number of bytes to be accepted for
                           in-memory stored form data.  If the data
                           exceeds the value specified an
                           :exc:`~exceptions.RequestEntityTooLarge`
                           exception is raised.
    :param max_content_length: If this is provided and the transmitted data
                               is longer than this value an
                               :exc:`~exceptions.RequestEntityTooLarge`
                               exception is raised.
    :param cls: an optional dict class to use.  If this is not specified
                       or `None` the default :class:`MultiDict` is used.
    :param silent: If set to False parsing errors will not be caught.
    :param max_form_parts: The maximum number of multipart parts to be parsed. If this
        is exceeded, a :exc:`~exceptions.RequestEntityTooLarge` exception is raised.
    :return: A tuple in the form ``(stream, form, files)``.

    .. versionchanged:: 3.0
        The ``charset`` and ``errors`` parameters were removed.

    .. versionchanged:: 2.3
        Added the ``max_form_parts`` parameter.

    .. versionadded:: 0.5.1
       Added the ``silent`` parameter.

    .. versionadded:: 0.5
       Added the ``max_form_memory_size``, ``max_content_length``, and ``cls``
       parameters.
    '''
    return FormDataParser(stream_factory = stream_factory, max_form_memory_size = max_form_memory_size, max_content_length = max_content_length, max_form_parts = max_form_parts, silent = silent, cls = cls).parse_from_environ(environ)


class FormDataParser:
    '''This class implements parsing of form data for Werkzeug.  By itself
    it can parse multipart and url encoded form data.  It can be subclassed
    and extended but for most mimetypes it is a better idea to use the
    untouched stream and expose it as separate attributes on a request
    object.

    :param stream_factory: An optional callable that returns a new read and
                           writeable file descriptor.  This callable works
                           the same as :meth:`Response._get_file_stream`.
    :param max_form_memory_size: the maximum number of bytes to be accepted for
                           in-memory stored form data.  If the data
                           exceeds the value specified an
                           :exc:`~exceptions.RequestEntityTooLarge`
                           exception is raised.
    :param max_content_length: If this is provided and the transmitted data
                               is longer than this value an
                               :exc:`~exceptions.RequestEntityTooLarge`
                               exception is raised.
    :param cls: an optional dict class to use.  If this is not specified
                       or `None` the default :class:`MultiDict` is used.
    :param silent: If set to False parsing errors will not be caught.
    :param max_form_parts: The maximum number of multipart parts to be parsed. If this
        is exceeded, a :exc:`~exceptions.RequestEntityTooLarge` exception is raised.

    .. versionchanged:: 3.0
        The ``charset`` and ``errors`` parameters were removed.

    .. versionchanged:: 3.0
        The ``parse_functions`` attribute and ``get_parse_func`` methods were removed.

    .. versionchanged:: 2.2.3
        Added the ``max_form_parts`` parameter.

    .. versionadded:: 0.8
    '''
    
    def __init__(self = None, stream_factory = None, max_form_memory_size = None, max_content_length = None, cls = (None, None, None, None, True), silent = {
        'max_form_parts': None }, *, max_form_parts):
        pass
    # WARNING: Decompyle incomplete

    
    def parse_from_environ(self = None, environ = None):
        '''Parses the information from the environment as form data.

        :param environ: the WSGI environment to be used for parsing.
        :return: A tuple in the form ``(stream, form, files)``.
        '''
        stream = get_input_stream(environ, max_content_length = self.max_content_length)
        content_length = get_content_length(environ)
        (mimetype, options) = parse_options_header(environ.get('CONTENT_TYPE'))
        return self.parse(stream, content_length = content_length, mimetype = mimetype, options = options)

    
    def parse(self = None, stream = None, mimetype = None, content_length = (None,), options = ('stream', 't.IO[bytes]', 'mimetype', 'str', 'content_length', 'int | None', 'options', 'dict[str, str] | None', 'return', 't_parse_result')):
        '''Parses the information from the given stream, mimetype,
        content length and mimetype parameters.

        :param stream: an input stream
        :param mimetype: the mimetype of the data
        :param content_length: the content length of the incoming data
        :param options: optional mimetype parameters (used for
                        the multipart boundary for instance)
        :return: A tuple in the form ``(stream, form, files)``.

        .. versionchanged:: 3.0
            The invalid ``application/x-url-encoded`` content type is not
            treated as ``application/x-www-form-urlencoded``.
        '''
        if mimetype == 'multipart/form-data':
            parse_func = self._parse_multipart
        elif mimetype == 'application/x-www-form-urlencoded':
            parse_func = self._parse_urlencoded
        else:
            return (stream, self.cls(), self.cls())
    # WARNING: Decompyle incomplete

    
    def _parse_multipart(self, stream = None, mimetype = None, content_length = None, options = ('stream', 't.IO[bytes]', 'mimetype', 'str', 'content_length', 'int | None', 'options', 'dict[str, str]', 'return', 't_parse_result')):
        parser = MultiPartParser(stream_factory = self.stream_factory, max_form_memory_size = self.max_form_memory_size, max_form_parts = self.max_form_parts, cls = self.cls)
        boundary = options.get('boundary', '').encode('ascii')
        if not boundary:
            raise ValueError('Missing boundary')
        (form, files) = parser.parse(stream, boundary, content_length)
        return (stream, form, files)

    
    def _parse_urlencoded(self, stream = None, mimetype = None, content_length = None, options = ('stream', 't.IO[bytes]', 'mimetype', 'str', 'content_length', 'int | None', 'options', 'dict[str, str]', 'return', 't_parse_result')):
        pass
    # WARNING: Decompyle incomplete



class MultiPartParser:
    
    def __init__(self, stream_factory = None, max_form_memory_size = None, cls = None, buffer_size = (None, None, None, 65536, None), max_form_parts = ('stream_factory', 'TStreamFactory | None', 'max_form_memory_size', 'int | None', 'cls', 'type[MultiDict[str, t.Any]] | None', 'buffer_size', 'int', 'max_form_parts', 'int | None', 'return', 'None')):
        self.max_form_memory_size = max_form_memory_size
        self.max_form_parts = max_form_parts
    # WARNING: Decompyle incomplete

    
    def fail(self = None, message = None):
        raise ValueError(message)

    
    def get_part_charset(self = None, headers = None):
