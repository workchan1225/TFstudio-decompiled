# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

__doc__ = 'Various helper functions'
import asyncio
import base64
import binascii
import contextlib
import datetime
import enum
import functools
import inspect
import netrc
import os
import platform
import re
import sys
import time
import weakref
from collections import namedtuple
from contextlib import suppress
from email.message import EmailMessage
from email.parser import HeaderParser
from email.policy import HTTP
from email.utils import parsedate
from math import ceil
from pathlib import Path
from types import MappingProxyType, TracebackType
from typing import Any, Callable, ContextManager, Dict, Generator, Generic, Iterable, Iterator, List, Mapping, Optional, Protocol, Tuple, Type, TypeVar, Union, get_args, overload
from urllib.parse import quote
from urllib.request import getproxies, proxy_bypass
import attr
from multidict import MultiDict, MultiDictProxy, MultiMapping
from propcache.api import under_cached_property as reify
from yarl import URL
from  import hdrs
from log import client_logger
if sys.version_info >= (3, 11):
    import asyncio as async_timeout
else:
    import async_timeout
__all__ = ('BasicAuth', 'ChainMapProxy', 'ETag', 'reify')
IS_MACOS = platform.system() == 'Darwin'
IS_WINDOWS = platform.system() == 'Windows'
PY_310 = sys.version_info >= (3, 10)
PY_311 = sys.version_info >= (3, 11)
_T = TypeVar('_T')
_S = TypeVar('_S')
_SENTINEL = enum.Enum('_SENTINEL', 'sentinel')
sentinel = _SENTINEL.sentinel
NO_EXTENSIONS = bool(os.environ.get('AIOHTTP_NO_EXTENSIONS'))
# WARNING: Decompyle incomplete
