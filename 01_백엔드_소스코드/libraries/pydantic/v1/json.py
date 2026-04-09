# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: json.pyc (Python 3.11)

import datetime
from collections import deque
from decimal import Decimal
from enum import Enum
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network
from pathlib import Path
from re import Pattern
from types import GeneratorType
from typing import Any, Callable, Dict, Type, Union
from uuid import UUID
from pydantic.v1.color import Color
from pydantic.v1.networks import NameEmail
from pydantic.v1.types import SecretBytes, SecretStr
__all__ = ('pydantic_encoder', 'custom_pydantic_encoder', 'timedelta_isoformat')

def isoformat(o = None):
    return o.isoformat()


def decimal_encoder(dec_value = None):
    '''
    Encodes a Decimal as int of there\'s no exponent, otherwise float

    This is useful when we use ConstrainedDecimal to represent Numeric(x,0)
    where a integer (but not int typed) is used. Encoding this as a float
    results in failed round-tripping between encode and parse.
    Our Id type is a prime example of this.

    >>> decimal_encoder(Decimal("1.0"))
    1.0

    >>> decimal_encoder(Decimal("1"))
    1
    '''
    if dec_value.as_tuple().exponent >= 0:
        return int(dec_value)
    return None(dec_value)

# WARNING: Decompyle incomplete
