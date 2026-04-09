# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http.pyc (Python 3.11)

import asyncio
import io
import logging
import re
import weakref
from copy import copy
from urllib.parse import urlparse
import aiohttp
import yarl
from fsspec.asyn import AbstractAsyncStreamedFile, AsyncFileSystem, sync, sync_wrapper
from fsspec.callbacks import DEFAULT_CALLBACK
from fsspec.exceptions import FSTimeoutError
from fsspec.spec import AbstractBufferedFile
from fsspec.utils import DEFAULT_BLOCK_SIZE, glob_translate, isfilelike, nullcontext, tokenize
from caching import AllBytes
ex = re.compile('<(a|A)\\s+(?:[^>]*?\\s+)?(href|HREF)=["\'](?P<url>[^"\']+)')
ex2 = re.compile('(?P<url>http[s]?://[-a-zA-Z0-9@:%_+.~#?&/=]+)')
logger = logging.getLogger('fsspec.http')

async def get_client(**kwargs):
    pass
# WARNING: Decompyle incomplete


class HTTPFileSystem(AsyncFileSystem):
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


class AsyncStreamFile(AbstractAsyncStreamedFile):
    pass
# WARNING: Decompyle incomplete


async def get_range(session, url, start, end, file = (None,), **kwargs):
    pass
# WARNING: Decompyle incomplete


async def _file_info(url, session, size_policy = ('head',), **kwargs):
    """Call HEAD on the server to get details about the file (size/checksum etc.)

    Default operation is to explicitly allow redirects and use encoding
    'identity' (no compression) to get the true size of the target.
    """
    pass
# WARNING: Decompyle incomplete


async def _file_size(url, session = (None,), *args, **kwargs):
    pass
# WARNING: Decompyle incomplete

file_size = sync_wrapper(_file_size)
