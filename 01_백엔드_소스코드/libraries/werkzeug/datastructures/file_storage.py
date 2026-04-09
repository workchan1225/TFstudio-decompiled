# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_storage.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import mimetypes
import os
import typing as t
from io import BytesIO
from os import fsdecode
from os import fspath
from _internal import _plain_int
from headers import Headers
from structures import MultiDict

class FileStorage:
    """The :class:`FileStorage` class is a thin wrapper over incoming files.
    It is used by the request object to represent uploaded files.  All the
    attributes of the wrapper stream are proxied by the file storage so
    it's possible to do ``storage.read()`` instead of the long form
    ``storage.stream.read()``.
    """
    
    def __init__(self, stream, filename = None, name = None, content_type = None, content_length = (None, None, None, None, None, None), headers = ('stream', 't.IO[bytes] | None', 'filename', 'str | None', 'name', 'str | None', 'content_type', 'str | None', 'content_length', 'int | None', 'headers', 'Headers | None')):
        self.name = name
        if not stream:
            pass
        self.stream = BytesIO()
    # WARNING: Decompyle incomplete

    
    def _parse_content_type(self = None):
        if not hasattr(self, '_parsed_content_type'):
            self._parsed_content_type = http.parse_options_header(self.content_type)
            return None

    content_type = (lambda self = None: self.headers.get('content-type'))()
    content_length = (lambda self = None:
