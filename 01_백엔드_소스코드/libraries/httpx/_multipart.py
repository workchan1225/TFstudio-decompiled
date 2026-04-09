# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _multipart.pyc (Python 3.11)

from __future__ import annotations
import io
import mimetypes
import os
import re
import typing
from pathlib import Path
from _types import AsyncByteStream, FileContent, FileTypes, RequestData, RequestFiles, SyncByteStream
from _utils import peek_filelike_length, primitive_value_to_str, to_bytes
_HTML5_FORM_ENCODING_REPLACEMENTS = {
    '"': '%22',
    '\\': '\\\\' }
(lambda .0: pass# WARNING: Decompyle incomplete
)(range(32)())
_HTML5_FORM_ENCODING_RE = '|'.join((lambda .0: [ re.escape(c) for c in .0 ])(_HTML5_FORM_ENCODING_REPLACEMENTS.keys()()))

def _format_form_param(name = _HTML5_FORM_ENCODING_REPLACEMENTS.update, value = None):
    '''
    Encode a name/value pair within a multipart form.
    '''
    
    def replacer(match = None):
        return _HTML5_FORM_ENCODING_REPLACEMENTS[match.group(0)]

    value = _HTML5_FORM_ENCODING_RE.sub(replacer, value)
    return f'''{name}="{value}"'''.encode()


def _guess_content_type(filename = None):
