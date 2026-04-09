# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http.pyc (Python 3.11)

from __future__ import annotations
import email.utils as email
import re
import typing as t
import warnings
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
from datetime import timezone
from enum import Enum
from hashlib import sha1
from time import mktime
from time import struct_time
from urllib.parse import quote
from urllib.parse import unquote
from urllib.request import parse_http_list as _parse_list_header
from _internal import _dt_as_utc
from _internal import _plain_int
if t.TYPE_CHECKING:
    from _typeshed.wsgi import WSGIEnvironment
_token_chars = frozenset("!#$%&'*+-.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`abcdefghijklmnopqrstuvwxyz|~")
_etag_re = re.compile('([Ww]/)?(?:"(.*?)"|(.*?))(?:\\s*,\\s*|$)')
_entity_headers = frozenset([
    'allow',
    'content-encoding',
    'content-language',
    'content-length',
    'content-location',
    'content-md5',
    'content-range',
    'content-type',
    'expires',
    'last-modified'])
_hop_by_hop_headers = frozenset([
    'connection',
    'keep-alive',
    'proxy-authenticate',
    'proxy-authorization',
    'te',
    'trailer',
    'transfer-encoding',
    'upgrade'])
# WARNING: Decompyle incomplete
