# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _compat.pyc (Python 3.11)

from __future__ import annotations
import sys
import typing_extensions
from typing import Any, Type, Union, Literal, Optional
from datetime import date, datetime
from typing_extensions import get_args as _get_args, get_origin as _get_origin
from _types import StrBytesIntFloat
from _datetime_parse import parse_date as _parse_date, parse_datetime as _parse_datetime
_LITERAL_TYPES = {
    Literal,
    typing_extensions.Literal}

def get_args(tp = None):
    return _get_args(tp)


def get_origin(tp = None):
    return _get_origin(tp)


def is_union(tp = None):
