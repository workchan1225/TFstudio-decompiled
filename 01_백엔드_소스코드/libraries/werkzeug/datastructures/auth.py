# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: auth.pyc (Python 3.11)

from __future__ import annotations
import base64
import binascii
from collections.abc import abc as cabc
import typing as t
from http import dump_header
from http import parse_dict_header
from http import quote_header_value
from structures import CallbackDict
if t.TYPE_CHECKING:
    import typing_extensions as te

class Authorization:
    '''Represents the parts of an ``Authorization`` request header.

    :attr:`.Request.authorization` returns an instance if the header is set.

    An instance can be used with the test :class:`.Client` request methods\' ``auth``
    parameter to send the header in test requests.

    Depending on the auth scheme, either :attr:`parameters` or :attr:`token` will be
    set. The ``Basic`` scheme\'s token is decoded into the ``username`` and ``password``
    parameters.

    For convenience, ``auth["key"]`` and ``auth.key`` both access the key in the
    :attr:`parameters` dict, along with ``auth.get("key")`` and ``"key" in auth``.

    .. versionchanged:: 2.3
        The ``token`` parameter and attribute was added to support auth schemes that use
        a token instead of parameters, such as ``Bearer``.

    .. versionchanged:: 2.3
        The object is no longer a ``dict``.

    .. versionchanged:: 0.5
        The object is an immutable dict.
    '''
    
    def __init__(self = None, auth_type = None, data = None, token = (None, None)):
        self.type = auth_type
    # WARNING: Decompyle incomplete

    
    def __getattr__(self = None, name = None):
        return self.parameters.get(name)

    
    def __getitem__(self = None, name = None):
        return self.parameters.get(name)

    
    def get(self = None, key = None, default = None):
        return self.parameters.get(key, default)

    
    def __contains__(self = None, key = None):
        return key in self.parameters

    
    def __eq__(self = None, other = None):
