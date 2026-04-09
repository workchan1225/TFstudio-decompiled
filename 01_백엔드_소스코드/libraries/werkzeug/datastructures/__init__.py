# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from accept import Accept
from accept import CharsetAccept
from accept import LanguageAccept
from accept import MIMEAccept
from auth import Authorization
from auth import WWWAuthenticate
from cache_control import RequestCacheControl
from cache_control import ResponseCacheControl
from csp import ContentSecurityPolicy
from etag import ETags
from file_storage import FileMultiDict
from file_storage import FileStorage
from headers import EnvironHeaders
from headers import Headers
from mixins import ImmutableDictMixin
from mixins import ImmutableHeadersMixin
from mixins import ImmutableListMixin
from mixins import ImmutableMultiDictMixin
from mixins import UpdateDictMixin
from range import ContentRange
from range import IfRange
from range import Range
from structures import CallbackDict
from structures import CombinedMultiDict
from structures import HeaderSet
from structures import ImmutableDict
from structures import ImmutableList
from structures import ImmutableMultiDict
from structures import ImmutableTypeConversionDict
from structures import iter_multi_items
from structures import MultiDict
from structures import TypeConversionDict

def __getattr__(name = None):
    import warnings
    if name == 'OrderedMultiDict':
        _OrderedMultiDict = _OrderedMultiDict
        import structures
        warnings.warn("'OrderedMultiDict' is deprecated and will be removed in Werkzeug 3.2. Use 'MultiDict' instead.", DeprecationWarning, stacklevel = 2)
        return _OrderedMultiDict
    if None == 'ImmutableOrderedMultiDict':
        _ImmutableOrderedMultiDict = _ImmutableOrderedMultiDict
        import structures
        warnings.warn("'OrderedMultiDict' is deprecated and will be removed in Werkzeug 3.2. Use 'ImmutableMultiDict' instead.", DeprecationWarning, stacklevel = 2)
        return _ImmutableOrderedMultiDict
    raise None(name)
