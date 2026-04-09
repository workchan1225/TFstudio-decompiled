# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http.pyc (Python 3.11)

from __future__ import annotations
import re
import typing as t
from datetime import datetime
from _internal import _dt_as_utc
from http import generate_etag
from http import parse_date
from http import parse_etags
from http import parse_if_range_header
from http import unquote_etag
_etag_re = re.compile('([Ww]/)?(?:"(.*?)"|(.*?))(?:\\s*,\\s*|$)')

def is_resource_modified(http_range, http_if_range, http_if_modified_since, http_if_none_match, http_if_match = None, etag = None, data = None, last_modified = (None, None, None, None, None, None, None, None, True), ignore_if_range = ('http_range', 'str | None', 'http_if_range', 'str | None', 'http_if_modified_since', 'str | None', 'http_if_none_match', 'str | None', 'http_if_match', 'str | None', 'etag', 'str | None', 'data', 'bytes | None', 'last_modified', 'datetime | str | None', 'ignore_if_range', 'bool', 'return', 'bool')):
    '''Convenience method for conditional requests.
    :param http_range: Range HTTP header
    :param http_if_range: If-Range HTTP header
    :param http_if_modified_since: If-Modified-Since HTTP header
    :param http_if_none_match: If-None-Match HTTP header
    :param http_if_match: If-Match HTTP header
    :param etag: the etag for the response for comparison.
    :param data: or alternatively the data of the response to automatically
                 generate an etag using :func:`generate_etag`.
    :param last_modified: an optional date of the last modification.
    :param ignore_if_range: If `False`, `If-Range` header will be taken into
                            account.
    :return: `True` if the resource was modified, otherwise `False`.

    .. versionadded:: 2.2
    '''
    pass
# WARNING: Decompyle incomplete

_cookie_re = re.compile('\n    ([^=;]*)\n    (?:\\s*=\\s*\n      (\n        "(?:[^\\\\"]|\\\\.)*"\n      |\n        .*?\n      )\n    )?\n    \\s*;\\s*\n    ', flags = re.ASCII | re.VERBOSE)
_cookie_unslash_re = re.compile(b'\\\\([0-3][0-7]{2}|.)')

def _cookie_unslash_replace(m = None):
    v = m.group(1)
    if len(v) == 1:
        return v
    return None(v, 8).to_bytes(1, 'big')


def parse_cookie(cookie = None, cls = None):
    '''Parse a cookie from a string.

    The same key can be provided multiple times, the values are stored
    in-order. The default :class:`MultiDict` will have the first value
    first, and all values can be retrieved with
    :meth:`MultiDict.getlist`.

    :param cookie: The cookie header as a string.
    :param cls: A dict-like class to store the parsed cookies in.
        Defaults to :class:`MultiDict`.

    .. versionchanged:: 3.0
        Passing bytes, and the ``charset`` and ``errors`` parameters, were removed.

    .. versionadded:: 2.2
    '''
    pass
# WARNING: Decompyle incomplete

from  import datastructures as ds
