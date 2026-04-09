# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cache_control.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import typing as t
from inspect import cleandoc
from mixins import ImmutableDictMixin
from structures import CallbackDict

def cache_control_property(key = None, empty = None, type = None, *, doc):
    '''Return a new property object for a cache header. Useful if you
    want to add support for a cache extension in a subclass.

    :param key: The attribute name present in the parsed cache-control header dict.
    :param empty: The value to use if the key is present without a value.
    :param type: The type to convert the string value to instead of a string. If
        conversion raises a ``ValueError``, the returned value is ``None``.
    :param doc: The docstring for the property. If not given, it is generated
        based on the other params.

    .. versionchanged:: 3.1
        Added the ``doc`` param.

    .. versionchanged:: 2.0
        Renamed from ``cache_property``.
    '''
    pass
# WARNING: Decompyle incomplete


def _CacheControl():
    '''_CacheControl'''
    pass
# WARNING: Decompyle incomplete

_CacheControl = <NODE:27>(_CacheControl, '_CacheControl', CallbackDict[(str, t.Optional[str])])

def RequestCacheControl():
    '''RequestCacheControl'''
    __doc__ = 'A cache control for requests.  This is immutable and gives access\n    to all the request-relevant cache control headers.\n\n    To get a header of the :class:`RequestCacheControl` object again you can\n    convert the object into a string or call the :meth:`to_header` method.  If\n    you plan to subclass it and add your own items have a look at the sourcecode\n    for that class.\n\n    .. versionchanged:: 3.1\n        Dict values are always ``str | None``. Setting properties will\n        convert the value to a string. Setting a non-bool property to\n        ``False`` is equivalent to setting it to ``None``. Getting typed\n        properties will return ``None`` if conversion raises\n        ``ValueError``, rather than the string.\n\n    .. versionchanged:: 3.1\n       ``max_age`` is ``None`` if present without a value, rather\n       than ``-1``.\n\n    .. versionchanged:: 3.1\n        ``no_cache`` is a boolean, it is ``True`` instead of ``"*"``\n        when present.\n\n    .. versionchanged:: 3.1\n        ``max_stale`` is ``True`` if present without a value, rather\n        than ``"*"``.\n\n    .. versionchanged:: 3.1\n       ``no_transform`` is a boolean. Previously it was mistakenly\n       always ``None``.\n\n    .. versionchanged:: 3.1\n       ``min_fresh`` is ``None`` if present without a value, rather\n       than ``"*"``.\n\n    .. versionchanged:: 2.1\n        Setting int properties such as ``max_age`` will convert the\n        value to an int.\n\n    .. versionadded:: 0.5\n        Response-only properties are not present on this request class.\n    '
    no_cache: 'bool' = cache_control_property('no-cache', None, bool)
    max_stale: 'int | t.Literal[True] | None' = cache_control_property('max-stale', True, int)
    min_fresh: 'int | None' = cache_control_property('min-fresh', None, int)
    only_if_cached: 'bool' = cache_control_property('only-if-cached', None, bool)

RequestCacheControl = <NODE:27>(RequestCacheControl, 'RequestCacheControl', ImmutableDictMixin[(str, t.Optional[str])], _CacheControl)

class ResponseCacheControl(_CacheControl):
    '''A cache control for responses.  Unlike :class:`RequestCacheControl`
    this is mutable and gives access to response-relevant cache control
    headers.

    To get a header of the :class:`ResponseCacheControl` object again you can
    convert the object into a string or call the :meth:`to_header` method.  If
    you plan to subclass it and add your own items have a look at the sourcecode
    for that class.

    .. versionchanged:: 3.1
        Dict values are always ``str | None``. Setting properties will
        convert the value to a string. Setting a non-bool property to
        ``False`` is equivalent to setting it to ``None``. Getting typed
        properties will return ``None`` if conversion raises
        ``ValueError``, rather than the string.

    .. versionchanged:: 3.1
        ``no_cache`` is ``True`` if present without a value, rather than
        ``"*"``.

    .. versionchanged:: 3.1
        ``private`` is ``True`` if present without a value, rather than
        ``"*"``.

    .. versionchanged:: 3.1
       ``no_transform`` is a boolean. Previously it was mistakenly
       always ``None``.

    .. versionchanged:: 3.1
        Added the ``must_understand``, ``stale_while_revalidate``, and
        ``stale_if_error`` properties.

    .. versionchanged:: 2.1.1
        ``s_maxage`` converts the value to an int.

    .. versionchanged:: 2.1
        Setting int properties such as ``max_age`` will convert the
        value to an int.

    .. versionadded:: 0.5
       Request-only properties are not present on this response class.
    '''
    no_cache: 'str | t.Literal[True] | None' = cache_control_property('no-cache', True, None)
    public: 'bool' = cache_control_property('public', None, bool)
    private: 'str | t.Literal[True] | None' = cache_control_property('private', True, None)
    must_revalidate: 'bool' = cache_control_property('must-revalidate', None, bool)
    proxy_revalidate: 'bool' = cache_control_property('proxy-revalidate', None, bool)
    s_maxage: 'int | None' = cache_control_property('s-maxage', None, int)
    immutable: 'bool' = cache_control_property('immutable', None, bool)
    must_understand: 'bool' = cache_control_property('must-understand', None, bool)
    stale_while_revalidate: 'int | None' = cache_control_property('stale-while-revalidate', None, int)

from  import http
