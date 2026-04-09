# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_fileresponse.pyc (Python 3.11)

import asyncio
import io
import os
import pathlib
import sys
from contextlib import suppress
from enum import Enum, auto
from mimetypes import MimeTypes
from stat import S_ISREG
from types import MappingProxyType
from typing import IO, TYPE_CHECKING, Any, Awaitable, Callable, Final, Iterator, List, Optional, Set, Tuple, Union, cast
from  import hdrs
from abc import AbstractStreamWriter
from helpers import ETAG_ANY, ETag, must_be_empty_body
from typedefs import LooseHeaders, PathLike
from web_exceptions import HTTPForbidden, HTTPNotFound, HTTPNotModified, HTTPPartialContent, HTTPPreconditionFailed, HTTPRequestRangeNotSatisfiable
from web_response import StreamResponse
__all__ = ('FileResponse',)
if TYPE_CHECKING:
    from web_request import BaseRequest
_T_OnChunkSent = Optional[Callable[([
    bytes], Awaitable[None])]]
NOSENDFILE: Final[bool] = bool(os.environ.get('AIOHTTP_NOSENDFILE'))
CONTENT_TYPES: Final[MimeTypes] = MimeTypes()
ENCODING_EXTENSIONS = (lambda .0: pass# WARNING: Decompyle incomplete
)(('.br', '.gz')())
FALLBACK_CONTENT_TYPE = 'application/octet-stream'
ADDITIONAL_CONTENT_TYPES = MappingProxyType({
    'application/gzip': '.gz',
    'application/x-brotli': '.br',
    'application/x-bzip2': '.bz2',
    'application/x-compress': '.Z',
    'application/x-xz': '.xz' })

class _FileResponseResult(Enum):
    '''The result of the file response.'''
    SEND_FILE = auto()
    NOT_ACCEPTABLE = auto()
    PRE_CONDITION_FAILED = auto()
    NOT_MODIFIED = auto()

CONTENT_TYPES.encodings_map.clear()
for content_type, extension in ADDITIONAL_CONTENT_TYPES.items():
    CONTENT_TYPES.add_type(content_type, extension)
    _CLOSE_FUTURES: Set[asyncio.Future[None]] = set()
    
    class FileResponse(StreamResponse):
        pass
    # WARNING: Decompyle incomplete

    return None
