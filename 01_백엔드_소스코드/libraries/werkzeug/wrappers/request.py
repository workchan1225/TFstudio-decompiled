# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: request.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import functools
import json
import typing as t
from io import BytesIO
from _internal import _wsgi_decoding_dance
from datastructures import CombinedMultiDict
from datastructures import EnvironHeaders
from datastructures import FileStorage
from datastructures import ImmutableMultiDict
from datastructures import iter_multi_items
from datastructures import MultiDict
from exceptions import BadRequest
from exceptions import UnsupportedMediaType
from formparser import default_stream_factory
from formparser import FormDataParser
from sansio.request import Request as _SansIORequest
from utils import cached_property
from utils import environ_property
from wsgi import _get_server
from wsgi import get_input_stream
if t.TYPE_CHECKING:
    from _typeshed.wsgi import WSGIApplication
    from _typeshed.wsgi import WSGIEnvironment

class Request(_SansIORequest):
    pass
# WARNING: Decompyle incomplete
