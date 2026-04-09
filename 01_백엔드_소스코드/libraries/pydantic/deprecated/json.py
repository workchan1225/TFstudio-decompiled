# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: json.pyc (Python 3.11)

import datetime
import warnings
from collections import deque
from decimal import Decimal
from enum import Enum
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network
from pathlib import Path
from re import Pattern
from types import GeneratorType
from typing import TYPE_CHECKING, Any, Callable, Union
from uuid import UUID
from typing_extensions import deprecated
from _internal._import_utils import import_cached_base_model
from color import Color
from networks import NameEmail
from types import SecretBytes, SecretStr
from warnings import PydanticDeprecatedSince20
if not TYPE_CHECKING:
    DeprecationWarning = PydanticDeprecatedSince20
__all__ = ('pydantic_encoder', 'custom_pydantic_encoder', 'timedelta_isoformat')

def isoformat(o = None):
    return o.isoformat()


def decimal_encoder(dec_value = None):
    '''Encodes a Decimal as int of there\'s no exponent, otherwise float.

    This is useful when we use ConstrainedDecimal to represent Numeric(x,0)
    where a integer (but not int typed) is used. Encoding this as a float
    results in failed round-tripping between encode and parse.
    Our Id type is a prime example of this.

    >>> decimal_encoder(Decimal("1.0"))
    1.0

    >>> decimal_encoder(Decimal("1"))
    1
    '''
    exponent = dec_value.as_tuple().exponent
    if isinstance(exponent, int) and exponent >= 0:
        return int(dec_value)
    return None(dec_value)

# WARNING: Decompyle incomplete
