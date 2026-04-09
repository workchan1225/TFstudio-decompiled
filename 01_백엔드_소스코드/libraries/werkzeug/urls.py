# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: urls.pyc (Python 3.11)

from __future__ import annotations
import codecs
import re
import typing as t
import urllib.parse as urllib
from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlencode
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from datastructures import iter_multi_items

def _codec_error_url_quote(e = None):
    '''Used in :func:`uri_to_iri` after unquoting to re-quote any
    invalid bytes.
    '''
    out = quote(e.object[e.start:e.end], safe = '')
    return (out, e.end)

codecs.register_error('werkzeug.url_quote', _codec_error_url_quote)

def _make_unquote_part(name = None, chars = None):
    '''Create a function that unquotes all percent encoded characters except those
    given. This allows working with unquoted characters if possible while not changing
    the meaning of a given part of a URL.
    '''
    pass
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
