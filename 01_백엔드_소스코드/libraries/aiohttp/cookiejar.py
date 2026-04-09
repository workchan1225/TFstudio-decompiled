# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cookiejar.pyc (Python 3.11)

import asyncio
import calendar
import contextlib
import datetime
import heapq
import itertools
import os
import pathlib
import pickle
import re
import time
import warnings
from collections import defaultdict
from collections.abc import Mapping
from http.cookies import BaseCookie, Morsel, SimpleCookie
from typing import DefaultDict, Dict, Iterable, Iterator, List, Optional, Set, Tuple, Union
from yarl import URL
from _cookie_helpers import preserve_morsel_with_coded_value
from abc import AbstractCookieJar, ClearCookiePredicate
from helpers import is_ip_address
from typedefs import LooseCookies, PathLike, StrOrURL
__all__ = ('CookieJar', 'DummyCookieJar')
CookieItem = Union[(str, 'Morsel[str]')]
_FORMAT_PATH = '{}/{}'.format
_FORMAT_DOMAIN_REVERSED = '{1}.{0}'.format
_MIN_SCHEDULED_COOKIE_EXPIRATION = 100
_SIMPLE_COOKIE = SimpleCookie()

class CookieJar(AbstractCookieJar):
    pass
# WARNING: Decompyle incomplete


class DummyCookieJar(AbstractCookieJar):
    pass
# WARNING: Decompyle incomplete
